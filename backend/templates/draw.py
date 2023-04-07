from PIL import Image, ImageDraw, ImageFont


def generate_image(text):
    img = Image.new('RGB', (800, 600), color = (255, 255, 255))

    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 36)
    d.text((10,10), text, fill=(0,0,0), font=font)

    img.save('static/images/image.png')
    return '/static/images/image.png'
