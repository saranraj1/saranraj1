import os
from PIL import Image, ImageDraw, ImageFont

SCALE = 2

# -------------------------------------------------------------
# FONT LOADER
# -------------------------------------------------------------
try:
    font_name = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 23 * SCALE)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 10 * SCALE)
    font_tag = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 9 * SCALE)
    font_tag_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 9 * SCALE)
    font_quote = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 13 * SCALE)
    font_cmd = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 11 * SCALE)
    font_cmd_normal = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 11 * SCALE)
    font_detail = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 9.5 * SCALE)
    font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13 * SCALE)
    font_mono_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 13 * SCALE)
    font_mono_small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 11 * SCALE)
except Exception:
    font_name = ImageFont.load_default()
    font_sub = font_name
    font_tag = font_name
    font_tag_bold = font_name
    font_quote = font_name
    font_cmd = font_name
    font_cmd_normal = font_name
    font_detail = font_name
    font_mono = font_name
    font_mono_bold = font_name
    font_mono_small = font_name

# -------------------------------------------------------------
# 1. COMPACT RESEARCH-TERMINAL HERO GIF
# -------------------------------------------------------------
HERO_WIDTH = 880 * SCALE
HERO_HEIGHT = 252 * SCALE
HERO_RADIUS = 12 * SCALE

def render_hero_frame(dark=True, state_idx=0, cursor_on=True, scanline_offset=0):
    img = Image.new("RGBA", (HERO_WIDTH, HERO_HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if dark:
        bg = (8, 11, 18, 255)            # #080b12
        border = (38, 50, 68, 255)       # #263244
        bar_bg = (14, 20, 32, 255)       # #0e1420
        text_main = (232, 237, 245, 255) # #e8edf5
        text_muted = (142, 154, 170, 255)# #8e9aaa
        text_dim = (75, 85, 99, 255)     # #4b5563
        accent = (34, 211, 238, 255)     # #22d3ee cyan
        console_bg = (6, 8, 14, 255)     # #06080e
        console_border = (30, 41, 59, 255) # #1e293b
        scanline_color = (34, 211, 238, 14)
        pass_color = (52, 211, 153, 255) # #34d399 green
    else:
        bg = (247, 248, 251, 255)        # #f7f8fb
        border = (217, 222, 232, 255)    # #d9dee8
        bar_bg = (255, 255, 255, 255)    # #ffffff
        text_main = (24, 32, 43, 255)     # #18202b
        text_muted = (100, 116, 139, 255)# #64748b
        text_dim = (148, 163, 184, 255)  # #94a3b8
        accent = (8, 145, 178, 255)      # #0891b2
        console_bg = (255, 255, 255, 255) # #ffffff
        console_border = (226, 232, 240, 255) # #e2e8f0
        scanline_color = (8, 145, 178, 10)
        pass_color = (16, 185, 129, 255) # #10b981 green

    # Outer container
    draw.rounded_rectangle(
        [(1, 1), (HERO_WIDTH - 2, HERO_HEIGHT - 2)],
        radius=HERO_RADIUS,
        fill=bg,
        outline=border,
        width=int(1.2 * SCALE)
    )

    # Top title bar
    title_h = int(32 * SCALE)
    draw.rounded_rectangle(
        [(int(2 * SCALE), int(2 * SCALE)), (HERO_WIDTH - int(3 * SCALE), title_h)],
        radius=HERO_RADIUS,
        fill=bar_bg
    )
    draw.line(
        [(int(2 * SCALE), title_h), (HERO_WIDTH - int(3 * SCALE), title_h)],
        fill=border,
        width=int(1 * SCALE)
    )

    # Window dots
    dot_y = title_h // 2 + int(1 * SCALE)
    dot_r = int(3.5 * SCALE)
    dots = [
        (int(22 * SCALE), (255, 95, 87)),
        (int(34 * SCALE), (254, 188, 46)),
        (int(46 * SCALE), (40, 200, 64))
    ]
    for dx, color in dots:
        draw.ellipse([dx - dot_r, dot_y - dot_r, dx + dot_r, dot_y + dot_r], fill=color)

    draw.text((int(58 * SCALE), dot_y - int(6 * SCALE)), "saran@ai-lab: ~/research-terminal", fill=text_muted, font=font_tag_bold)
    draw.text((HERO_WIDTH - int(24 * SCALE), dot_y - int(6 * SCALE)), "AI RESEARCH LAB // VERIFIABLE", fill=accent, font=font_tag_bold, anchor="ra")

    # Left Panel: Identity & Philosophy
    left_x = int(26 * SCALE)
    start_y = title_h + int(18 * SCALE)

    draw.text((left_x, start_y), "$ whoami", fill=accent, font=font_tag_bold)
    draw.text((left_x, start_y + int(16 * SCALE)), "U SARAN RAJ", fill=text_main, font=font_name)
    draw.text((left_x, start_y + int(46 * SCALE)), "AI/ML RESEARCHER · RESPONSIBLE AI · AGENT SYSTEMS", fill=accent, font=font_sub)

    div_y = start_y + int(65 * SCALE)
    draw.line([(left_x, div_y), (int(410 * SCALE), div_y)], fill=border, width=int(1 * SCALE))

    phil_y = div_y + int(12 * SCALE)
    draw.text((left_x, phil_y), "RESEARCH PRINCIPLE //", fill=text_muted, font=font_tag_bold)

    quote_y = phil_y + int(16 * SCALE)
    draw.text((left_x, quote_y), "BUILD INTELLIGENCE.", fill=text_main, font=font_quote)
    draw.text((left_x, quote_y + int(19 * SCALE)), "EXPOSE ITS REASONING.", fill=text_main, font=font_quote)
    draw.text((left_x, quote_y + int(38 * SCALE)), "OWN ITS CONSEQUENCES.", fill=accent, font=font_quote)

    # Right Panel: Living Terminal Console
    con_x0 = int(430 * SCALE)
    con_y0 = title_h + int(12 * SCALE)
    con_x1 = HERO_WIDTH - int(20 * SCALE)
    con_y1 = HERO_HEIGHT - int(14 * SCALE)

    draw.rounded_rectangle(
        [(con_x0, con_y0), (con_x1, con_y1)],
        radius=int(8 * SCALE),
        fill=console_bg,
        outline=console_border,
        width=int(1 * SCALE)
    )

    con_head_h = int(24 * SCALE)
    draw.line(
        [(con_x0, con_y0 + con_head_h), (con_x1, con_y0 + con_head_h)],
        fill=console_border,
        width=int(1 * SCALE)
    )
    state_titles = [
        "PHASE 01 // CODE INTELLIGENCE",
        "PHASE 02 // ROBUSTNESS & OOD",
        "PHASE 03 // FAIRNESS & PROXY AUDIT",
        "PHASE 04 // REASONING VERIFICATION",
        "STATUS // ALL PROOFS ESTABLISHED"
    ]
    draw.text((con_x0 + int(12 * SCALE), con_y0 + int(6 * SCALE)), "EXPERIMENTAL WORKSPACE", fill=text_muted, font=font_tag_bold)
    draw.text((con_x1 - int(12 * SCALE), con_y0 + int(6 * SCALE)), state_titles[state_idx], fill=accent, font=font_tag_bold, anchor="ra")

    scan_y = con_y0 + con_head_h + int(10 * SCALE) + scanline_offset
    if scan_y < con_y1 - int(4 * SCALE):
        draw.rectangle(
            [(con_x0 + int(2 * SCALE), scan_y), (con_x1 - int(2 * SCALE), scan_y + int(3 * SCALE))],
            fill=scanline_color
        )

    commands = [
        ("./build", "synthesizing AST proof trees & impact radius", "[OK]"),
        ("./test", "reproducing distribution shifts & boundary decay", "[OK]"),
        ("./audit", "auditing hidden proxies & algorithmic bias", "[OK]"),
        ("./verify", "formal reasoning checked · zero hallucination", "[VERIFIED ✓]")
    ]

    base_cmd_y = con_y0 + con_head_h + int(12 * SCALE)
    line_step = int(36 * SCALE)
    cur = "█" if cursor_on else " "

    for idx, (cmd_name, detail, tag) in enumerate(commands):
        cy = base_cmd_y + idx * line_step
        if idx < state_idx or state_idx == 4:
            draw.text((con_x0 + int(12 * SCALE), cy), f"$ {cmd_name}", fill=text_main, font=font_cmd)
            draw.text((con_x1 - int(12 * SCALE), cy), tag, fill=pass_color, font=font_tag_bold, anchor="ra")
            draw.text((con_x0 + int(16 * SCALE), cy + int(16 * SCALE)), f"› {detail}", fill=text_muted, font=font_detail)
        elif idx == state_idx:
            draw.text((con_x0 + int(12 * SCALE), cy), f"$ {cmd_name} {cur}", fill=accent, font=font_cmd)
            draw.text((con_x1 - int(12 * SCALE), cy), "RUNNING...", fill=accent, font=font_tag_bold, anchor="ra")
            draw.text((con_x0 + int(16 * SCALE), cy + int(16 * SCALE)), f"› {detail}", fill=accent, font=font_detail)
        else:
            draw.text((con_x0 + int(12 * SCALE), cy), f"$ {cmd_name}", fill=text_dim, font=font_cmd_normal)
            draw.text((con_x1 - int(12 * SCALE), cy), "PENDING", fill=text_dim, font=font_tag, anchor="ra")
            draw.text((con_x0 + int(16 * SCALE), cy + int(16 * SCALE)), f"› {detail}", fill=text_dim, font=font_detail)

    img_res = img.resize((HERO_WIDTH // SCALE, HERO_HEIGHT // SCALE), Image.Resampling.LANCZOS)
    return img_res.convert("P", palette=Image.Palette.ADAPTIVE, colors=64)

def generate_hero_gif(dark=True, output_path="assets/hero-dark.gif"):
    frames = []
    durations = []
    scanlines = [int(10 * SCALE), int(45 * SCALE), int(80 * SCALE), int(120 * SCALE)]

    for state in range(4):
        f1 = render_hero_frame(dark=dark, state_idx=state, cursor_on=True, scanline_offset=scanlines[0])
        frames.append(f1)
        durations.append(450)

        f2 = render_hero_frame(dark=dark, state_idx=state, cursor_on=False, scanline_offset=scanlines[1])
        frames.append(f2)
        durations.append(350)

        f3 = render_hero_frame(dark=dark, state_idx=state, cursor_on=True, scanline_offset=scanlines[2])
        frames.append(f3)
        durations.append(400)

    f_hold1 = render_hero_frame(dark=dark, state_idx=4, cursor_on=True, scanline_offset=scanlines[3])
    frames.append(f_hold1)
    durations.append(800)

    f_hold2 = render_hero_frame(dark=dark, state_idx=4, cursor_on=False, scanline_offset=scanlines[0])
    frames.append(f_hold2)
    durations.append(700)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        optimize=True,
        disposal=2
    )
    print(f"Generated {output_path} ({os.path.getsize(output_path) // 1024} KB)")

# -----------------------------------------------------------------------------------
# 2. RESEARCH FAILURE PIPELINE GIF (DATA -> SHIFT -> FAIL -> AUDIT -> EXPLAIN -> VERIFY)
# -----------------------------------------------------------------------------------
PIPE_WIDTH = 860 * SCALE
PIPE_HEIGHT = 56 * SCALE
PIPE_RADIUS = 10 * SCALE

def generate_pipeline_gif(dark=True, output_path="assets/pipeline-dark.gif"):
    nodes = ["DATA", "SHIFT", "FAIL", "AUDIT", "EXPLAIN", "VERIFY"]
    frames = []
    durations = []

    if dark:
        bg_color = (8, 11, 18, 255)
        border_color = (38, 50, 68, 255)
        text_muted = (100, 116, 139)
        text_active = (34, 211, 238)
        chip_active = (14, 58, 80)
        border_active = (34, 211, 238)
        arrow_color = (60, 75, 96)
        arrow_active = (34, 211, 238)
        warning_color = (251, 146, 60)
        warning_chip = (67, 36, 18)
    else:
        bg_color = (247, 248, 251, 255)
        border_color = (217, 222, 232, 255)
        text_muted = (148, 163, 184)
        text_active = (8, 145, 178)
        chip_active = (224, 242, 254)
        border_active = (8, 145, 178)
        arrow_color = (203, 213, 225)
        arrow_active = (8, 145, 178)
        warning_color = (217, 119, 6)
        warning_chip = (254, 243, 199)

    start_x = int(220 * SCALE)
    available_width = PIPE_WIDTH - start_x - int(25 * SCALE)
    node_width = available_width // len(nodes)

    def base_pipe_frame(title):
        img = Image.new("RGBA", (PIPE_WIDTH, PIPE_HEIGHT), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.rounded_rectangle(
            [(1, 1), (PIPE_WIDTH - 2, PIPE_HEIGHT - 2)],
            radius=PIPE_RADIUS,
            fill=bg_color,
            outline=border_color,
            width=int(1.2 * SCALE)
        )
        dot_y = PIPE_HEIGHT // 2
        dot_r = int(3.5 * SCALE)
        dots = [
            (int(24 * SCALE), (255, 95, 87)),
            (int(36 * SCALE), (254, 188, 46)),
            (int(48 * SCALE), (40, 200, 64))
        ]
        for dx, color in dots:
            draw.ellipse([dx - dot_r, dot_y - dot_r, dx + dot_r, dot_y + dot_r], fill=color)
        title_color = (142, 154, 170) if dark else (100, 116, 139)
        draw.text((int(62 * SCALE), dot_y - int(7 * SCALE)), title, fill=title_color, font=font_mono_small)
        return img, draw

    for active_idx in range(len(nodes)):
        curr_node = nodes[active_idx]
        title = f"research.pipeline: [{curr_node}]"
        img, draw = base_pipe_frame(title)

        for i, node_name in enumerate(nodes):
            cx = start_x + i * node_width + node_width // 2
            cy = PIPE_HEIGHT // 2
            is_active = (i == active_idx)
            is_fail = (node_name == "FAIL")

            bbox = font_mono_bold.getbbox(node_name)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            chip_w = tw + int(14 * SCALE)
            chip_h = th + int(10 * SCALE)
            x0 = cx - chip_w // 2
            y0 = cy - chip_h // 2
            x1 = cx + chip_w // 2
            y1 = cy + chip_h // 2

            if is_active:
                fill_c = warning_chip if is_fail else chip_active
                border_c = warning_color if is_fail else border_active
                text_c = warning_color if is_fail else text_active
                draw.rounded_rectangle([(x0, y0), (x1, y1)], radius=int(5 * SCALE), fill=fill_c, outline=border_c, width=int(1.2 * SCALE))
                draw.text((x0 + int(7 * SCALE), y0 + int(3 * SCALE)), node_name, fill=text_c, font=font_mono_bold)
            else:
                draw.text((x0 + int(7 * SCALE), y0 + int(3 * SCALE)), node_name, fill=text_muted, font=font_mono)

            if i < len(nodes) - 1:
                arr_x = start_x + (i + 1) * node_width - int(8 * SCALE)
                arr_col = arrow_active if i < active_idx else arrow_color
                draw.text((arr_x, cy - int(8 * SCALE)), "→", fill=arr_col, font=font_mono_bold)

        img_res = img.resize((PIPE_WIDTH // SCALE, PIPE_HEIGHT // SCALE), Image.Resampling.LANCZOS)
        frames.append(img_res.convert("P", palette=Image.Palette.ADAPTIVE, colors=64))
        durations.append(850)

    # Final hold phase
    img, draw = base_pipe_frame("research.pipeline: [PROOF ESTABLISHED ✓]")
    for i, node_name in enumerate(nodes):
        cx = start_x + i * node_width + node_width // 2
        cy = PIPE_HEIGHT // 2
        is_fail = (node_name == "FAIL")

        bbox = font_mono_bold.getbbox(node_name)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        chip_w = tw + int(14 * SCALE)
        chip_h = th + int(10 * SCALE)
        x0 = cx - chip_w // 2
        y0 = cy - chip_h // 2
        x1 = cx + chip_w // 2
        y1 = cy + chip_h // 2

        fill_c = warning_chip if is_fail else chip_active
        border_c = warning_color if is_fail else border_active
        text_c = warning_color if is_fail else text_active

        draw.rounded_rectangle([(x0, y0), (x1, y1)], radius=int(5 * SCALE), fill=fill_c, outline=border_c, width=int(1 * SCALE))
        draw.text((x0 + int(7 * SCALE), y0 + int(3 * SCALE)), node_name, fill=text_c, font=font_mono_bold)

        if i < len(nodes) - 1:
            arr_x = start_x + (i + 1) * node_width - int(8 * SCALE)
            draw.text((arr_x, cy - int(8 * SCALE)), "→", fill=arrow_active, font=font_mono_bold)

    img_res = img.resize((PIPE_WIDTH // SCALE, PIPE_HEIGHT // SCALE), Image.Resampling.LANCZOS)
    frames.append(img_res.convert("P", palette=Image.Palette.ADAPTIVE, colors=64))
    durations.append(1300)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        optimize=True,
        disposal=2
    )
    print(f"Generated {output_path} ({os.path.getsize(output_path) // 1024} KB)")

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    generate_hero_gif(dark=True, output_path="assets/hero-dark.gif")
    generate_hero_gif(dark=False, output_path="assets/hero-light.gif")
    generate_pipeline_gif(dark=True, output_path="assets/pipeline-dark.gif")
    generate_pipeline_gif(dark=False, output_path="assets/pipeline-light.gif")
    print("All profile animations generated successfully!")
