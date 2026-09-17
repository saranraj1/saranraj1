import os

def generate_systems_svg(dark=True):
    bg = "#080b12" if dark else "#f7f8fb"
    panel = "#0d131f" if dark else "#ffffff"
    border = "#1e293b" if dark else "#d9dee8"
    grid_line = "#141c2b" if dark else "#edf2f7"
    line_subtle = "#223046" if dark else "#cbd5e1"
    accent = "#22d3ee" if dark else "#0891b2"
    warn = "#f59e0b" if dark else "#d97706"
    verify = "#34d399" if dark else "#059669"
    
    text_main = "#f1f5f9" if dark else "#0f172a"
    text_muted = "#94a3b8" if dark else "#64748b"
    text_dim = "#475569" if dark else "#94a3b8"

    w = 960
    h = 280

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Systems: Four core research projects — TITAN, DARA v2, SILENTBIAS, and AGENT-NOIR">
<title>Systems</title>

<!-- Outer Container -->
<rect width="{w}" height="{h}" rx="12" fill="{bg}"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="12" fill="none" stroke="{border}" stroke-width="1.2"/>

<!-- Top Ledger Header -->
<text x="32" y="32" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" font-weight="600" letter-spacing="1.5" fill="{text_muted}">03 // SYSTEMS</text>
<text x="480" y="32" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" letter-spacing="1" fill="{text_dim}">CORE RESEARCH SPECIMENS</text>
<text x="{w-32}" y="32" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" font-weight="600" letter-spacing="1" fill="{accent}">4 FLAGSHIP SYSTEMS</text>

<line x1="24" y1="46" x2="{w-24}" y2="46" stroke="{border}" stroke-width="1"/>

<!-- Center Dividing Hairline -->
<line x1="480" y1="56" x2="480" y2="{h-36}" stroke="{border}" stroke-width="1" stroke-dasharray="4 4"/>

<!-- ───────────────────────────────────────────────────────────── -->
<!-- QUADRANT 1: TITAN (North-West)                                -->
<!-- ───────────────────────────────────────────────────────────── -->
<g transform="translate(32, 60)">
  <rect width="424" height="92" rx="6" fill="{panel}" stroke="{border}" stroke-width="1"/>
  <rect x="0" y="0" width="3.5" height="92" rx="2" fill="{accent}"/>
  
  <text x="16" y="22" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" font-weight="700" letter-spacing="1" fill="{accent}">[01] SPECIMEN // SYNTAX &amp; PROOFS</text>
  <text x="16" y="42" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="14" font-weight="700" letter-spacing="0.5" fill="{text_main}">TITAN</text>
  <text x="80" y="42" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" font-weight="500" fill="{text_muted}">CHANGE-AWARE CODE INTELLIGENCE</text>
  
  <text x="16" y="62" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" fill="{text_dim}">OBJECTIVE: Impact radius &amp; semantic change reasoning</text>
  <text x="16" y="78" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9.5" fill="{accent}">AST · Git co-change history · Datalog · proof trees</text>
</g>

<!-- ───────────────────────────────────────────────────────────── -->
<!-- QUADRANT 2: DARA v2 (South-West)                             -->
<!-- ───────────────────────────────────────────────────────────── -->
<g transform="translate(32, 164)">
  <rect width="424" height="92" rx="6" fill="{panel}" stroke="{border}" stroke-width="1"/>
  <rect x="0" y="0" width="3.5" height="92" rx="2" fill="{accent}"/>
  
  <text x="16" y="22" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" font-weight="700" letter-spacing="1" fill="{accent}">[02] SPECIMEN // CAUSAL REPAIR</text>
  <text x="16" y="42" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="14" font-weight="700" letter-spacing="0.5" fill="{text_main}">DARA v2</text>
  <text x="96" y="42" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" font-weight="500" fill="{text_muted}">AUTONOMOUS SOFTWARE REPAIR</text>
  
  <text x="16" y="62" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" fill="{text_dim}">OBJECTIVE: Root-cause localization &amp; sandbox-verified repair</text>
  <text x="16" y="78" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9.5" fill="{accent}">Multi-agent workflows · vector retrieval · Docker · Neo4j</text>
</g>

<!-- ───────────────────────────────────────────────────────────── -->
<!-- QUADRANT 3: SILENTBIAS (North-East)                          -->
<!-- ───────────────────────────────────────────────────────────── -->
<g transform="translate(504, 60)">
  <rect width="424" height="92" rx="6" fill="{panel}" stroke="{warn}" stroke-width="1"/>
  <rect x="0" y="0" width="3.5" height="92" rx="2" fill="{warn}"/>
  
  <text x="16" y="22" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" font-weight="700" letter-spacing="1" fill="{warn}">[03] SPECIMEN // LATENT AUDIT</text>
  <text x="16" y="42" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="14" font-weight="700" letter-spacing="0.5" fill="{text_main}">SILENTBIAS</text>
  <text x="126" y="42" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" font-weight="500" fill="{text_muted}">PROXY LEAKAGE &amp; FAIRNESS</text>
  
  <text x="16" y="62" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" fill="{text_dim}">OBJECTIVE: Uncovering latent bias &amp; proxy attribute leakage</text>
  <text x="16" y="78" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9.5" fill="{warn}">Shadow models · fairness metrics · representation probing</text>
</g>

<!-- ───────────────────────────────────────────────────────────── -->
<!-- QUADRANT 4: AGENT-NOIR (South-East)                          -->
<!-- ───────────────────────────────────────────────────────────── -->
<g transform="translate(504, 164)">
  <rect width="424" height="92" rx="6" fill="{panel}" stroke="{verify}" stroke-width="1"/>
  <rect x="0" y="0" width="3.5" height="92" rx="2" fill="{verify}"/>
  
  <text x="16" y="22" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" font-weight="700" letter-spacing="1" fill="{verify}">[04] SPECIMEN // GAME CONSENSUS</text>
  <text x="16" y="42" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="14" font-weight="700" letter-spacing="0.5" fill="{text_main}">AGENT-NOIR</text>
  <text x="136" y="42" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" font-weight="500" fill="{text_muted}">DECEPTION &amp; AGENT RELIABILITY</text>
  
  <text x="16" y="62" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" fill="{text_dim}">OBJECTIVE: Multi-agent interrogation &amp; deception resistance</text>
  <text x="16" y="78" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9.5" fill="{verify}">Deterministic simulation · audit provenance · verifier</text>
</g>

<!-- Footer Coordinates -->
<text x="32" y="{h-12}" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{text_dim}">TAXONOMY: CODE INTELLIGENCE · FAIRNESS · CAUSAL LOCALIZATION · CONSENSUS</text>
<text x="{w-32}" y="{h-12}" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" letter-spacing="1" fill="{accent}">ALL SPECIMENS ACTIVE</text>

</svg>"""
    return svg

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    with open("assets/systems-dark.svg", "w", encoding="utf-8") as f:
        f.write(generate_systems_svg(dark=True))
    with open("assets/systems-light.svg", "w", encoding="utf-8") as f:
        f.write(generate_systems_svg(dark=False))
    print("Generated assets/systems-dark.svg and assets/systems-light.svg successfully!")
