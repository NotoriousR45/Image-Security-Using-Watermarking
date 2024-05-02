from PIL import Image, ImageDraw, ImageFont

demo_image = Image.open('conv.jpg')
img_width, img_height = demo_image.size

draw_image = ImageDraw.Draw(demo_image)
text_image = "Aman"

font_image = ImageFont.truetype('C:/Users/ROHIT CHHETRI/PycharmProjects/firstproj/CollegiateBlackFLF.ttf',30)
text_width, text_height = draw_image.textsize(text_image,font_image)

font_margin = 12
x = 0
y = 0

draw_image.text((x,y), text_image, font = font_image)
demo_image.show()

demo_image.save("watermark.jpg")



