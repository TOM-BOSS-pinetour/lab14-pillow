import argparse
from pathlib import Path
from PIL import Image

DEFAULT_INPUT_DIR = Path("task3_input")
DEFAULT_OUTPUT = Path("task3_converted.png")


def get_resample():
    if hasattr(Image, "Resampling"):
        return Image.Resampling.LANCZOS
    return Image.LANCZOS


def find_first_jpg(folder: Path) -> Path | None:
    if not folder.exists():
        return None
    candidates = sorted(
        p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg"}
    )
    return candidates[0] if candidates else None


def convert_jpg_to_png(input_path: Path, output_path: Path, new_width: int) -> None:
    with Image.open(input_path) as img:
        rgb = img.convert("RGB")
        scale = new_width / rgb.width
        new_height = max(1, int(rgb.height * scale))
        resized = rgb.resize((new_width, new_height), resample=get_resample())
        resized.save(output_path, format="PNG")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert JPG/JPEG to PNG and resize width.")
    parser.add_argument("--input", type=str, default="", help="Path to input JPG/JPEG file")
    parser.add_argument("--output", type=str, default=str(DEFAULT_OUTPUT), help="Path to output PNG file")
    parser.add_argument("--width", type=int, default=700, help="New width in pixels")
    args = parser.parse_args()

    if args.width <= 0:
        raise ValueError("--width must be a positive integer")

    input_path = Path(args.input) if args.input else find_first_jpg(DEFAULT_INPUT_DIR)
    if input_path is None or not input_path.exists():
        raise FileNotFoundError(
            "Input JPG not found. Put a .jpg/.jpeg file into task3_input/ or pass --input <path>."
        )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    convert_jpg_to_png(input_path, output_path, args.width)

    print(f"Input:  {input_path}")
    print(f"Output: {output_path}")
    print(f"Width:  {args.width}")


if __name__ == "__main__":
    main()
