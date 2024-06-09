from image_processor import ImageProcessor
from watermark import Watermark

"""
Entry point for the image watermarking script.

This script creates a Watermark object, an ImageProcessor object using
the Watermark object, and calls the ImageProcessor's add_watermark method
to process images in the configured folder and add watermarks. Finally,
a message is printed indicating completion.
"""

# Create a watermark object
watermark = Watermark()

# Create an image processor object
image_processor = ImageProcessor(watermark)

# Add watermark to all images in the configured folder
image_processor.add_watermark()

print("Watermarking complete!")
