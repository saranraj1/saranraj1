import os

def generate_map_svg(dark=True):
    bg = "#080b12" if dark else "#f7f8fb"
    panel = "#0d131f" if dark else "#ffffff"
    border = "#1e293b" if dark else "#d9dee8"
    grid_line = "#141c2b" if dark else "#edf2f7"
    line_subtle = "#223046" if dark else "#cbd5e1"
    line_active = "#22d3ee" if dark else "#0891b2"
    line_warn = "#f59e0b" if dark else "#d97706"
    line_verify = "#34d399" if dark else "#059669"
    
    text_main = "#f1f5f9" if dark else "#0f172a"
    text_muted = "#94a3b8" if dark else "#64748b"
    text_dim = "#475569" if dark else "#94a3b8"
    accent = "#22d3ee" if dark else "#0891b2"

    w = 960
    h = 430

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Research Map: Spatial relationships across Code Intelligence, Responsible AI, AI Reliability, Agent Systems, and Verification">
<title>Research Map</title>
<defs>
  <marker id="arrow-cyan-{ 'dark' if dark else 'light' }" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="{accent}"/>
  </marker>
  <marker id="arrow-subtle-{ 'dark' if dark else 'light' }" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="{line_subtle}"/>
  </marker>
  <marker id="arrow-verify-{ 'dark' if dark else 'light' }" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="{line_verify}"/>
  </marker>
</defs>

<!-- Outer Container -->
<rect width="{w}" height="{h}" rx="12" fill="{bg}"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="12" fill="none" stroke="{border}" stroke-width="1.2"/>

<!-- Editorial Measurement Grid & Calipers -->
<g stroke="{grid_line}" stroke-width="1">
  <line x1="40" y1="56" x2="{w-40}" y2="56"/>
  <line x1="40" y1="190" x2="{w-40}" y2="190" stroke-dasharray="3 6"/>
  <line x1="40" y1="320" x2="{w-40}" y2="320" stroke-dasharray="3 6"/>
  <line x1="40" y1="{h-40}" x2="{w-40}" y2="{h-40}"/>
  
  <line x1="330" y1="56" x2="330" y2="{h-40}" stroke-dasharray="3 6"/>
  <line x1="640" y1="56" x2="640" y2="{h-40}" stroke-dasharray="3 6"/>
</g>

<!-- Top Ledger Header -->
<text x="32" y="34" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" font-weight="600" letter-spacing="1.5" fill="{text_muted}">FIG 01 // RESEARCH TOPOLOGY</text>
<text x="440" y="34" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" letter-spacing="1" fill="{text_dim}">AXIS-X: PROVABILITY · AXIS-Y: AUTONOMY DYNAMICS</text>
<text x="{w-32}" y="34" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" font-weight="600" letter-spacing="1" fill="{accent}">REF: COORD-2026.04</text>

<!-- Subtle Corner Marks -->
<path d="M 18 26 L 18 18 L 26 18" fill="none" stroke="{accent}" stroke-width="1.2"/>
<path d="M {w-18} 26 L {w-18} 18 L {w-26} 18" fill="none" stroke="{accent}" stroke-width="1.2"/>
<path d="M 18 {h-26} L 18 {h-18} L 26 {h-18}" fill="none" stroke="{accent}" stroke-width="1.2"/>
<path d="M {w-18} {h-26} L {w-18} {h-18} L {w-26} {h-18}" fill="none" stroke="{accent}" stroke-width="1.2"/>

<!-- Coordinate Measurement Notes -->
<text x="48" y="78" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_dim}">COORD: 0x01 [STATIC AST]</text>
<text x="340" y="78" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_dim}">TRANSITION: Δ_representation</text>
<text x="650" y="78" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_dim}">COORD: 0x03 [EMPIRICAL OOD]</text>

<!-- ───────────────────────────────────────────────────────────── -->
<!-- CONNECTING RESEARCH TENSION VECTORS (Thin hairlines)         -->
<!-- ───────────────────────────────────────────────────────────── -->

<!-- Vector 1: Code Intelligence -> Responsible AI (Downward) -->
<path d="M 180 148 L 180 230" fill="none" stroke="{accent}" stroke-width="1.2" marker-end="url(#arrow-cyan-{ 'dark' if dark else 'light' })"/>
<text x="190" y="195" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{accent}">syntax → semantics</text>

<!-- Vector 2: Responsible AI -> AI Reliability (Horizontal / Transversal) -->
<path d="M 320 270 L 630 145" fill="none" stroke="{line_subtle}" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arrow-subtle-{ 'dark' if dark else 'light' })"/>
<text x="440" y="190" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_dim}">probe: distribution shift</text>

<!-- Vector 3: Responsible AI -> Agent Systems (South-East) -->
<path d="M 280 297 L 430 286" fill="none" stroke="{line_active}" stroke-width="1.2" marker-end="url(#arrow-cyan-{ 'dark' if dark else 'light' })"/>
<text x="290" y="322" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_muted}">constraint propagation</text>

<!-- Vector 4: AI Reliability -> Verification (South-East Anchor) -->
<path d="M 755 160 L 755 315" fill="none" stroke="{line_subtle}" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arrow-subtle-{ 'dark' if dark else 'light' })"/>
<text x="765" y="240" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_dim}">formal bounds</text>

<!-- Vector 5: Agent Systems -> Verification (Horizontal to Anchor) -->
<path d="M 660 286 L 700 320" fill="none" stroke="{line_verify}" stroke-width="1.5" marker-end="url(#arrow-verify-{ 'dark' if dark else 'light' })"/>
<text x="630" y="335" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" font-weight="600" fill="{line_verify}">provenance audit</text>


<!-- ───────────────────────────────────────────────────────────── -->
<!-- ASYMMETRIC RESEARCH NODES                                    -->
<!-- ───────────────────────────────────────────────────────────── -->

<!-- NODE 01: CODE INTELLIGENCE (North-West) -->
<g transform="translate(60, 95)">
  <rect width="240" height="52" rx="6" fill="{panel}" stroke="{border}" stroke-width="1"/>
  <rect x="0" y="0" width="4" height="52" rx="2" fill="{accent}"/>
  <text x="16" y="20" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" font-weight="600" letter-spacing="1" fill="{accent}">[01] FOUNDATION</text>
  <text x="16" y="38" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13" font-weight="700" letter-spacing="0.5" fill="{text_main}">CODE INTELLIGENCE</text>
  <text x="228" y="20" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_dim}">cov(AST, Impact)</text>
</g>

<!-- NODE 02: RESPONSIBLE AI (Mid-West) -->
<g transform="translate(60, 245)">
  <rect width="240" height="52" rx="6" fill="{panel}" stroke="{border}" stroke-width="1"/>
  <rect x="0" y="0" width="4" height="52" rx="2" fill="{accent}"/>
  <text x="16" y="20" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" font-weight="600" letter-spacing="1" fill="{accent}">[02] GOVERNANCE</text>
  <text x="16" y="38" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13" font-weight="700" letter-spacing="0.5" fill="{text_main}">RESPONSIBLE AI</text>
  <text x="228" y="20" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_dim}">Δ_proxy leakage</text>
</g>

<!-- NODE 03: AI RELIABILITY (North-East / Mid-East) -->
<g transform="translate(630, 105)">
  <rect width="250" height="54" rx="6" fill="{panel}" stroke="{line_warn}" stroke-width="1"/>
  <rect x="0" y="0" width="4" height="54" rx="2" fill="{line_warn}"/>
  <text x="16" y="20" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" font-weight="600" letter-spacing="1" fill="{line_warn}">[03] ROBUSTNESS &amp; OOD</text>
  <text x="16" y="39" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13" font-weight="700" letter-spacing="0.5" fill="{text_main}">AI RELIABILITY</text>
  <text x="238" y="20" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_dim}">τ_boundary</text>
</g>

<!-- NODE 04: AGENT SYSTEMS (Center-South) -->
<g transform="translate(430, 260)">
  <rect width="230" height="52" rx="6" fill="{panel}" stroke="{border}" stroke-width="1"/>
  <rect x="0" y="0" width="4" height="52" rx="2" fill="{accent}"/>
  <text x="16" y="20" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" font-weight="600" letter-spacing="1" fill="{accent}">[04] DYNAMICS</text>
  <text x="16" y="38" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13" font-weight="700" letter-spacing="0.5" fill="{text_main}">AGENT SYSTEMS</text>
  <text x="218" y="20" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_dim}">game_consensus</text>
</g>

<!-- NODE 05: VERIFICATION (South-East Anchor) -->
<g transform="translate(700, 320)">
  <rect width="220" height="52" rx="6" fill="{panel}" stroke="{line_verify}" stroke-width="1.2"/>
  <rect x="0" y="0" width="4" height="52" rx="2" fill="{line_verify}"/>
  <text x="16" y="20" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" font-weight="700" letter-spacing="1" fill="{line_verify}">[05] FORMAL PROOFS</text>
  <text x="16" y="38" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13" font-weight="700" letter-spacing="0.5" fill="{text_main}">VERIFICATION</text>
  <text x="208" y="20" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{line_verify}">P(H | E) = 1.0</text>
</g>

<!-- Bottom Metadata Strip -->
<text x="40" y="{h-18}" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_dim}">TOPOLOGY METRIC: LATENT COUPLING · INDEPENDENT VERIFIER ARCHITECTURE</text>
<text x="{w-40}" y="{h-18}" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" letter-spacing="1" fill="{accent}">STATUS // OPEN RESEARCH</text>

</svg>"""
    return svg

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    with open("assets/map-dark.svg", "w", encoding="utf-8") as f:
        f.write(generate_map_svg(dark=True))
    with open("assets/map-light.svg", "w", encoding="utf-8") as f:
        f.write(generate_map_svg(dark=False))
    print("Generated assets/map-dark.svg and assets/map-light.svg successfully!")
