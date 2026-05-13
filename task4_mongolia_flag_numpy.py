import numpy as np
from PIL import Image, ImageDraw

# Mongolia flag ratio: 1:2
HEIGHT = 300
WIDTH = 600


def main() -> None:
    flag = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    stripe_w = WIDTH // 3

    red = (220, 0, 0)
    blue = (0, 25, 190)

    flag[:, :stripe_w] = red
    flag[:, stripe_w : stripe_w * 2] = blue
    flag[:, stripe_w * 2 :] = red

    img = Image.fromarray(flag, mode="RGB")

    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, WIDTH - 1, HEIGHT - 1), outline=(0, 0, 0), width=2)

    img.save("task4_mongolia_flag.png")
    print("Saved: task4_mongolia_flag.png")


if __name__ == "__main__":
    main()
