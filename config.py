"""Configuration options for image watermarking process."""

watermark_text = "TAG"  # Change to "TAG" for circular watermark
"""Text to be used as the watermark."""

watermark_color_1 = (255, 220, 220)  # Navy Blue (RGB)
"""Primary color of the watermark (RGB tuple)."""

watermark_color_2 = (128, 128, 128)  # Grey (RGB)
"""Secondary color of the watermark (RGB tuple, optional for circle outline)."""

watermark_opacity = 50
"""Transparency level of the watermark (0-255, 0 is fully transparent)."""

font_path = "fonts/glorious-christmas-font/GloriousChristmas-BLWWB.ttf"
"""Path to the desired font file for the watermark text (optional)."""

font_size = 45  # Adjust font size as needed
"""Font size for the watermark text."""

image_folder = "/Users/abigailwoolley/ArtWorld/AISideHustles/Videos/ReadyToPost/TechArtGenius/trial"
"""Path to the folder containing the images to be watermarked."""
