import os

def generate_systems_svg(dark=True):
    bg = "#080b12" if dark else "#f7f8fb"
    panel = "#0d131f" if dark else "#ffffff"
    border = "#1e293b" if dark else "#d9dee8"
    line_subtle = "#192438" if dark else "#e2e8f0"
    accent = "#22d3ee" if dark else "#0891b2"
    warn = "#f59e0b" if dark else "#d97706"
    verify = "#34d399" if dark else "#059669"
    
    text_main = "#f1f5f9" if dark else "#0f172a"
    text_muted = "#94a3b8" if dark else "#64748b"
    text_dim = "#475569" if dark else "#94a3b8"

    w = 960
    h = 310

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Systems: Four core research specimens — TITAN, DARA v2, SILENTBIAS, and AGENT-NOIR">
<title>Systems — Editorial Research Specimens</title>

<!-- Outer Container -->
<rect width="{w}" height="{h}" rx="10" fill="{bg}"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="10" fill="none" stroke="{border}" stroke-width="1.2"/>

<!-- Top Ledger Header -->
<text x="32" y="30" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" font-weight="700" letter-spacing="1.5" fill="{accent}">03 // RESEARCH SPECIMENS</text>
<text x="480" y="30" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" letter-spacing="1" fill="{text_dim}">LAB // INDEPENDENT RESEARCH · SPECIMEN // SR-01</text>
<text x="{w-32}" y="30" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" font-weight="600" letter-spacing="1" fill="{text_muted}">MODE: EVIDENCE-FIRST</text>

<line x1="24" y1="44" x2="{w-24}" y2="44" stroke="{border}" stroke-width="1"/>

<!-- Asymmetric Horizontal Construction Hairline -->
<line x1="24" y1="168" x2="{w-24}" y2="168" stroke="{border}" stroke-width="1" stroke-dasharray="3 4"/>

<!-- ───────────────────────────────────────────────────────────── -->
<!-- SPECIMEN [01]: TITAN (North-West, Asymmetric Span: 440px)     -->
<!-- ───────────────────────────────────────────────────────────── -->
<g transform="translate(32, 56)">
  <!-- Architectural Specimen Bracket -->
  <path d="M 12 0 L 0 0 L 0 98 L 12 98" fill="none" stroke="{accent}" stroke-width="1.5"/>
  <rect x="1" y="0" width="435" height="98" fill="{panel}" fill-opacity="0.5"/>
  
  <text x="20" y="24" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="14" font-weight="800" fill="{accent}">[01]</text>
  <text x="62" y="24" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="15" font-weight="800" letter-spacing="0.5" fill="{text_main}">TITAN</text>
  <text x="424" y="22" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" font-weight="600" letter-spacing="1" fill="{text_dim}">SPECIMEN // SYNTAX</text>
  
  <text x="20" y="44" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" font-weight="600" letter-spacing="0.8" fill="{text_muted}">CHANGE-AWARE CODE INTELLIGENCE</text>
  <text x="20" y="64" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9.5" fill="{text_dim}">OBJECTIVE: Impact radius &amp; semantic change reasoning</text>
  <text x="20" y="82" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{accent}">› AST · Git co-change history · Datalog · proof trees</text>
  
  <line x1="20" y1="94" x2="424" y2="94" stroke="{line_subtle}" stroke-width="0.75" stroke-dasharray="2 3"/>
</g>

<!-- ───────────────────────────────────────────────────────────── -->
<!-- SPECIMEN [03]: SILENTBIAS (North-East, Asymmetric Span: 420px)-->
<!-- ───────────────────────────────────────────────────────────── -->
<g transform="translate(504, 56)">
  <!-- Architectural Specimen Bracket -->
  <path d="M 12 0 L 0 0 L 0 98 L 12 98" fill="none" stroke="{warn}" stroke-width="1.5"/>
  <rect x="1" y="0" width="423" height="98" fill="{panel}" fill-opacity="0.5"/>
  
  <text x="20" y="24" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="14" font-weight="800" fill="{warn}">[03]</text>
  <text x="62" y="24" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="15" font-weight="800" letter-spacing="0.5" fill="{text_main}">SILENTBIAS</text>
  <text x="412" y="22" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" font-weight="600" letter-spacing="1" fill="{warn}">SPECIMEN // LATENT</text>
  
  <text x="20" y="44" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" font-weight="600" letter-spacing="0.8" fill="{text_muted}">PROXY LEAKAGE &amp; FAIRNESS</text>
  <text x="20" y="64" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9.5" fill="{text_dim}">OBJECTIVE: Uncovering latent bias &amp; proxy attribute leakage</text>
  <text x="20" y="82" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{warn}">› Shadow models · fairness metrics · representation probing</text>
  
  <line x1="20" y1="94" x2="412" y2="94" stroke="{line_subtle}" stroke-width="0.75" stroke-dasharray="2 3"/>
</g>

<!-- ───────────────────────────────────────────────────────────── -->
<!-- SPECIMEN [02]: DARA v2 (South-West, Asymmetric Span: 420px)   -->
<!-- ───────────────────────────────────────────────────────────── -->
<g transform="translate(32, 180)">
  <!-- Architectural Specimen Bracket -->
  <path d="M 12 0 L 0 0 L 0 98 L 12 98" fill="none" stroke="{accent}" stroke-width="1.5"/>
  <rect x="1" y="0" width="415" height="98" fill="{panel}" fill-opacity="0.5"/>
  
  <text x="20" y="24" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="14" font-weight="800" fill="{accent}">[02]</text>
  <text x="62" y="24" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="15" font-weight="800" letter-spacing="0.5" fill="{text_main}">DARA v2</text>
  <text x="404" y="22" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" font-weight="600" letter-spacing="1" fill="{text_dim}">SPECIMEN // REPAIR</text>
  
  <text x="20" y="44" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" font-weight="600" letter-spacing="0.8" fill="{text_muted}">AUTONOMOUS SOFTWARE REPAIR</text>
  <text x="20" y="64" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9.5" fill="{text_dim}">OBJECTIVE: Root-cause localization &amp; sandbox-verified repair</text>
  <text x="20" y="82" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{accent}">› Multi-agent workflows · vector retrieval · Docker · Neo4j</text>
  
  <line x1="20" y1="94" x2="404" y2="94" stroke="{line_subtle}" stroke-width="0.75" stroke-dasharray="2 3"/>
</g>

<!-- ───────────────────────────────────────────────────────────── -->
<!-- SPECIMEN [04]: AGENT-NOIR (South-East, Asymmetric Span: 440px)-->
<!-- ───────────────────────────────────────────────────────────── -->
<g transform="translate(484, 180)">
  <!-- Architectural Specimen Bracket -->
  <path d="M 12 0 L 0 0 L 0 98 L 12 98" fill="none" stroke="{verify}" stroke-width="1.5"/>
  <rect x="1" y="0" width="443" height="98" fill="{panel}" fill-opacity="0.5"/>
  
  <text x="20" y="24" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="14" font-weight="800" fill="{verify}">[04]</text>
  <text x="62" y="24" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="15" font-weight="800" letter-spacing="0.5" fill="{text_main}">AGENT-NOIR</text>
  <text x="432" y="22" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" font-weight="600" letter-spacing="1" fill="{verify}">SPECIMEN // PROOF</text>
  
  <text x="20" y="44" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" font-weight="600" letter-spacing="0.8" fill="{text_muted}">DECEPTION &amp; AGENT RELIABILITY</text>
  <text x="20" y="64" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9.5" fill="{text_dim}">OBJECTIVE: Multi-agent interrogation &amp; deception resistance</text>
  <text x="20" y="82" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="{verify}">› Deterministic simulation · audit provenance · verifier</text>
  
  <line x1="20" y1="94" x2="432" y2="94" stroke="{line_subtle}" stroke-width="0.75" stroke-dasharray="2 3"/>
</g>

<!-- Footer Ledger -->
<text x="32" y="{h-12}" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" fill="{text_dim}">INDEX: [01] CODE INTELLIGENCE · [02] REPAIR · [03] FAIRNESS · [04] AGENT PROOFS</text>
<text x="{w-32}" y="{h-12}" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="8.5" letter-spacing="1" fill="{accent}">ALL SPECIMENS VERIFIABLE</text>

</svg>"""
    return svg

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    with open("assets/systems-dark.svg", "w", encoding="utf-8") as f:
        f.write(generate_systems_svg(dark=True))
    with open("assets/systems-light.svg", "w", encoding="utf-8") as f:
        f.write(generate_systems_svg(dark=False))
    print("Generated assets/systems-dark.svg and assets/systems-light.svg successfully!")
