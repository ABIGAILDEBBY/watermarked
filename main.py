from image_processor import ImageProcessor
from watermark import Watermark

# Create a watermark object
watermark = Watermark()

# Create an image processor object
image_processor = ImageProcessor(watermark)

# Add watermark to all images in the configured folder
image_processor.add_watermark()

print("Watermarking complete!")
