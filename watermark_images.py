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
    """
    Adds a centered text watermark to an image with adjustable transparency.

    This function opens an image using PIL's `Image.open` function,
    ensures it has an alpha channel for transparency by converting it
    to 'RGBA' mode. It then creates a new transparent RGBA image as the
    watermark canvas.

    The function calculates the dimensions (width and height) of the
    watermark text using `draw.textsize` and the provided font and size.
    It then calculates the center coordinates for placing the watermark
    text horizontally and vertically centered on the original image.

    Using the `ImageDraw` object on the watermark canvas, the function
    draws the watermark text twice with a slight difference:
     - The first layer uses the `watermark_color_2` (usually a lighter shade)
     - The second layer uses the `watermark_color_1` (usually the main color)

    This creates a double-layered text effect for the watermark.

    Finally, the watermark image is composited onto the original image
    using `Image.alpha_composite`. The transparency level of the combined
    image is set based on the `watermark_opacity` value using calculations
    and conversion to the 'L' (luminance) mode. The image is then converted
    to 'RGB' mode (to avoid transparency errors when saving as JPEG)
    and saved back to the original image path.

    Args:
        image_path (str): The path to the image file to be watermarked.
    """

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
