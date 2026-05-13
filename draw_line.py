from PIL import Image, ImageDraw

img = Image.new("RGB", (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)

draw.line((200, 100, 300, 200), fill=(0, 0, 0), width=10)

img.save("line_result.png")

img.show()
