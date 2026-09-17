import os
from PIL import Image, ImageDraw, ImageFont

SCALE = 2

# -------------------------------------------------------------
# FONT LOADER
# -------------------------------------------------------------
try:
    font_name = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22 * SCALE)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 10 * SCALE)
    font_tag = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 9 * SCALE)
    font_tag_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 9 * SCALE)
    font_axiom = ImageFont.truetype("C:/Windows/Fonts/segoeuii.ttf", 11.5 * SCALE)
    font_quote = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 11 * SCALE)
    font_quote_cyan = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 11 * SCALE)
    font_cmd = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 10.5 * SCALE)
    font_detail = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 9 * SCALE)
    font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 11 * SCALE)
    font_mono_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 11 * SCALE)
    font_mono_small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 8.5 * SCALE)
    font_mono_small_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 9 * SCALE)
    font_node = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 9.5 * SCALE)
except Exception:
    font_name = ImageFont.load_default()
    font_sub = font_name
    font_tag = font_name
    font_tag_bold = font_name
    font_axiom = font_name
    font_quote = font_name
    font_quote_cyan = font_name
    font_cmd = font_name
    font_detail = font_name
    font_mono = font_name
    font_mono_bold = font_name
    font_mono_small = font_name
    font_mono_small_bold = font_name
    font_node = font_name

# -------------------------------------------------------------
# 1. "THE SARAN RESEARCH OS" HERO ANIMATION
# -------------------------------------------------------------
HERO_WIDTH = 900 * SCALE
HERO_HEIGHT = 276 * SCALE
HERO_RADIUS = 12 * SCALE

def render_hero_frame(dark=True, state_idx=0, cursor_on=True, scanline_offset=0):
    img = Image.new("RGBA", (HERO_WIDTH, HERO_HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if dark:
        bg = (8, 11, 18, 255)              # #080b12
        border = (30, 41, 59, 255)         # #1e293b
        bar_bg = (13, 19, 31, 255)         # #0d131f
        text_main = (241, 245, 249, 255)   # #f1f5f9
        text_muted = (148, 163, 184, 255)  # #94a3b8
        text_dim = (71, 85, 105, 255)      # #475569
        accent = (34, 211, 238, 255)       # #22d3ee cyan
        console_bg = (6, 8, 14, 255)       # #06080e
        console_border = (26, 36, 52, 255) # #1a2434
        scanline_color = (34, 211, 238, 12)
        pass_color = (52, 211, 153, 255)   # #34d399 emerald
        amber_color = (245, 158, 11, 255)  # #f59e0b amber
    else:
        bg = (247, 248, 251, 255)          # #f7f8fb
        border = (217, 222, 232, 255)      # #d9dee8
        bar_bg = (255, 255, 255, 255)      # #ffffff
        text_main = (15, 23, 42, 255)      # #0f172a
        text_muted = (100, 116, 139, 255)  # #64748b
        text_dim = (148, 163, 184, 255)    # #94a3b8
        accent = (8, 145, 178, 255)        # #0891b2 cyan
        console_bg = (255, 255, 255, 255)  # #ffffff
        console_border = (226, 232, 240, 255) # #e2e8f0
        scanline_color = (8, 145, 178, 8)
        pass_color = (16, 185, 129, 255)   # #10b981 emerald
        amber_color = (217, 119, 6, 255)   # #d97706 amber

    # Outer border container
    draw.rounded_rectangle(
        [(1, 1), (HERO_WIDTH - 2, HERO_HEIGHT - 2)],
        radius=HERO_RADIUS,
        fill=bg,
        outline=border,
        width=int(1.2 * SCALE)
    )

    # Top titlebar
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

    # Laboratory telemetry markers (Replacing generic macOS dots)
    dot_y = title_h // 2 + int(1 * SCALE)
    beacon_r = int(3 * SCALE)
    draw.ellipse([int(22 * SCALE) - beacon_r, dot_y - beacon_r, int(22 * SCALE) + beacon_r, dot_y + beacon_r], fill=accent)
    draw.text((int(32 * SCALE), dot_y - int(6 * SCALE)), "[SYS-01]", fill=accent, font=font_tag_bold)
    draw.text((int(78 * SCALE), dot_y - int(6 * SCALE)), "SARAN RESEARCH OS // EPISTEMIC TELEMETRY", fill=text_muted, font=font_tag_bold)
    draw.text((HERO_WIDTH - int(24 * SCALE), dot_y - int(6 * SCALE)), "MODE: EVIDENCE-FIRST", fill=accent, font=font_tag_bold, anchor="ra")

    # ---------------------------------------------------------
    # LEFT COLUMN: Identity + Statement + Philosophy
    # ---------------------------------------------------------
    left_x = int(26 * SCALE)
    start_y = title_h + int(16 * SCALE)

    # Small coordinate tag
    draw.text((left_x, start_y), "SPECIMEN // 0xSR1", fill=accent, font=font_tag_bold)

    # Name
    draw.text((left_x, start_y + int(14 * SCALE)), "U SARAN RAJ", fill=text_main, font=font_name)

    # Subtitles
    draw.text((left_x, start_y + int(44 * SCALE)), "AI/ML RESEARCHER", fill=accent, font=font_sub)
    draw.text((left_x, start_y + int(59 * SCALE)), "RESPONSIBLE AI · AGENT SYSTEMS · CODE INTELLIGENCE", fill=text_muted, font=font_mono_small)

    # Thin technical divider
    div_y1 = start_y + int(76 * SCALE)
    draw.line([(left_x, div_y1), (int(420 * SCALE), div_y1)], fill=border, width=int(1 * SCALE))

    # Centerpiece Statement: "I build AI systems that can be questioned."
    axiom_y = div_y1 + int(9 * SCALE)
    draw.text((left_x, axiom_y), '"I build AI systems that can be questioned."', fill=text_main, font=font_axiom)

    # Thin technical divider
    div_y2 = axiom_y + int(24 * SCALE)
    draw.line([(left_x, div_y2), (int(420 * SCALE), div_y2)], fill=border, width=int(1 * SCALE))

    # Philosophy Block
    phil_label_y = div_y2 + int(8 * SCALE)
    draw.text((left_x, phil_label_y), "AXIOMATIC PRINCIPLE //", fill=text_dim, font=font_mono_small_bold)

    quote_y = phil_label_y + int(14 * SCALE)
    draw.text((left_x, quote_y), "BUILD INTELLIGENCE.", fill=text_main, font=font_quote)
    draw.text((left_x, quote_y + int(16 * SCALE)), "EXPOSE ITS REASONING.", fill=text_main, font=font_quote)
    draw.text((left_x, quote_y + int(32 * SCALE)), "OWN ITS CONSEQUENCES.", fill=accent, font=font_quote_cyan)

    # Coordinate watermark
    draw.text((left_x, HERO_HEIGHT - int(16 * SCALE)), "LOC: 13.0827°N 80.2707°E · EPISTEMIC KERNEL", fill=text_dim, font=font_mono_small)

    # ---------------------------------------------------------
    # RIGHT COLUMN: Interrogation Console
    # ---------------------------------------------------------
    con_x0 = int(440 * SCALE)
    con_y0 = title_h + int(12 * SCALE)
    con_x1 = HERO_WIDTH - int(20 * SCALE)
    con_y1 = HERO_HEIGHT - int(14 * SCALE)

    draw.rounded_rectangle(
        [(con_x0, con_y0), (con_x1, con_y1)],
        radius=int(7 * SCALE),
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
        "PROBE // CODE INTELLIGENCE",
        "PROBE // ROBUSTNESS & OOD",
        "PROBE // PROXY AUDITING",
        "PROBE // REASONING PROOFS",
        "STATUS // EVIDENCE RECORDED"
    ]
    draw.text((con_x0 + int(12 * SCALE), con_y0 + int(6 * SCALE)), "EPISTEMIC PROBE MONITOR", fill=text_muted, font=font_tag_bold)
    draw.text((con_x1 - int(12 * SCALE), con_y0 + int(6 * SCALE)), state_titles[state_idx], fill=accent, font=font_tag_bold, anchor="ra")

    # Subtle scanline effect
    scan_y = con_y0 + con_head_h + int(8 * SCALE) + scanline_offset
    if scan_y < con_y1 - int(4 * SCALE):
        draw.rectangle(
            [(con_x0 + int(2 * SCALE), scan_y), (con_x1 - int(2 * SCALE), scan_y + int(3 * SCALE))],
            fill=scanline_color
        )

    commands = [
        ("PROBE 01 // CODE INTEL", "AST proof trees & impact radius", "[AUDITED]"),
        ("PROBE 02 // ROBUSTNESS", "perturbation stress & boundary decay", "[AUDITED]"),
        ("PROBE 03 // PROXY BIAS", "auditing latent demographic leakage", "[AUDITED]"),
        ("PROBE 04 // CONSENSUS", "game-theoretic proof · zero deceit", "[VERIFIED ✓]")
    ]

    base_cmd_y = con_y0 + con_head_h + int(10 * SCALE)
    line_step = int(37 * SCALE)
    cur = "◈" if cursor_on else " "

    for idx, (cmd_name, detail, tag) in enumerate(commands):
        cy = base_cmd_y + idx * line_step
        if idx < state_idx or state_idx == 4:
            draw.text((con_x0 + int(12 * SCALE), cy), f"{cmd_name}", fill=text_main, font=font_cmd)
            tag_col = pass_color if idx == 3 else text_muted
            draw.text((con_x1 - int(12 * SCALE), cy), tag, fill=tag_col, font=font_tag_bold, anchor="ra")
            draw.text((con_x0 + int(16 * SCALE), cy + int(16 * SCALE)), f"› {detail}", fill=text_muted, font=font_detail)
        elif idx == state_idx:
            draw.text((con_x0 + int(12 * SCALE), cy), f"{cmd_name} {cur}", fill=accent, font=font_cmd)
            draw.text((con_x1 - int(12 * SCALE), cy), "INTERROGATING...", fill=amber_color, font=font_tag_bold, anchor="ra")
            draw.text((con_x0 + int(16 * SCALE), cy + int(16 * SCALE)), f"› {detail}", fill=text_dim, font=font_detail)
        else:
            draw.text((con_x0 + int(12 * SCALE), cy), f"{cmd_name}", fill=text_dim, font=font_cmd)
            draw.text((con_x1 - int(12 * SCALE), cy), "[PENDING]", fill=text_dim, font=font_tag, anchor="ra")

    img_res = img.resize((HERO_WIDTH // SCALE, HERO_HEIGHT // SCALE), Image.Resampling.LANCZOS)
    return img_res.convert("P", palette=Image.Palette.ADAPTIVE, colors=64)

def generate_hero_gif(dark=True, output_path="assets/hero-dark.gif"):
    frames = []
    durations = []

    # 4 command phases + 1 hold state
    for state in range(4):
        # Step 1: command typing / start
        f1 = render_hero_frame(dark=dark, state_idx=state, cursor_on=True, scanline_offset=state * 25)
        frames.append(f1)
        durations.append(480)

        # Step 2: cursor off during execution
        f2 = render_hero_frame(dark=dark, state_idx=state, cursor_on=False, scanline_offset=state * 25 + 15)
        frames.append(f2)
        durations.append(380)

    # State 4: All evidence recorded hold frame
    f_hold1 = render_hero_frame(dark=dark, state_idx=4, cursor_on=True, scanline_offset=120)
    frames.append(f_hold1)
    durations.append(850)

    f_hold2 = render_hero_frame(dark=dark, state_idx=4, cursor_on=False, scanline_offset=140)
    frames.append(f_hold2)
    durations.append(650)

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


# -------------------------------------------------------------
# 2. HORIZONTAL FAILURE LAB RESEARCH PIPELINE ANIMATION
# -------------------------------------------------------------
PIPE_WIDTH = 900 * SCALE
PIPE_HEIGHT = 68 * SCALE
PIPE_RADIUS = 10 * SCALE

def render_pipeline_frame(dark=True, active_idx=0, pulse_sub=0):
    img = Image.new("RGBA", (PIPE_WIDTH, PIPE_HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if dark:
        bg = (8, 11, 18, 255)
        border = (30, 41, 59, 255)
        text_muted = (100, 116, 139, 255)
        arrow_color = (47, 60, 78, 255)
        arrow_lit = (34, 211, 238, 255)
        cyan_text = (34, 211, 238, 255)
        cyan_chip = (14, 58, 80, 255)
        cyan_border = (34, 211, 238, 255)
        # Warning node colors for FAILURE
        warn_text = (251, 146, 60, 255)
        warn_chip = (67, 36, 18, 255)
        warn_border = (251, 146, 60, 255)
        # Pass node colors for VERIFICATION
        pass_text = (52, 211, 153, 255)
        pass_chip = (6, 78, 59, 255)
        pass_border = (52, 211, 153, 255)
    else:
        bg = (247, 248, 251, 255)
        border = (217, 222, 232, 255)
        text_muted = (148, 163, 184, 255)
        arrow_color = (203, 213, 225, 255)
        arrow_lit = (8, 145, 178, 255)
        cyan_text = (8, 145, 178, 255)
        cyan_chip = (224, 242, 254, 255)
        cyan_border = (8, 145, 178, 255)
        # Warning node colors for FAILURE
        warn_text = (217, 119, 6, 255)
        warn_chip = (254, 243, 199, 255)
        warn_border = (217, 119, 6, 255)
        # Pass node colors for VERIFICATION
        pass_text = (16, 185, 129, 255)
        pass_chip = (209, 250, 229, 255)
        pass_border = (16, 185, 129, 255)

    # Outer container
    draw.rounded_rectangle(
        [(1, 1), (PIPE_WIDTH - 2, PIPE_HEIGHT - 2)],
        radius=PIPE_RADIUS,
        fill=bg,
        outline=border,
        width=int(1.2 * SCALE)
    )

    # Left prefix: dots + label
    dot_y = PIPE_HEIGHT // 2
    dot_r = int(3 * SCALE)
    dots = [
        (int(18 * SCALE), (255, 95, 87)),
        (int(28 * SCALE), (254, 188, 46)),
        (int(38 * SCALE), (40, 200, 64))
    ]
    for dx, color in dots:
        draw.ellipse([dx - dot_r, dot_y - dot_r, dx + dot_r, dot_y + dot_r], fill=color)

    title_color = (142, 154, 170) if dark else (100, 116, 139)
    draw.text((int(50 * SCALE), dot_y - int(6 * SCALE)), "FAILURE LAB", fill=title_color, font=font_mono_small_bold)

    # Dividing separator
    sep_x = int(140 * SCALE)
    draw.line([(sep_x, int(10 * SCALE)), (sep_x, PIPE_HEIGHT - int(10 * SCALE))], fill=border, width=int(1 * SCALE))

    # 6 pipeline nodes: DATA -> SHIFT -> FAILURE -> AUDIT -> EXPLANATION -> VERIFICATION
    nodes = ["DATA", "SHIFT", "FAILURE", "AUDIT", "EXPLANATION", "VERIFICATION"]
    start_x = int(152 * SCALE)
    available_width = PIPE_WIDTH - start_x - int(16 * SCALE)
    slot_width = available_width // len(nodes)

    is_hold = (active_idx == len(nodes))

    for i, node_name in enumerate(nodes):
        cx = start_x + i * slot_width + slot_width // 2
        cy = dot_y

        is_active = (i == active_idx)
        is_past = (i < active_idx)
        is_fail = (node_name == "FAILURE")
        is_verify = (node_name == "VERIFICATION")

        # Measure text
        bbox = font_node.getbbox(node_name)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]

        # Extra padding when active for subtle pulse feel
        extra_p = int(2 * SCALE) if (is_active and pulse_sub == 1) else 0
        chip_w = tw + int(14 * SCALE) + extra_p * 2
        chip_h = th + int(10 * SCALE) + extra_p * 2
        x0 = cx - chip_w // 2
        y0 = cy - chip_h // 2
        x1 = cx + chip_w // 2
        y1 = cy + chip_h // 2

        if is_active:
            if is_fail:
                fc, bc, tc = warn_chip, warn_border, warn_text
            elif is_verify:
                fc, bc, tc = pass_chip, pass_border, pass_text
            else:
                fc, bc, tc = cyan_chip, cyan_border, cyan_text

            draw.rounded_rectangle(
                [(x0, y0), (x1, y1)],
                radius=int(5 * SCALE),
                fill=fc,
                outline=bc,
                width=int(1.2 * SCALE)
            )
            draw.text((cx - tw // 2, cy - th // 2 - int(1 * SCALE)), node_name, fill=tc, font=font_node)
        elif is_hold:
            if is_fail:
                fc, bc, tc = warn_chip, warn_border, warn_text
            elif is_verify:
                fc, bc, tc = pass_chip, pass_border, pass_text
            else:
                fc, bc, tc = cyan_chip, cyan_border, cyan_text

            draw.rounded_rectangle(
                [(x0, y0), (x1, y1)],
                radius=int(5 * SCALE),
                fill=fc,
                outline=bc,
                width=int(1 * SCALE)
            )
            draw.text((cx - tw // 2, cy - th // 2 - int(1 * SCALE)), node_name, fill=tc, font=font_node)
        else:
            tc = text_muted
            draw.text((cx - tw // 2, cy - th // 2 - int(1 * SCALE)), node_name, fill=tc, font=font_node)

        # Arrow to next node
        if i < len(nodes) - 1:
            arr_x = start_x + (i + 1) * slot_width - int(8 * SCALE)
            arr_c = arrow_lit if (is_past or is_hold) else arrow_color
            draw.text((arr_x, cy - int(8 * SCALE)), "→", fill=arr_c, font=font_mono_bold)

    img_res = img.resize((PIPE_WIDTH // SCALE, PIPE_HEIGHT // SCALE), Image.Resampling.LANCZOS)
    return img_res.convert("P", palette=Image.Palette.ADAPTIVE, colors=64)

def generate_pipeline_gif(dark=True, output_path="assets/pipeline-dark.gif"):
    frames = []
    durations = []

    # 6 stages, each stage has 2 subtle pulse subframes (420ms + 380ms = 800ms per stage)
    for stage in range(6):
        # Pulse frame 1
        f1 = render_pipeline_frame(dark=dark, active_idx=stage, pulse_sub=0)
        frames.append(f1)
        durations.append(420)

        # Pulse frame 2 (subtle expand)
        f2 = render_pipeline_frame(dark=dark, active_idx=stage, pulse_sub=1)
        frames.append(f2)
        durations.append(380)

    # Stage 6: Hold state where the full path is illuminated
    f_hold = render_pipeline_frame(dark=dark, active_idx=6, pulse_sub=0)
    frames.append(f_hold)
    durations.append(1400)

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
