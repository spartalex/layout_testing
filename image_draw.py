from PIL import Image, ImageDraw
text = "kek :)"
color = (120, 120, 120)
img = Image.open("screenie.png")
draw = ImageDraw.Draw(img)
draw.text((50, 50), "hello")
img.save("pil-example.png")