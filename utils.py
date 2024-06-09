from PIL import Image, ImageDraw, ImageFont


def get_text_size(text, font_path, font_size):
    """
    Calculates the width and height of a text string based on font and size.

    This function creates a temporary 1x1 pixel image in 'L' (luminance)
    mode and uses an ImageDraw object to draw the text on it with the
    specified font path and size. It then returns a tuple containing
    the width and height of the rendered text.

    Args:
        text (str): The text string to calculate the size for.
        font_path (str): The path to the font file to be used.
        font_size (int): The desired font size.

    Returns:
        tuple: A tuple containing the width and height of the text.
    """
    return ImageDraw.Draw(Image.new('L', (1, 1))).textsize(
        text, font=ImageFont.truetype(font_path, font_size))


def check_image_mode(image):
    """
    Checks if the image has an alpha channel (RGBA mode).

    This function checks the image mode of the provided PIL Image object
    and returns True if the mode is 'RGBA' (indicating an alpha channel
    for transparency), False otherwise.

    Args:
        image (PIL.Image): The image object to check the mode for.

    Returns:
        bool: True if the image has an alpha channel, False otherwise.
    """
    return image.mode == 'RGBA'


def convert_to_rgba(image):
    """
    Converts the image to RGBA mode if necessary (for consistency).

    This function checks if the image has an alpha channel using the
    `check_image_mode` function. If the image mode is not 'RGBA', it
    converts the image to RGBA mode using the `convert` method. This
    ensures consistent handling of transparency across different image
    formats.

    Args:
        image (PIL.Image): The image object to potentially convert.

    Returns:
        PIL.Image: The image object, potentially converted to RGBA mode.
    """
    if not check_image_mode(image):
        return image.convert('RGBA')
    return image
