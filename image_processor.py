import os

from PIL import Image

from config import image_folder  # Import image folder path


class ImageProcessor:
    def __init__(self, watermark):
        self.watermark = watermark
        self.image_folder = image_folder

    def add_watermark(self):
        """Loops through images in the configured folder and adds watermark."""
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
