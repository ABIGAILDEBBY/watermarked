from PIL import Image, ImageDraw, ImageFont


def get_text_size(text, font_path, font_size):
    """Calculates the width and height of a text based on font and size."""
    return ImageDraw.Draw(Image.new('L', (1, 1))).textsize(
        text, font=ImageFont.truetype(font_path, font_size))


def check_image_mode(image):
    """Checks if the image has an alpha channel (RGBA mode)."""
    return image.mode == 'RGBA'


def convert_to_rgba(image):
    """Converts the image to RGBA mode if necessary (for consistency)."""
    if not check_image_mode(image):
        return image.convert('RGBA')
    return image
