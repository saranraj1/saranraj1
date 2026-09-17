import os
from PIL import Image, ImageDraw, ImageFont

# Set high-resolution scale for crisp 2x supersampling
SCALE = 2
WIDTH = 860 * SCALE
HEIGHT = 56 * SCALE
CORNER_RADIUS = 10 * SCALE

# Load fonts
try:
    font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13 * SCALE)
    font_mono_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 13 * SCALE)
    font_mono_small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 11 * SCALE)
    font_mono_small_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 11 * SCALE)
    font_sans = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13 * SCALE)
    font_sans_bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 13 * SCALE)
except Exception:
    font_mono = ImageFont.load_default()
    font_mono_bold = font_mono
    font_mono_small = font_mono
    font_mono_small_bold = font_mono
    font_sans = font_mono
    font_sans_bold = font_mono

def create_base_frame(dark=True, title=""):
    img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Colors
    if dark:
        bg_color = (8, 11, 18, 255)       # #080b12
        border_color = (38, 50, 68, 255)   # #263244
        panel_bg = (14, 20, 32, 255)      # #0e1420
    else:
        bg_color = (247, 248, 251, 255)   # #f7f8fb
        border_color = (217, 222, 232, 255) # #d9dee8
        panel_bg = (255, 255, 255, 255)   # #ffffff

    # Outer rounded box
    draw.rounded_rectangle(
        [(1, 1), (WIDTH - 2, HEIGHT - 2)],
        radius=CORNER_RADIUS,
        fill=bg_color,
        outline=border_color,
        width=int(1.2 * SCALE)
    )

    # Terminal window dots on the left
    dot_y = HEIGHT // 2
    dot_r = int(3.5 * SCALE)
    dots = [
        (int(24 * SCALE), (255, 95, 87)),   # #ff5f57 red
        (int(36 * SCALE), (254, 188, 46)),  # #febc2e yellow
        (int(48 * SCALE), (40, 200, 64))    # #28c840 green
    ]
    for dx, color in dots:
        draw.ellipse([dx - dot_r, dot_y - dot_r, dx + dot_r, dot_y + dot_r], fill=color)

    # Title / prompt label
    if title:
        title_color = (142, 154, 170) if dark else (100, 116, 139)
        draw.text((int(62 * SCALE), dot_y - int(7 * SCALE)), title, fill=title_color, font=font_mono_small)

    return img, draw

# -------------------------------------------------------------
# ANIMATION 1: RESEARCH LOOP (BUILD -> TEST -> AUDIT -> VERIFY)
# -------------------------------------------------------------
def generate_loop_gif(dark=True, output_path="assets/loop-dark.gif"):
    steps = ["BUILD", "TEST", "AUDIT", "VERIFY"]
    frames = []
    durations = []

    # Palette
    if dark:
        text_muted = (100, 116, 139)     # #64748b
        text_active = (34, 211, 238)     # #22d3ee cyan
        chip_active = (14, 58, 80)       # #0e3a50
        border_active = (34, 211, 238)
        arrow_color = (60, 75, 96)
        arrow_active = (34, 211, 238)
    else:
        text_muted = (148, 163, 184)    # #94a3b8
        text_active = (8, 145, 178)     # #0891b2
        chip_active = (224, 242, 254)   # #e0f2fe
        border_active = (8, 145, 178)
        arrow_color = (203, 213, 225)
        arrow_active = (8, 145, 178)

    # Step layout coordinates
    # We leave x=230px for title: "saran@ai-lab:~$ ./loop"
    start_x = int(240 * SCALE)
    available_width = WIDTH - start_x - int(30 * SCALE)
    step_width = available_width // 4

    # We generate 4 main active phases + 1 complete phase
    # Each phase has a couple of subtle subframes for smoothness
    for active_idx in range(len(steps)):
        # Active step phase
        img, draw = create_base_frame(dark=dark, title="saran@ai-lab:~$ ./loop")

        for i, step_name in enumerate(steps):
            cx = start_x + i * step_width + step_width // 2
            cy = HEIGHT // 2

            is_active = (i == active_idx)
            is_done = (i < active_idx)

            # Draw step chip
            label = f"0{i+1} {step_name}"
            bbox = font_mono_bold.getbbox(label)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]

            chip_w = tw + int(18 * SCALE)
            chip_h = th + int(12 * SCALE)
            x0 = cx - chip_w // 2
            y0 = cy - chip_h // 2
            x1 = cx + chip_w // 2
            y1 = cy + chip_h // 2

            if is_active:
                # Active chip with highlighted background & border
                draw.rounded_rectangle(
                    [(x0, y0), (x1, y1)],
                    radius=int(6 * SCALE),
                    fill=chip_active,
                    outline=border_active,
                    width=int(1.2 * SCALE)
                )
                draw.text((x0 + int(9 * SCALE), y0 + int(4 * SCALE)), label, fill=text_active, font=font_mono_bold)
            else:
                col = text_muted
                draw.rounded_rectangle(
                    [(x0, y0), (x1, y1)],
                    radius=int(6 * SCALE),
                    fill=None,
                    outline=None
                )
                draw.text((x0 + int(9 * SCALE), y0 + int(4 * SCALE)), label, fill=col, font=font_mono)

            # Arrow to next step
            if i < len(steps) - 1:
                arr_x = start_x + (i + 1) * step_width - int(10 * SCALE)
                arr_col = arrow_active if i < active_idx else arrow_color
                draw.text((arr_x, cy - int(8 * SCALE)), "→", fill=arr_col, font=font_mono_bold)

        # Downsample 2x with LANCZOS
        img_res = img.resize((WIDTH // SCALE, HEIGHT // SCALE), Image.Resampling.LANCZOS)
        frames.append(img_res.convert("P", palette=Image.Palette.ADAPTIVE, colors=64))
        durations.append(900)  # 900ms per step

    # Final summary phase (all verified pulse)
    img, draw = create_base_frame(dark=dark, title="saran@ai-lab:~$ [VERIFIED ✓]")
    for i, step_name in enumerate(steps):
        cx = start_x + i * step_width + step_width // 2
        cy = HEIGHT // 2
        label = f"0{i+1} {step_name}"
        bbox = font_mono_bold.getbbox(label)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        chip_w = tw + int(18 * SCALE)
        chip_h = th + int(12 * SCALE)
        x0 = cx - chip_w // 2
        y0 = cy - chip_h // 2
        x1 = cx + chip_w // 2
        y1 = cy + chip_h // 2

        # Draw verified state for all
        draw.rounded_rectangle(
            [(x0, y0), (x1, y1)],
            radius=int(6 * SCALE),
            fill=chip_active,
            outline=border_active,
            width=int(1 * SCALE)
        )
        draw.text((x0 + int(9 * SCALE), y0 + int(4 * SCALE)), label, fill=text_active, font=font_mono_bold)

        if i < len(steps) - 1:
            arr_x = start_x + (i + 1) * step_width - int(10 * SCALE)
            draw.text((arr_x, cy - int(8 * SCALE)), "→", fill=arrow_active, font=font_mono_bold)

    img_res = img.resize((WIDTH // SCALE, HEIGHT // SCALE), Image.Resampling.LANCZOS)
    frames.append(img_res.convert("P", palette=Image.Palette.ADAPTIVE, colors=64))
    durations.append(1200)  # 1.2s pause on verified state

    # Save animated GIF
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
# ANIMATION 2: RESEARCH PIPELINE (DATA -> SHIFT -> FAIL -> AUDIT -> EXPLAIN -> VERIFY)
# -----------------------------------------------------------------------------------
def generate_pipeline_gif(dark=True, output_path="assets/pipeline-dark.gif"):
    nodes = ["DATA", "SHIFT", "FAIL", "AUDIT", "EXPLAIN", "VERIFY"]
    frames = []
    durations = []

    # Palette
    if dark:
        text_muted = (100, 116, 139)       # #64748b
        text_active = (34, 211, 238)       # #22d3ee
        chip_active = (14, 58, 80)         # #0e3a50
        border_active = (34, 211, 238)
        arrow_color = (60, 75, 96)
        arrow_active = (34, 211, 238)
        warning_color = (251, 146, 60)     # #fb923c orange for FAIL
        warning_chip = (67, 36, 18)
    else:
        text_muted = (148, 163, 184)      # #94a3b8
        text_active = (8, 145, 178)       # #0891b2
        chip_active = (224, 242, 254)     # #e0f2fe
        border_active = (8, 145, 178)
        arrow_color = (203, 213, 225)
        arrow_active = (8, 145, 178)
        warning_color = (217, 119, 6)     # #d97706
        warning_chip = (254, 243, 199)

    start_x = int(220 * SCALE)
    available_width = WIDTH - start_x - int(25 * SCALE)
    node_width = available_width // len(nodes)

    # 6 node phases
    for active_idx in range(len(nodes)):
        curr_node = nodes[active_idx]
        title = f"research.pipeline: [{curr_node}]"
        img, draw = create_base_frame(dark=dark, title=title)

        for i, node_name in enumerate(nodes):
            cx = start_x + i * node_width + node_width // 2
            cy = HEIGHT // 2

            is_active = (i == active_idx)
            is_fail_node = (node_name == "FAIL")

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
                fill_c = warning_chip if is_fail_node else chip_active
                border_c = warning_color if is_fail_node else border_active
                text_c = warning_color if is_fail_node else text_active
                draw.rounded_rectangle(
                    [(x0, y0), (x1, y1)],
                    radius=int(5 * SCALE),
                    fill=fill_c,
                    outline=border_c,
                    width=int(1.2 * SCALE)
                )
                draw.text((x0 + int(7 * SCALE), y0 + int(3 * SCALE)), node_name, fill=text_c, font=font_mono_bold)
            else:
                draw.text((x0 + int(7 * SCALE), y0 + int(3 * SCALE)), node_name, fill=text_muted, font=font_mono)

            # Arrow to next node
            if i < len(nodes) - 1:
                arr_x = start_x + (i + 1) * node_width - int(8 * SCALE)
                arr_col = arrow_active if i < active_idx else arrow_color
                draw.text((arr_x, cy - int(8 * SCALE)), "→", fill=arr_col, font=font_mono_bold)

        img_res = img.resize((WIDTH // SCALE, HEIGHT // SCALE), Image.Resampling.LANCZOS)
        frames.append(img_res.convert("P", palette=Image.Palette.ADAPTIVE, colors=64))
        durations.append(850)

    # Summary phase (proof tree established)
    img, draw = create_base_frame(dark=dark, title="research.pipeline: [PROOF ESTABLISHED ✓]")
    for i, node_name in enumerate(nodes):
        cx = start_x + i * node_width + node_width // 2
        cy = HEIGHT // 2
        is_fail_node = (node_name == "FAIL")

        bbox = font_mono_bold.getbbox(node_name)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        chip_w = tw + int(14 * SCALE)
        chip_h = th + int(10 * SCALE)
        x0 = cx - chip_w // 2
        y0 = cy - chip_h // 2
        x1 = cx + chip_w // 2
        y1 = cy + chip_h // 2

        fill_c = warning_chip if is_fail_node else chip_active
        border_c = warning_color if is_fail_node else border_active
        text_c = warning_color if is_fail_node else text_active

        draw.rounded_rectangle(
            [(x0, y0), (x1, y1)],
            radius=int(5 * SCALE),
            fill=fill_c,
            outline=border_c,
            width=int(1 * SCALE)
        )
        draw.text((x0 + int(7 * SCALE), y0 + int(3 * SCALE)), node_name, fill=text_c, font=font_mono_bold)

        if i < len(nodes) - 1:
            arr_x = start_x + (i + 1) * node_width - int(8 * SCALE)
            draw.text((arr_x, cy - int(8 * SCALE)), "→", fill=arrow_active, font=font_mono_bold)

    img_res = img.resize((WIDTH // SCALE, HEIGHT // SCALE), Image.Resampling.LANCZOS)
    frames.append(img_res.convert("P", palette=Image.Palette.ADAPTIVE, colors=64))
    durations.append(1300)

    # Save animated GIF
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
    generate_loop_gif(dark=True, output_path="assets/loop-dark.gif")
    generate_loop_gif(dark=False, output_path="assets/loop-light.gif")
    generate_pipeline_gif(dark=True, output_path="assets/pipeline-dark.gif")
    generate_pipeline_gif(dark=False, output_path="assets/pipeline-light.gif")
    print("All animated GIFs created successfully!")
