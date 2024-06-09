import os

from PIL import Image, ImageDraw, ImageFont

# Folder containing your images
image_folder = "/Users/abigailwoolley/ArtWorld/AISideHustles/Videos/ReadyToPost/TechArtGenius/trial"

# Watermark text and colors
watermark_text = "TechArtGenius"
watermark_color_1 = (0, 0, 0)  # Navy Blue (RGB)
watermark_color_2 = (128, 128, 140)  # Grey (RGB)

# Watermark transparency (0 - fully transparent, 255 - fully opaque)
watermark_opacity = 178  # 70% visible

# Font size and path (adjust font size and path as needed)
font_size = 100
# Replace with your font path (if using a custom font)
font_path = "/Users/abigailwoolley/PersonalProjects/TechArtGenius/fonts/Bighome.otf"


def add_watermark(image_path):
    """Adds watermark to an image, centered horizontally and vertically."""
    image = Image.open(image_path).convert(
        "RGBA")  # Open image with alpha channel
    watermark = Image.new("RGBA", image.size, (0, 0, 0, 0)
                          )  # Create transparent canvas
    draw = ImageDraw.Draw(watermark)

    # Get the dimensions of the watermark text
    text_width, text_height = draw.textsize(
        watermark_text, font=ImageFont.truetype(
            font_path, font_size))

    # Calculate the center coordinates for the watermark text
    x_center = (image.width - text_width) // 2
    y_center = (image.height - text_height) // 2

    # Draw the watermark text at the center coordinates
    draw.text(
        (x_center,
         y_center),
        watermark_text,
        font=ImageFont.truetype(
            font_path,
            font_size),
        fill=watermark_color_1)
    draw.text(
        (x_center,
         y_center),
        watermark_text,
        font=ImageFont.truetype(
            font_path,
            font_size),
        fill=watermark_color_2)

    # Composite watermark onto image
    image = Image.alpha_composite(image, watermark)
    image.putalpha(
        watermark.convert("L").point(
            lambda x: x *
            watermark_opacity //
            255))  # Set watermark transparency

    # Convert image to RGB before saving as JPEG (to avoid transparency error)
    image = image.convert("RGB")
    image.save(image_path)  # Save the watermarked image


# Loop through images in the folder
for filename in os.listdir(image_folder):
    if filename.lower().endswith((".jpg", ".jpeg")
                                 ):  # Check for JPG/JPEG extensions only (if transparency not needed)
        image_path = os.path.join(image_folder, filename)
        # print("IMAGE PATH", image_path)
        add_watermark(image_path)
        print(f"Watermarked: {image_path}")

print("Watermarking complete!")
