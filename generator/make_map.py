import os

def generate_map_svg(dark=True):
    bg = "#070b14" if dark else "#f6f8fb"
    panel = "#0b1220" if dark else "#ffffff"
    border = "#1a2942" if dark else "#d5dbe5"
    grid_subtle = "rgba(34, 211, 238, 0.08)" if dark else "rgba(8, 145, 178, 0.08)"
    grid_major = "rgba(34, 211, 238, 0.16)" if dark else "rgba(8, 145, 178, 0.16)"
    line_subtle = "#1e3352" if dark else "#cbd5e1"
    line_active = "#22d3ee" if dark else "#0891b2"
    line_warn = "#f59e0b" if dark else "#d97706"
    line_verify = "#34d399" if dark else "#059669"
    
    text_main = "#f1f5f9" if dark else "#0f172a"
    text_muted = "#94a3b8" if dark else "#64748b"
    text_dim = "#415574" if dark else "#94a3b8"
    accent = "#22d3ee" if dark else "#0891b2"

    w = 960
    h = 430

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Research Blueprint: Asymmetric technical topology across Code Intelligence, Responsible AI, AI Reliability, Agent Systems, and Verification">
<title>Research Blueprint — Topology</title>
<defs>
  <pattern id="blueprint-grid-{ 'dark' if dark else 'light' }" width="24" height="24" patternUnits="userSpaceOnUse">
    <path d="M 24 0 L 0 0 0 24" fill="none" stroke="{grid_subtle}" stroke-width="0.75"/>
  </pattern>
  <marker id="bp-arrow-cyan-{ 'dark' if dark else 'light' }" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 2 L 7 5 L 0 8 z" fill="{accent}"/>
  </marker>
  <marker id="bp-arrow-subtle-{ 'dark' if dark else 'light' }" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 2 L 7 5 L 0 8 z" fill="{line_subtle}"/>
  </marker>
  <marker id="bp-arrow-verify-{ 'dark' if dark else 'light' }" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 2 L 7 5 L 0 8 z" fill="{line_verify}"/>
  </marker>
</defs>

<!-- Outer Container -->
<rect width="{w}" height="{h}" rx="10" fill="{bg}"/>
<rect width="{w}" height="{h}" rx="10" fill="url(#blueprint-grid-{ 'dark' if dark else 'light' })"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="10" fill="none" stroke="{border}" stroke-width="1.2"/>

<!-- Major Construction Caliper Lines -->
<g stroke="{grid_major}" stroke-width="1">
  <line x1="30" y1="52" x2="{w-30}" y2="52"/>
  <line x1="30" y1="190" x2="{w-30}" y2="190" stroke-dasharray="2 6"/>
  <line x1="30" y1="324" x2="{w-30}" y2="324" stroke-dasharray="2 6"/>
  <line x1="30" y1="{h-36}" x2="{w-30}" y2="{h-36}"/>
  
  <line x1="320" y1="52" x2="320" y2="{h-36}" stroke-dasharray="2 6"/>
  <line x1="640" y1="52" x2="640" y2="{h-36}" stroke-dasharray="2 6"/>
</g>

<!-- Blueprint Top Ledger Header -->
<text x="32" y="32" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" font-weight="700" letter-spacing="1.5" fill="{accent}">BLUEPRINT 01 // RESEARCH TOPOLOGY</text>
<text x="440" y="32" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9.5" letter-spacing="1" fill="{text_dim}">LAB // INDEPENDENT RESEARCH</text>
<text x="{w-32}" y="32" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" font-weight="600" letter-spacing="1" fill="{text_muted}">SPECIMEN // SR-01</text>

<!-- Blueprint Corner Crosshairs -->
<g stroke="{accent}" stroke-width="1">
  <path d="M 14 20 L 14 14 L 20 14"/>
  <path d="M {w-14} 20 L {w-14} 14 L {w-20} 14"/>
  <path d="M 14 {h-20} L 14 {h-14} L 20 {h-14}"/>
  <path d="M {w-14} {h-20} L {w-14} {h-14} L {w-20} {h-14}"/>
  <circle cx="14" cy="14" r="1.5" fill="{accent}"/>
  <circle cx="{w-14}" cy="14" r="1.5" fill="{accent}"/>
  <circle cx="14" cy="{h-14}" r="1.5" fill="{accent}"/>
  <circle cx="{w-14}" cy="{h-14}" r="1.5" fill="{accent}"/>
</g>

<!-- Coordinate Reference Ticks -->
<text x="40" y="74" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" fill="{text_dim}">[AXIS: SYNTACTIC STRUCTURE]</text>
<text x="332" y="74" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" fill="{text_dim}">[TRANSITION: REPRESENTATION PROBE]</text>
<text x="652" y="74" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" fill="{text_dim}">[AXIS: EMPIRICAL BOUNDS]</text>

<!-- ───────────────────────────────────────────────────────────── -->
<!-- BLUEPRINT CONNECTING VECTORS (Thin construction lines)       -->
<!-- ───────────────────────────────────────────────────────────── -->

<!-- Vector 1: Code Intelligence -> Responsible AI (Downward) -->
<path d="M 180 148 L 180 232" fill="none" stroke="{accent}" stroke-width="1.2" marker-end="url(#bp-arrow-cyan-{ 'dark' if dark else 'light' })"/>
<text x="190" y="196" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{accent}">syntax → semantics</text>

<!-- Vector 2: Responsible AI -> AI Reliability (Transversal Construction Line) -->
<path d="M 320 270 L 630 145" fill="none" stroke="{line_subtle}" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#bp-arrow-subtle-{ 'dark' if dark else 'light' })"/>
<text x="430" y="188" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_dim}">probe: distribution shift</text>

<!-- Vector 3: Responsible AI -> Agent Systems (South-East) -->
<path d="M 280 297 L 430 286" fill="none" stroke="{line_active}" stroke-width="1.2" marker-end="url(#bp-arrow-cyan-{ 'dark' if dark else 'light' })"/>
<text x="290" y="322" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_muted}">constraint propagation</text>

<!-- Vector 4: AI Reliability -> Verification (South-East Anchor) -->
<path d="M 755 160 L 755 315" fill="none" stroke="{line_subtle}" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#bp-arrow-subtle-{ 'dark' if dark else 'light' })"/>
<text x="765" y="240" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_dim}">formal bounds</text>

<!-- Vector 5: Agent Systems -> Verification (Horizontal to Anchor) -->
<path d="M 660 286 L 700 320" fill="none" stroke="{line_verify}" stroke-width="1.5" marker-end="url(#bp-arrow-verify-{ 'dark' if dark else 'light' })"/>
<text x="630" y="336" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" font-weight="600" fill="{line_verify}">provenance audit</text>

<!-- ───────────────────────────────────────────────────────────── -->
<!-- BLUEPRINT SPECIMEN NODES                                      -->
<!-- ───────────────────────────────────────────────────────────── -->

<!-- NODE 01: CODE INTELLIGENCE (North-West) -->
<g transform="translate(60, 95)">
  <rect width="240" height="52" rx="4" fill="{panel}" stroke="{border}" stroke-width="1"/>
  <rect x="0" y="0" width="3.5" height="52" rx="1" fill="{accent}"/>
  <text x="14" y="19" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" font-weight="700" letter-spacing="1" fill="{accent}">[01] STRUCTURE</text>
  <text x="14" y="38" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13" font-weight="700" letter-spacing="0.5" fill="{text_main}">CODE INTELLIGENCE</text>
  <text x="228" y="19" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" fill="{text_dim}">AST / Impact</text>
</g>

<!-- NODE 02: RESPONSIBLE AI (Mid-West) -->
<g transform="translate(60, 245)">
  <rect width="240" height="52" rx="4" fill="{panel}" stroke="{border}" stroke-width="1"/>
  <rect x="0" y="0" width="3.5" height="52" rx="1" fill="{accent}"/>
  <text x="14" y="19" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" font-weight="700" letter-spacing="1" fill="{accent}">[02] FAIRNESS</text>
  <text x="14" y="38" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13" font-weight="700" letter-spacing="0.5" fill="{text_main}">RESPONSIBLE AI</text>
  <text x="228" y="19" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" fill="{text_dim}">Proxy Leakage</text>
</g>

<!-- NODE 03: AI RELIABILITY (North-East / Mid-East) -->
<g transform="translate(630, 105)">
  <rect width="250" height="54" rx="4" fill="{panel}" stroke="{line_warn}" stroke-width="1"/>
  <rect x="0" y="0" width="3.5" height="54" rx="1" fill="{line_warn}"/>
  <text x="14" y="19" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" font-weight="700" letter-spacing="1" fill="{line_warn}">[03] ROBUSTNESS &amp; OOD</text>
  <text x="14" y="39" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13" font-weight="700" letter-spacing="0.5" fill="{text_main}">AI RELIABILITY</text>
  <text x="238" y="19" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" fill="{text_dim}">Boundary Decay</text>
</g>

<!-- NODE 04: AGENT SYSTEMS (Center-South) -->
<g transform="translate(430, 260)">
  <rect width="230" height="52" rx="4" fill="{panel}" stroke="{border}" stroke-width="1"/>
  <rect x="0" y="0" width="3.5" height="52" rx="1" fill="{accent}"/>
  <text x="14" y="19" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" font-weight="700" letter-spacing="1" fill="{accent}">[04] DYNAMICS</text>
  <text x="14" y="38" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13" font-weight="700" letter-spacing="0.5" fill="{text_main}">AGENT SYSTEMS</text>
  <text x="218" y="19" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" fill="{text_dim}">Consensus</text>
</g>

<!-- NODE 05: VERIFICATION (South-East Anchor) -->
<g transform="translate(700, 320)">
  <rect width="220" height="52" rx="4" fill="{panel}" stroke="{line_verify}" stroke-width="1.2"/>
  <rect x="0" y="0" width="3.5" height="52" rx="1" fill="{line_verify}"/>
  <text x="14" y="19" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" font-weight="700" letter-spacing="1" fill="{line_verify}">[05] PROOFS</text>
  <text x="14" y="38" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13" font-weight="700" letter-spacing="0.5" fill="{text_main}">VERIFICATION</text>
  <text x="208" y="19" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" fill="{line_verify}">P(H|E) = 1.0</text>
</g>

<!-- Bottom Blueprint Ledger -->
<text x="32" y="{h-16}" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" fill="{text_dim}">CONSTRUCTION: ASYMMETRIC TOPOLOGY · PROOF GATES · AUDIT TRACE</text>
<text x="{w-32}" y="{h-16}" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" letter-spacing="1" fill="{accent}">STATUS // ACTIVE BLUEPRINT</text>

</svg>"""
    return svg

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    with open("assets/map-dark.svg", "w", encoding="utf-8") as f:
        f.write(generate_map_svg(dark=True))
    with open("assets/map-light.svg", "w", encoding="utf-8") as f:
        f.write(generate_map_svg(dark=False))
    print("Generated assets/map-dark.svg and assets/map-light.svg successfully!")
