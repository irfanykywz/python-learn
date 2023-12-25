# pip install pillow

from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
image = Image.new('RGB', (300, 200), color='white')

# Create a draw object to draw on the image
draw = ImageDraw.Draw(image)

# Set the font and size
font = ImageFont.truetype('arial.ttf', 20)

# Draw the text on the image
draw.text((10, 10), 'Hello, World!', font=font, fill='black')

# Save the image
image.save('output_image.png')