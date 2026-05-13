from PIL import Image, ImageDraw

WIDTH, HEIGHT = 500, 300
BG = (160, 160, 160)


def base_canvas() -> Image.Image:
    return Image.new("RGB", (WIDTH, HEIGHT), BG)


def draw_cross(path: str) -> None:
    img = base_canvas()
    draw = ImageDraw.Draw(img)
    draw.line((150, 90, 350, 230), fill=(0, 0, 0), width=16)
    draw.line((350, 90, 150, 230), fill=(0, 0, 0), width=16)
    img.save(path)


def draw_two_circles(path: str) -> None:
    img = base_canvas()
    draw = ImageDraw.Draw(img)
    draw.ellipse((60, 40, 190, 170), fill=(90, 170, 230), outline=(50, 110, 170), width=6)
    draw.ellipse((150, 100, 280, 230), fill=(255, 200, 0), outline=(205, 150, 0), width=6)
    img.save(path)


def draw_polygon(path: str) -> None:
    img = base_canvas()
    draw = ImageDraw.Draw(img)
    draw.polygon([(70, 120), (350, 185), (250, 250)], fill=(245, 0, 230), outline=(220, 0, 210))
    img.save(path)


def draw_rectangles(path: str) -> None:
    img = base_canvas()
    draw = ImageDraw.Draw(img)
    draw.rectangle((30, 30, 170, 130), fill=(90, 170, 230), outline=(50, 110, 170), width=6)
    draw.rectangle((180, 140, 340, 250), fill=(110, 175, 70), outline=(255, 255, 255), width=6)
    img.save(path)


def build_preview(paths: list[str], out_path: str) -> None:
    gap = 20
    canvas_w = WIDTH * 2 + gap * 3
    canvas_h = HEIGHT * 2 + gap * 3
    merged = Image.new("RGB", (canvas_w, canvas_h), (235, 235, 235))

    positions = [
        (gap, gap),
        (gap * 2 + WIDTH, gap),
        (gap, gap * 2 + HEIGHT),
        (gap * 2 + WIDTH, gap * 2 + HEIGHT),
    ]

    for image_path, pos in zip(paths, positions):
        with Image.open(image_path) as frame:
            merged.paste(frame, pos)

    merged.save(out_path)


def main() -> None:
    cross_path = "task1_cross.png"
    circles_path = "task1_circles.png"
    polygon_path = "task1_polygon.png"
    rectangles_path = "task1_rectangles.png"

    draw_cross(cross_path)
    draw_two_circles(circles_path)
    draw_polygon(polygon_path)
    draw_rectangles(rectangles_path)

    build_preview(
        [cross_path, circles_path, polygon_path, rectangles_path],
        "task1_all_shapes.png",
    )

    print("Saved: task1_cross.png")
    print("Saved: task1_circles.png")
    print("Saved: task1_polygon.png")
    print("Saved: task1_rectangles.png")
    print("Saved: task1_all_shapes.png")


if __name__ == "__main__":
    main()
