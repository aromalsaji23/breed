from PIL import Image, ImageDraw
import os

def create_background():
    # Create directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')

    # Create a new image with a gradient background
    width = 1920
    height = 1080
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)

    # Create a subtle gradient background
    for y in range(height):
        r = int(220 + (y / height) * 20)  # Slight variation in red
        g = int(230 + (y / height) * 15)  # Slight variation in green
        b = int(255 - (y / height) * 20)  # Slight variation in blue
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Save the image
    image.save('images/pets_bg.jpg', quality=95)

if __name__ == "__main__":
    create_background() 