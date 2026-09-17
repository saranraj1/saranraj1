import fs from "node:fs";

const token = process.env.PROFILE_TOKEN || process.env.GITHUB_TOKEN;
const login = process.env.GITHUB_LOGIN || "saranraj1";

if (!token) {
  throw new Error("No GitHub token found. Set PROFILE_TOKEN or GITHUB_TOKEN.");
}

const query = `
query($login:String!) {
  user(login:$login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays { date contributionCount contributionLevel }
        }
      }
    }
  }
}`;

const res = await fetch("https://api.github.com/graphql", {
  method: "POST",
  headers: {
    Authorization: `bearer ${token}`,
    Accept: "application/vnd.github+json",
    "Content-Type": "application/json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "saranraj-profile-generator"
  },
  body: JSON.stringify({ query, variables: { login } })
});

if (!res.ok) {
  throw new Error(`GitHub GraphQL HTTP ${res.status}: ${await res.text()}`);
}

const body = await res.json();
if (body.errors?.length) {
  throw new Error(`GitHub GraphQL error: ${JSON.stringify(body.errors)}`);
}

const cal = body.data?.user?.contributionsCollection?.contributionCalendar;
if (!cal) {
  throw new Error(`Could not read the contribution calendar for ${login}.`);
}

const days = cal.weeks.flatMap((week) => week.contributionDays);
const palette = {
  NONE: "#151c29",
  FIRST_QUARTILE: "#283548",
  SECOND_QUARTILE: "#3d536f",
  THIRD_QUARTILE: "#637e9d",
  FOURTH_QUARTILE: "#8ea9c4"
};

function esc(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function makeSvg(dark = true) {
  const bg = dark ? "#080b12" : "#f7f8fb";
  const panel = dark ? "#0e1420" : "#ffffff";
  const line = dark ? "#263244" : "#d9dee8";
  const muted = dark ? "#8e9aaa" : "#667085";
  const fg = dark ? "#e8edf5" : "#18202b";
  const accent = dark ? "#22d3ee" : "#0e7490";
  const startX = 100;
  const startY = 96;
  const stepX = 15;
  const stepY = 15;
  const cols = Math.ceil(days.length / 7);
  const maxX = startX + Math.max(0, cols - 1) * stepX;

  let rects = "";
  days.forEach((day, i) => {
    const c = Math.floor(i / 7);
    const r = i % 7;
    const x = startX + c * stepX;
    const y = startY + r * stepY;
    const recent = i >= Math.max(0, days.length - 21);
    const delay = ((i % 21) * 0.035).toFixed(3);
    rects += `<rect class="cell${recent ? " recent" : ""}" style="--d:${delay}s" x="${x}" y="${y}" width="11" height="11" rx="2" fill="${palette[day.contributionLevel] || palette.NONE}"><title>${esc(day.date)}: ${day.contributionCount} contributions</title></rect>`;
  });

  const firstDate = days[0]?.date || "";
  const lastDate = days.at(-1)?.date || "";
  const generated = new Date().toISOString().slice(0, 10);

  return `<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="270" viewBox="0 0 1000 270" role="img" aria-labelledby="title desc">
<title id="title">GitHub contribution activity for ${esc(login)}</title>
<desc id="desc">Contribution calendar from ${esc(firstDate)} through ${esc(lastDate)}, generated ${esc(generated)}.</desc>
<style>
  .cell { transform-box: fill-box; transform-origin: center; }
  .recent { animation: pulse 2.8s ease-in-out var(--d) infinite alternate; }
  @keyframes pulse { from { opacity: .72; } to { opacity: 1; } }
</style>
<rect width="1000" height="270" rx="18" fill="${bg}"/>
<rect x="1" y="1" width="998" height="268" rx="18" fill="none" stroke="${line}"/>
<rect x="22" y="18" width="956" height="38" rx="10" fill="${panel}" stroke="${line}"/>
<text x="38" y="43" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="12" fill="${muted}">GITHUB ACTIVITY // ${esc(login.toUpperCase())}</text>
<text x="962" y="43" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="12" fill="${accent}">${cal.totalContributions} contributions</text>
${rects}
<text x="100" y="221" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" fill="${muted}">LESS</text>
<text x="${Math.min(maxX, 880)}" y="221" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" fill="${muted}">MORE</text>
<text x="38" y="250" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" fill="${muted}">BUILD → EXPERIMENT → VERIFY → SHIP</text>
<text x="962" y="250" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" fill="${muted}">UPDATED ${esc(generated)}</text>
</svg>`;
}

fs.mkdirSync("assets", { recursive: true });
fs.writeFileSync("assets/activity-dark.svg", makeSvg(true));
fs.writeFileSync("assets/activity-light.svg", makeSvg(false));
console.log(`Generated ${days.length} contribution days for ${login}: ${cal.totalContributions} contributions`);
