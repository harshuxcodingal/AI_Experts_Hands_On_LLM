import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread("original_images/example.jpg")

# Check if the image exists
if img is None:
    print("Error: Unable to load the image.")

else:
    # Convert BGR to RGB for displaying with Matplotlib
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Get image dimensions
    height, width, channels = img.shape

    # Define the arrow positions
    start_point = (30, height - 40)
    end_point = (width - 30, height - 40)

    # Draw arrows in both directions
    cv2.arrowedLine(rgb_img, start_point, end_point, (255, 0, 0), 2, tipLength=0.04)
    cv2.arrowedLine(rgb_img, end_point, start_point, (255, 0, 0), 2, tipLength=0.04)

    # Add width label
    text_position = (width // 2 - 60, height - 60)

    cv2.putText(
        rgb_img,
        f"Width = {width} px",
        text_position,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    # Save the output image
    cv2.imwrite("output_images/width_measurement.jpg", cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR))

    # Display the image
    plt.figure(figsize=(8, 5))
    plt.imshow(rgb_img)
    plt.title("Image Width Measurement")
    plt.axis("off")
    plt.show()