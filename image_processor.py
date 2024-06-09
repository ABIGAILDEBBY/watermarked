import os

from PIL import Image

from config import image_folder  # Import image folder path


class ImageProcessor:
    """
    Class for processing images and adding watermarks.

    This class handles iterating through images in a specified folder,
    adding watermarks using a provided Watermark object, and saving
    the watermarked images.
    """

    def __init__(self, watermark):
        """
        Initialize an ImageProcessor object.

        Args:
            watermark (Watermark): An instance of the Watermark class
                containing watermark properties.
        """
        self.watermark = watermark
        self.image_folder = image_folder

    def add_watermark(self):
        """
        Loops through images in the configured folder and adds watermarks.

        This method iterates through all files in the `image_folder` path,
        checks for image extensions (currently JPG and JPEG), attempts to
        open the image using Pillow's Image.open function, and if successful,
        calls the `draw_circle_watermark` method of the provided `watermark`
        object to add a watermark. The watermarked image is then converted
        to RGB format (to avoid transparency errors when saving as JPEG) and
        saved back to the original image path. Any errors encountered during
        the process are printed to the console.
        """
        for filename in os.listdir(self.image_folder):
            if filename.lower().endswith((".jpg", ".jpeg")):
                image_path = os.path.join(self.image_folder, filename)
                try:
                    image = Image.open(image_path)
                except (IOError, OSError) as e:
                    print(f"Error opening image: {image_path} - {e}")
                    continue

                watermarked_image = self.watermark.draw_circle_watermark(image)

                # Convert to RGB before saving as JPEG (to avoid transparency
                # error)
                watermarked_image.putalpha(
                    watermarked_image.convert("L").point(
                        lambda x: x * self.watermark.opacity // 255))
                watermarked_image = watermarked_image.convert("RGB")

                # Save the watermarked image (replace with desired
                # filename/path)
                watermarked_image.save(image_path)
                print(f"Watermarked: {image_path}")
