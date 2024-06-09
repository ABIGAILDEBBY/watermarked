# Image Watermarking Tool

This Python script provides a tool for batch image watermarking with customizable options.

**Features:**

* Adds a watermark (text and/or circle) to multiple images in a folder.
* Customizable watermark text, color, and opacity.
* Supports various image formats (configurable).
* Leverages classes (`ImageProcessor` and `Watermark`) for modularity.

**Requirements:**

* Python 3.x
* Pillow (PIL Fork) library: `pip install Pillow`

**Installation:**

1. **Install Python 3:**
    If you don't have Python 3 installed, download and install it from the official website: https://www.python.org/downloads/.

2. **Install Pillow Library:**
    Open your terminal and run the following command to install the Pillow library:

    ```bash
    pip install Pillow
    ```

**Usage:**

1. **Project Setup:**
    * Clone or download this repository to your local machine.
    * Replace the placeholder values in `config.py` with your desired settings:
        * `watermark_text`: The text to be used as a watermark.
        * `watermark_color_1`: Text color (RGB tuple).
        * `watermark_color_2` (optional): Circle outline color (RGB tuple, defaults to grey).
        * `watermark_opacity`: Transparency level (0-255, 0 is fully transparent).
        * `font_path`: Path to your desired font file (if using a custom font).
        * `image_folder`: Path to the folder containing your images.

2. **Run the Script:**
    * Open your terminal and navigate to the project directory where you cloned/downloaded the code.
    * Run the script using the following command:

    ```bash
    python main.py
    ```

    This will watermark all the images in the specified folder (`image_folder`) according to your configuration settings.

**Example Configuration (config.py):**

```python
watermark_text = "TechArtGenius"
watermark_color_1 = (0, 0, 0)  # Black (text)
watermark_color_2 = (128, 128, 140)  # Grey (circle outline, optional)
watermark_opacity = 178  # 70% opacity
font_path = "/path/to/your/font.ttf"  # Replace with your font path (optional)
image_folder = "/path/to/your/images/folder"  # Replace with your image folder path
