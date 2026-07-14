import cv2

# Load the image
img = cv2.imread("example.jpg")

# Check if the image was loaded successfully
if img is None:
    print("Error: Unable to load the image.")
else:
    # Create a resizable window
    cv2.namedWindow("Image Viewer", cv2.WINDOW_NORMAL)

    # Set the window size (Width, Height)
    cv2.resizeWindow("Image Viewer", 800, 500)

    # Display the image
    cv2.imshow("Image Viewer", img)

    # Wait until any key is pressed
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()

    # Display image information
    print("Image Properties")
    print("----------------")
    print(f"Height   : {img.shape[0]} pixels")
    print(f"Width    : {img.shape[1]} pixels")
    print(f"Channels : {img.shape[2]}")