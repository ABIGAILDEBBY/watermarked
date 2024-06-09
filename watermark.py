from PIL import ImageDraw, ImageFont

from config import (font_path, font_size,  # Import configuration
                    watermark_color_1, watermark_color_2, watermark_opacity,
                    watermark_text)
from utils import convert_to_rgba, get_text_size


class Watermark:
    """
    Class representing a watermark with properties and drawing functionality.

    This class defines a watermark object with properties like text, colors,
    opacity, font path, and font size. It also includes a method
    `draw_circle_watermark` that takes a PIL image object and adds a circular
    watermark with the configured text centered on the image.
    """

    def __init__(self):
        """
        Initialize a Watermark object with properties from configuration.

        This constructor retrieves watermark properties (text, colors, opacity,
        font path, and font size) from the configuration file (`config.py`).
        It also calculates the alpha value based on the opacity for transparency.
        """
        self.text = watermark_text
        self.color_1 = watermark_color_1
        self.color_2 = watermark_color_2
        self.opacity = watermark_opacity
        self.font_path = font_path
        self.font_size = font_size
        self.alpha = int(255 * (self.opacity / 100))

        # self.watermark_navy_blue = watermark_navy_blue (commented out)

    def draw_circle_watermark(self, image):
        """
        Draws a circular watermark with text centered on the provided image.

        This method takes a PIL Image object as input. It ensures the image
        has an alpha channel for transparency using `convert_to_rgba` from the
        `utils.py` module. Then, it creates an ImageDraw object and calculates
        the width and height of the watermark text using `get_text_size` from
        `utils.py`.

        The method calculates the radius and center coordinates for the circular
        watermark based on the text size and image dimensions. It then draws
        a filled circle with the outline color and the text centered inside the
        circle using the specified font and colors (with transparency applied
        based on the alpha value).

        Args:
            image (PIL.Image): The image object to add the watermark to.

        Returns:
            PIL.Image: The modified image with the watermark drawn on it.
        """
        image = convert_to_rgba(image)  # Ensure image has alpha channel

        draw = ImageDraw.Draw(image)
        text_width, text_height = get_text_size(
            self.text, self.font_path, self.font_size)

        # Calculate circle radius and center coordinates
        max_text_size = max(text_width, text_height)
        radius = max_text_size // 2 + 10  # Adjust padding as needed
        center_x = image.width // 2
        center_y = image.height // 2

        # Draw filled circle
        draw.ellipse([(center_x -
                       radius, center_y -
                       radius), (center_x +
                                 radius, center_y +
                                 radius)], width=5,
                     outline=self.color_2)

        # Draw text inside circle, centered
        text_x = center_x - text_width // 2
        text_y = center_y - text_height // 2
        draw.text((text_x, text_y), self.text, font=ImageFont.truetype(
            self.font_path, self.font_size), fill=self.color_1, alpha=self.alpha)

        return image
