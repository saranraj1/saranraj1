import os, math
from PIL import Image, ImageDraw, ImageFont

SCALE = 2
WIDTH = 900 * SCALE
HEIGHT = 280 * SCALE
RADIUS = 12 * SCALE

# Load fonts
try:
    font_name = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 23 * SCALE)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 10.5 * SCALE)
    font_tag = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 9 * SCALE)
    font_tag_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 9 * SCALE)
    font_axiom = ImageFont.truetype("C:/Windows/Fonts/segoeuii.ttf", 11.5 * SCALE)
    font_quote = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 10.5 * SCALE)
    font_quote_cyan = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 10.5 * SCALE)
    font_hud = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 8.5 * SCALE)
    font_hud_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 8.5 * SCALE)
except Exception:
    font_name = ImageFont.load_default()
    font_sub = font_name
    font_tag = font_name
    font_tag_bold = font_name
    font_axiom = font_name
    font_quote = font_name
    font_quote_cyan = font_name
    font_hud = font_name
    font_hud_bold = font_name

# Outer Icosahedron Vertices
phi = (1 + math.sqrt(5)) / 2
raw_outer = [
    (-1, phi, 0), (1, phi, 0), (-1, -phi, 0), (1, -phi, 0),
    (0, -1, phi), (0, 1, phi), (0, -1, -phi), (0, 1, -phi),
    (phi, 0, -1), (phi, 0, 1), (-phi, 0, -1), (-phi, 0, 1)
]
outer_verts = []
for x, y, z in raw_outer:
    l = math.sqrt(x*x + y*y + z*z)
    outer_verts.append((x/l, y/l, z/l))

outer_edges = []
for i in range(len(outer_verts)):
    for j in range(i+1, len(outer_verts)):
        dx = outer_verts[i][0] - outer_verts[j][0]
        dy = outer_verts[i][1] - outer_verts[j][1]
        dz = outer_verts[i][2] - outer_verts[j][2]
        d = math.sqrt(dx*dx + dy*dy + dz*dz)
        if abs(d - 1.05146) < 0.05:
            outer_edges.append((i, j))

# Inner Octahedron Vertices (Dual Core)
inner_verts = [
    (0.52, 0, 0), (-0.52, 0, 0),
    (0, 0.52, 0), (0, -0.52, 0),
    (0, 0, 0.52), (0, 0, -0.52)
]
inner_edges = [
    (0, 2), (0, 3), (0, 4), (0, 5),
    (1, 2), (1, 3), (1, 4), (1, 5),
    (2, 4), (4, 3), (3, 5), (5, 2)
]

def render_3d_hero_frame(frame_idx, total_frames=30, dark=True):
    img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if dark:
        bg = (8, 11, 18, 255)              # #080b12
        border = (30, 41, 59, 255)         # #1e293b
        bar_bg = (13, 19, 31, 255)         # #0d131f
        text_main = (241, 245, 249, 255)   # #f1f5f9
        text_muted = (148, 163, 184, 255)  # #94a3b8
        text_dim = (71, 85, 105, 255)      # #475569
        accent = (34, 211, 238, 255)       # #22d3ee cyan
        accent_dim = (34, 211, 238, 80)
        core_col = (52, 211, 153, 255)     # #34d399 emerald
        hud_bg = (11, 16, 26, 255)
        hud_border = (26, 36, 52, 255)
    else:
        bg = (248, 250, 252, 255)          # #f8fafc
        border = (217, 222, 232, 255)      # #d9dee8
        bar_bg = (255, 255, 255, 255)      # #ffffff
        text_main = (15, 23, 42, 255)      # #0f172a
        text_muted = (100, 116, 139, 255)  # #64748b
        text_dim = (148, 163, 184, 255)    # #94a3b8
        accent = (8, 145, 178, 255)        # #0891b2 cyan
        accent_dim = (8, 145, 178, 60)
        core_col = (16, 185, 129, 255)     # #10b981 emerald
        hud_bg = (255, 255, 255, 255)
        hud_border = (226, 232, 240, 255)

    # 1. Main outer border
    draw.rounded_rectangle(
        [(1, 1), (WIDTH - 2, HEIGHT - 2)],
        radius=RADIUS,
        fill=bg,
        outline=border,
        width=int(1.2 * SCALE)
    )

    # 2. Header Bar
    bar_h = int(32 * SCALE)
    draw.rounded_rectangle(
        [(int(2 * SCALE), int(2 * SCALE)), (WIDTH - int(3 * SCALE), bar_h)],
        radius=RADIUS,
        fill=bar_bg
    )
    draw.line(
        [(int(2 * SCALE), bar_h), (WIDTH - int(3 * SCALE), bar_h)],
        fill=border,
        width=int(1 * SCALE)
    )

    # Header Telemetry
    dot_y = bar_h // 2 + int(1 * SCALE)
    beacon_r = int(3 * SCALE)
    draw.ellipse([int(22 * SCALE) - beacon_r, dot_y - beacon_r, int(22 * SCALE) + beacon_r, dot_y + beacon_r], fill=accent)
    draw.text((int(32 * SCALE), dot_y - int(6 * SCALE)), "SARAN RAJ // AI RESEARCH LAB", fill=text_main, font=font_tag_bold)
    draw.text((WIDTH - int(24 * SCALE), dot_y - int(6 * SCALE)), "VERIFICATION & RELIABILITY", fill=accent, font=font_tag_bold, anchor="ra")

    # ---------------------------------------------------------
    # LEFT COLUMN: Humanized Research Identity
    # ---------------------------------------------------------
    left_x = int(28 * SCALE)
    start_y = bar_h + int(18 * SCALE)

    draw.text((left_x, start_y), "AI / ML RESEARCHER · INDEPENDENT", fill=accent, font=font_tag_bold)
    draw.text((left_x, start_y + int(15 * SCALE)), "U SARAN RAJ", fill=text_main, font=font_name)
    draw.text((left_x, start_y + int(46 * SCALE)), "RESPONSIBLE AI · AGENT SYSTEMS · CODE INTELLIGENCE", fill=text_muted, font=font_sub)

    # Divider
    div_y1 = start_y + int(68 * SCALE)
    draw.line([(left_x, div_y1), (int(470 * SCALE), div_y1)], fill=border, width=int(1 * SCALE))

    # Human research statement
    stmt_y = div_y1 + int(10 * SCALE)
    draw.text((left_x, stmt_y), '"I investigate where intelligent systems fail —', fill=text_main, font=font_axiom)
    draw.text((left_x, stmt_y + int(17 * SCALE)), ' and build tools to expose why."', fill=accent, font=font_axiom)

    # Divider
    div_y2 = stmt_y + int(39 * SCALE)
    draw.line([(left_x, div_y2), (int(470 * SCALE), div_y2)], fill=border, width=int(1 * SCALE))

    # Core philosophy
    phil_y = div_y2 + int(10 * SCALE)
    draw.text((left_x, phil_y), "BUILD INTELLIGENCE.", fill=text_main, font=font_quote)
    draw.text((left_x, phil_y + int(16 * SCALE)), "EXPOSE ITS REASONING.", fill=text_main, font=font_quote)
    draw.text((left_x, phil_y + int(32 * SCALE)), "OWN ITS CONSEQUENCES.", fill=accent, font=font_quote_cyan)

    # Footer note
    draw.text((left_x, HEIGHT - int(16 * SCALE)), "CHENNAI, IN · EVIDENCE-FIRST EMPIRICAL RESEARCH", fill=text_dim, font=font_hud)

    # ---------------------------------------------------------
    # RIGHT COLUMN: 3D Animated Neural Manifold HUD
    # ---------------------------------------------------------
    hud_x0 = int(510 * SCALE)
    hud_y0 = bar_h + int(12 * SCALE)
    hud_x1 = WIDTH - int(20 * SCALE)
    hud_y1 = HEIGHT - int(14 * SCALE)

    draw.rounded_rectangle(
        [(hud_x0, hud_y0), (hud_x1, hud_y1)],
        radius=int(8 * SCALE),
        fill=hud_bg,
        outline=hud_border,
        width=int(1 * SCALE)
    )

    # HUD Header
    hud_bar_h = int(22 * SCALE)
    draw.line([(hud_x0, hud_y0 + hud_bar_h), (hud_x1, hud_y0 + hud_bar_h)], fill=hud_border, width=int(1 * SCALE))
    draw.text((hud_x0 + int(10 * SCALE), hud_y0 + int(5 * SCALE)), "3D LOSS MANIFOLD // SO(3) PROJECTION", fill=text_muted, font=font_hud_bold)
    deg = int((frame_idx / total_frames) * 360)
    draw.text((hud_x1 - int(10 * SCALE), hud_y0 + int(5 * SCALE)), f"AZIMUTH: {deg:03d}°", fill=accent, font=font_hud_bold, anchor="ra")

    # HUD Caliper Corner Crosshairs
    cross_sz = int(6 * SCALE)
    for cx_pos, cy_pos in [(hud_x0 + int(6 * SCALE), hud_y0 + hud_bar_h + int(6 * SCALE)),
                           (hud_x1 - int(6 * SCALE), hud_y0 + hud_bar_h + int(6 * SCALE)),
                           (hud_x0 + int(6 * SCALE), hud_y1 - int(6 * SCALE)),
                           (hud_x1 - int(6 * SCALE), hud_y1 - int(6 * SCALE))]:
        draw.line([(cx_pos - cross_sz, cy_pos), (cx_pos + cross_sz, cy_pos)], fill=border, width=1)
        draw.line([(cx_pos, cy_pos - cross_sz), (cx_pos, cy_pos + cross_sz)], fill=border, width=1)

    # 3D Math Projection
    center_3d_x = (hud_x0 + hud_x1) // 2
    center_3d_y = (hud_y0 + hud_bar_h + hud_y1) // 2
    scale_3d = int(68 * SCALE)

    # Rotation angles: full 360 Y rotation, subtle wobble on X
    theta = (frame_idx / total_frames) * 2 * math.pi
    cos_y, sin_y = math.cos(theta), math.sin(theta)
    
    phi_angle = math.radians(24 + 4 * math.sin(theta))
    cos_x, sin_x = math.cos(phi_angle), math.sin(phi_angle)

    def project_point(p, r_scale):
        x, y, z = p[0] * r_scale, p[1] * r_scale, p[2] * r_scale
        # Rotate Y
        x1 = x * cos_y + z * sin_y
        z1 = -x * sin_y + z * cos_y
        # Tilt X
        y2 = y * cos_x - z1 * sin_x
        z2 = y * sin_x + z1 * cos_x
        # Perspective
        dist = 3.2
        p_factor = dist / (dist + z2)
        px = center_3d_x + x1 * p_factor * scale_3d
        py = center_3d_y - y2 * p_factor * scale_3d
        return (px, py, z2)

    # Background subtle ground grid
    grid_y_plane = center_3d_y + int(62 * SCALE)
    for gx in range(-3, 4):
        x_g = center_3d_x + gx * int(22 * SCALE)
        draw.line([(x_g, grid_y_plane - int(10 * SCALE)), (x_g, grid_y_plane + int(10 * SCALE))], fill=accent_dim, width=1)
    draw.line([(center_3d_x - int(70 * SCALE), grid_y_plane), (center_3d_x + int(70 * SCALE), grid_y_plane)], fill=accent_dim, width=1)

    # Project Outer Vertices
    proj_outer = [project_point(v, 1.0) for v in outer_verts]
    
    # Project Inner Core Vertices (counter-rotating for dual dynamic feel)
    theta_inner = -theta * 1.5
    cos_yi, sin_yi = math.cos(theta_inner), math.sin(theta_inner)
    def project_inner(p):
        x, y, z = p[0], p[1], p[2]
        x1 = x * cos_yi + z * sin_yi
        z1 = -x * sin_yi + z * cos_yi
        y2 = y * cos_x - z1 * sin_x
        z2 = y * sin_x + z1 * cos_x
        dist = 3.2
        p_factor = dist / (dist + z2)
        px = center_3d_x + x1 * p_factor * scale_3d
        py = center_3d_y - y2 * p_factor * scale_3d
        return (px, py, z2)
    proj_inner = [project_inner(v) for v in inner_verts]

    # Draw Inner Core Edges
    for i, j in inner_edges:
        x1, y1, z1 = proj_inner[i]
        x2, y2, z2 = proj_inner[j]
        alpha = int(140 + 115 * ((z1 + z2) / 2.0))
        alpha = max(60, min(255, alpha))
        if dark:
            edge_c = (52, 211, 153, alpha)
        else:
            edge_c = (16, 185, 129, alpha)
        draw.line([(x1, y1), (x2, y2)], fill=edge_c, width=int(1.2 * SCALE))

    # Inner Core Vertices
    for px, py, z_val in proj_inner:
        r = int(2.5 * SCALE)
        draw.ellipse([px - r, py - r, px + r, py + r], fill=core_col)

    # Sort Outer Edges by depth for clean rendering
    sorted_outer = []
    for i, j in outer_edges:
        avg_z = (proj_outer[i][2] + proj_outer[j][2]) / 2.0
        sorted_outer.append((avg_z, i, j))
    sorted_outer.sort()

    # Draw Outer Edges
    for z_val, i, j in sorted_outer:
        x1, y1, _ = proj_outer[i]
        x2, y2, _ = proj_outer[j]
        # Depth shading
        norm_z = (z_val + 1.0) / 2.0
        if dark:
            alpha = int(80 + 175 * norm_z)
            alpha = max(40, min(255, alpha))
            col = (34, 211, 238, alpha)
        else:
            alpha = int(90 + 165 * norm_z)
            alpha = max(50, min(255, alpha))
            col = (8, 145, 178, alpha)
        draw.line([(x1, y1), (x2, y2)], fill=col, width=int(1.4 * SCALE))

    # Outer Vertices with pulsing glow
    for px, py, z_val in proj_outer:
        norm_z = (z_val + 1.0) / 2.0
        r = int((2.0 + 1.8 * norm_z) * SCALE)
        if z_val > 0.1:
            draw.ellipse([px - r, py - r, px + r, py + r], fill=text_main)
        else:
            draw.ellipse([px - r, py - r, px + r, py + r], fill=accent)

    # HUD Bottom Status
    draw.text((hud_x0 + int(10 * SCALE), hud_y1 - int(14 * SCALE)), "VERTICES: 18 · EDGES: 42 · SO(3)", fill=text_dim, font=font_hud)
    draw.text((hud_x1 - int(10 * SCALE), hud_y1 - int(14 * SCALE)), "AUDIT STATE: OK", fill=core_col, font=font_hud_bold, anchor="ra")

    # Antialiased downsample
    img_res = img.resize((WIDTH // SCALE, HEIGHT // SCALE), Image.Resampling.LANCZOS)
    return img_res.convert("P", palette=Image.Palette.ADAPTIVE, colors=36)

def generate_3d_hero_gifs():
    total_frames = 24
    durations = [110] * total_frames  # ~2.64 second complete seamless loop

    for dark in [True, False]:
        mode_name = "dark" if dark else "light"
        out_path = f"assets/hero-{mode_name}.gif"
        print(f"Rendering 3D Hero {mode_name} ({total_frames} frames)...")
        frames = []
        for f in range(total_frames):
            frame = render_3d_hero_frame(f, total_frames=total_frames, dark=dark)
            frames.append(frame)
        
        frames[0].save(
            out_path,
            save_all=True,
            append_images=frames[1:],
            duration=durations,
            loop=0,
            optimize=True,
            disposal=2
        )
        print(f"Generated {out_path} ({os.path.getsize(out_path) // 1024} KB)")

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    generate_3d_hero_gifs()
