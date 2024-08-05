# Animated GIF Creator

This project creates an animated GIF by rotating a static image through multiple frames using the Python Imaging Library (PIL).

## Features

- Open a static image.
- Generate multiple frames by rotating the static image.
- Save the frames as an animated GIF.

## Technologies Used

- **Python**: Programming language used to develop the script.
- **Pillow (PIL)**: Python Imaging Library used for image processing.

## Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/yourusername/AnimatedGIFCreator
    cd AnimatedGIFCreator
    ```

2. **Install Dependencies:**

    Make sure you have Python and Pillow installed. You can install Pillow using pip:

    ```sh
    pip install Pillow
    ```

## Usage

1. **Prepare your static image:**

    Ensure you have a static image file named `static_image.jpg` in your project directory or modify the script to point to your image file.

2. **Run the Script:**

    ```python
    from PIL import Image

    # Open the static image
    static_image = Image.open("static_image.jpg")

    # Create a list to store the frames
    frames = []

    # Add each frame to the list (modify as needed)
    for i in range 10):  # Assuming 10 frames
        # Create a new frame by rotating the static image
        angle = i * 36  # 36 degrees rotation for each frame
        rotated_frame = static_image.rotate(angle)
        frames.append(rotated_frame)

    # Save the frames as an animated GIF
    frames[0].save("output_image.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)
    ```

3. **Output:**

    The script will generate an animated GIF named `output_image.gif` in your project directory.

## Customization

- **Number of Frames:** Change the number of frames by modifying the range in the for loop (`for i in range(10)`).
- **Rotation Angle:** Adjust the rotation angle by modifying the multiplier (`angle = i * 36`).
- **Duration:** Change the duration of each frame by modifying the `duration` parameter in the `save` method.
- **Loop:** Set the number of times the GIF should loop by modifying the `loop` parameter in the `save` method.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
