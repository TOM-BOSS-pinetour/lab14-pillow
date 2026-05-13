from PIL import Image, ImageDraw

img = Image.new("RGB", (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)

draw.ellipse((200, 125, 300, 200), fill=(255, 0, 0), outline=(0, 0, 0))

img.save("circle_result.png")

img.show()
