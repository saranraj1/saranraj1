import fs from "node:fs";

const login = process.env.GITHUB_LOGIN || "saranraj1";

async function fetchContributionData(user) {
  // First attempt: fetch from public GitHub profile contributions endpoint
  try {
    const res = await fetch(`https://github.com/users/${user}/contributions`, {
      headers: {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
      }
    });

    if (res.ok) {
      const html = await res.text();
      const totalMatch = html.match(/([\d,]+)\s+contributions\s+in the last year/);
      const totalContributions = totalMatch ? parseInt(totalMatch[1].replace(/,/g, ""), 10) : 0;

      const tooltipMap = new Map();
      for (const m of html.matchAll(/<tool-tip[^>]*for="([^"]+)"[^>]*>(.*?)<\/tool-tip>/gs)) {
        tooltipMap.set(m[1], m[2].trim());
      }

      const trMatches = [...html.matchAll(/<tr[^>]*>(.*?)<\/tr>/gs)];
      if (trMatches.length >= 8) {
        const monthTr = trMatches[0][1];
        const monthLabels = [];
        let colIndex = 0;
        for (const m of monthTr.matchAll(/<td([^>]*)>(.*?)<\/td>/gs)) {
          const attrs = m[1];
          const content = m[2];
          const colspanMatch = attrs.match(/colspan="(\d+)"/);
          const colspan = colspanMatch ? parseInt(colspanMatch[1], 10) : 1;
          const labelMatch = content.match(/<span aria-hidden="true"[^>]*>([^<]+)<\/span>/);
          if (labelMatch) {
            monthLabels.push({ label: labelMatch[1].trim(), col: colIndex });
          }
          colIndex += colspan;
        }

        const columns = [];
        for (let r = 0; r < 7; r++) {
          const rowHtml = trMatches[r + 1][1];
          const dayTds = [...rowHtml.matchAll(/<td([^>]*data-date="[^"]+"[^>]*)>/g)];
          dayTds.forEach((tdMatch, c) => {
            if (!columns[c]) columns[c] = [];
            const attrs = tdMatch[1];
            const date = attrs.match(/data-date="([^"]+)"/)?.[1];
            const level = attrs.match(/data-level="([^"]+)"/)?.[1];
            const id = attrs.match(/id="([^"]+)"/)?.[1];
            const tip = tooltipMap.get(id) || "";
            let count = 0;
            const countMatch = tip.match(/^([\d,]+)\s+contribution/);
            if (countMatch) {
              count = parseInt(countMatch[1].replace(/,/g, ""), 10);
            }
            columns[c][r] = {
              date,
              level: parseInt(level || "0", 10),
              count,
              tip
            };
          });
        }

        return { totalContributions, monthLabels, columns };
      }
    }
  } catch (err) {
    console.warn("Public contributions fetch failed, trying GraphQL if token is available:", err.message);
  }

  // Fallback to GraphQL if token exists
  const token = process.env.PROFILE_TOKEN || process.env.GITHUB_TOKEN;
  if (!token) {
    throw new Error(`Could not fetch contribution data for ${user} and no token was provided.`);
  }

  const query = `
  query($user:String!) {
    user(login:$user) {
      contributionsCollection {
        contributionCalendar {
          totalContributions
          weeks {
            firstDay
            contributionDays { date contributionCount contributionLevel weekday }
          }
          months { name firstDay totalWeeks }
        }
      }
    }
  }`;

  const gqlRes = await fetch("https://api.github.com/graphql", {
    method: "POST",
    headers: {
      Authorization: `bearer ${token}`,
      Accept: "application/vnd.github+json",
      "Content-Type": "application/json",
      "User-Agent": "saranraj-profile-generator"
    },
    body: JSON.stringify({ query, variables: { user } })
  });

  if (!gqlRes.ok) {
    throw new Error(`GraphQL HTTP ${gqlRes.status}: ${await gqlRes.text()}`);
  }

  const gqlBody = await gqlRes.json();
  const cal = gqlBody.data?.user?.contributionsCollection?.contributionCalendar;
  if (!cal) {
    throw new Error(`GraphQL returned no calendar: ${JSON.stringify(gqlBody)}`);
  }

  const levelMap = {
    NONE: 0,
    FIRST_QUARTILE: 1,
    SECOND_QUARTILE: 2,
    THIRD_QUARTILE: 3,
    FOURTH_QUARTILE: 4
  };

  const columns = cal.weeks.map(week => {
    const col = new Array(7).fill(null);
    week.contributionDays.forEach(d => {
      col[d.weekday] = {
        date: d.date,
        level: levelMap[d.contributionLevel] || 0,
        count: d.contributionCount,
        tip: `${d.contributionCount} contributions on ${d.date}`
      };
    });
    return col;
  });

  let currentCol = 0;
  const monthLabels = cal.months.map(m => {
    const item = { label: m.name.slice(0, 3), col: currentCol };
    currentCol += m.totalWeeks;
    return item;
  });

  return { totalContributions: cal.totalContributions, monthLabels, columns };
}

function esc(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function makeSvg(data, dark = true) {
  const { totalContributions, monthLabels, columns } = data;
  const numCols = columns.length;

  const bg = dark ? "#080b12" : "#f7f8fb";
  const panel = dark ? "#0e1420" : "#ffffff";
  const line = dark ? "#263244" : "#d9dee8";
  const muted = dark ? "#8e9aaa" : "#667085";
  const textMain = dark ? "#e8edf5" : "#18202b";
  const accent = dark ? "#22d3ee" : "#0891b2";

  // Cyan / Teal Matrix Palette
  const paletteDark = ["#151c29", "#0e3a50", "#087ea4", "#06b6d4", "#22d3ee"];
  const paletteLight = ["#ebedf0", "#bae6fd", "#38bdf8", "#0284c7", "#0369a1"];
  const pal = dark ? paletteDark : paletteLight;

  const startX = 100;
  const startY = 88;
  const step = 15;
  const cellSize = 11;
  const cellRadius = 2.5;

  // Month labels
  let monthSvg = "";
  monthLabels.forEach(m => {
    const mx = startX + m.col * step;
    monthSvg += `<text x="${mx}" y="${startY - 12}" font-family="Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="11" fill="${muted}">${esc(m.label)}</text>`;
  });

  // Weekday labels (Mon, Wed, Fri)
  const weekdays = [
    { label: "Mon", row: 1 },
    { label: "Wed", row: 3 },
    { label: "Fri", row: 5 }
  ];
  let weekdaySvg = "";
  weekdays.forEach(w => {
    const wy = startY + w.row * step + 9;
    weekdaySvg += `<text x="${startX - 12}" y="${wy}" text-anchor="end" font-family="Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="10" fill="${muted}">${w.label}</text>`;
  });

  // Calendar cells
  let rects = "";
  columns.forEach((col, c) => {
    col.forEach((day, r) => {
      if (!day) return;
      const x = startX + c * step;
      const y = startY + r * step;
      const color = pal[day.level] || pal[0];
      const recent = c >= numCols - 3;
      const delay = (((c * 7 + r) % 21) * 0.04).toFixed(3);
      rects += `<rect class="cell${recent && day.count > 0 ? " pulse" : ""}" style="--d:${delay}s" x="${x}" y="${y}" width="${cellSize}" height="${cellSize}" rx="${cellRadius}" fill="${color}"><title>${esc(day.date)}: ${day.count} contributions</title></rect>`;
    });
  });

  const calendarEndX = startX + numCols * step;
  const legendStartX = calendarEndX - 130;
  const legendY = startY + 7 * step + 16;

  let legendSquares = "";
  pal.forEach((color, i) => {
    legendSquares += `<rect x="${legendStartX + 34 + i * 14}" y="${legendY - 9}" width="10" height="10" rx="2" fill="${color}"/>`;
  });

  const generatedDate = new Date().toISOString().slice(0, 10);

  return `<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="260" viewBox="0 0 1000 260" role="img" aria-label="Activity Signal trace for ${esc(login)}">
<title>Activity Signal trace for ${esc(login)}</title>
<rect width="1000" height="260" rx="14" fill="${bg}"/>
<rect x="1" y="1" width="998" height="258" rx="14" fill="none" stroke="${line}"/>

<!-- Top Research OS Header -->
<rect x="22" y="16" width="956" height="38" rx="8" fill="${panel}" stroke="${line}"/>
<circle cx="44" cy="35" r="4.5" fill="#ff5f57"/>
<circle cx="60" cy="35" r="4.5" fill="#febc2e"/>
<circle cx="76" cy="35" r="4.5" fill="#28c840"/>
<text x="96" y="40" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" letter-spacing="1" fill="${muted}">ACTIVITY / SIGNAL // <tspan fill="${textMain}" font-weight="600">PUBLIC EVIDENCE TRACE</tspan></text>
<text x="962" y="40" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" font-weight="600" letter-spacing="0.5" fill="${accent}">MODE: CONTINUOUS</text>

<!-- Grid & Labels -->
${monthSvg}
${weekdaySvg}
${rects}

<!-- Legend & Footer -->
<text x="${startX}" y="${legendY}" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" letter-spacing="1" fill="${muted}">SIGNAL INTENSITY</text>
<text x="${legendStartX}" y="${legendY}" font-family="Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="10" fill="${muted}">Low</text>
${legendSquares}
<text x="${legendStartX + 109}" y="${legendY}" font-family="Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="10" fill="${muted}">High</text>

<text x="962" y="244" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" letter-spacing="1" fill="${muted}">LOG: ${esc(generatedDate)}</text>
</svg>`;
}

const data = await fetchContributionData(login);
console.log(`Fetched ${data.totalContributions} total contributions across ${data.columns.length} weeks for ${login}`);

fs.mkdirSync("assets", { recursive: true });
fs.writeFileSync("assets/activity-dark.svg", makeSvg(data, true));
fs.writeFileSync("assets/activity-light.svg", makeSvg(data, false));
console.log("Successfully generated assets/activity-dark.svg and assets/activity-light.svg!");
