from PIL import Image

# Open the static image
static_image = Image.open("/content/WhatsApp Image 2024-02-12 at 00.21.12_6d67b829.jpg")

# Create a list to store the frames
frames = []

# Add each frame to the list (modify as needed)
for i in range(10):  # Assuming 10 frames
    # Create a new frame by rotating the static image
    angle = i * 36  # 36 degrees rotation for each frame
    rotated_frame = static_image.rotate(angle)
    frames.append(rotated_frame)

# Save the frames as an animated GIF
frames[0].save("output_image.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)