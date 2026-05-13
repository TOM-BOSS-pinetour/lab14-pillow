from pathlib import Path
from PIL import Image, ImageDraw

INPUT_DIR = Path("task2_input")
OUTPUT = Path("task2_thumbnails_collage.png")


def get_resample():
    if hasattr(Image, "Resampling"):
        return Image.Resampling.LANCZOS
    return Image.LANCZOS


def find_images(folder: Path) -> list[Path]:
    exts = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
    return sorted([p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in exts])


def placeholder(idx: int, size=(900, 600)) -> Image.Image:
    colors = [(210, 210, 250), (210, 250, 210), (250, 220, 210)]
    img = Image.new("RGB", size, colors[(idx - 1) % len(colors)])
    draw = ImageDraw.Draw(img)
    draw.text((30, 30), f"IMAGE {idx}", fill=(30, 30, 30))
    return img


def fit_center(img: Image.Image, box_size: tuple[int, int]) -> Image.Image:
    box_w, box_h = box_size
    canvas = Image.new("RGB", box_size, (245, 245, 245))

    src = img.copy()
    src.thumbnail(box_size, get_resample())
    px = (box_w - src.width) // 2
    py = (box_h - src.height) // 2
    canvas.paste(src, (px, py))
    return canvas


def main() -> None:
    INPUT_DIR.mkdir(parents=True, exist_ok=True)

    files = find_images(INPUT_DIR)
    imgs: list[Image.Image] = []

    for i in range(3):
        if i < len(files):
            imgs.append(Image.open(files[i]).convert("RGB"))
        else:
            imgs.append(placeholder(i + 1))

    thumb_size = (360, 220)
    gap = 20
    margin = 20

    canvas_w = thumb_size[0] * 2 + gap + margin * 2
    canvas_h = thumb_size[1] * 2 + gap + margin * 2
    canvas = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))

    top_left = (margin, margin)
    top_right = (margin + thumb_size[0] + gap, margin)
    bottom_center = ((canvas_w - thumb_size[0]) // 2, margin + thumb_size[1] + gap)

    for img, pos in zip(imgs, [top_left, top_right, bottom_center]):
        tile = fit_center(img, thumb_size)
        canvas.paste(tile, pos)

    draw = ImageDraw.Draw(canvas)
    border_color = (20, 20, 20)
    draw.rectangle((0, 0, canvas_w - 1, canvas_h - 1), outline=border_color, width=2)
    draw.line((canvas_w // 2, margin, canvas_w // 2, margin + thumb_size[1]), fill=border_color, width=2)
    draw.line(
        (margin, margin + thumb_size[1] + gap // 2, canvas_w - margin, margin + thumb_size[1] + gap // 2),
        fill=border_color,
        width=2,
    )

    canvas.save(OUTPUT)

    print(f"Input folder: {INPUT_DIR.resolve()}")
    print(f"Found images: {len(files)}")
    print(f"Saved: {OUTPUT}")
    if len(files) < 3:
        print("Note: Less than 3 input images, placeholders were used.")


if __name__ == "__main__":
    main()
