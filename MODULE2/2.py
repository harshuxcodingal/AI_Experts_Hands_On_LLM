import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread("example.jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Image not found.")

else:
    # ---------------- RGB Conversion ----------------
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(6, 6))
    plt.imshow(rgb_img)
    plt.title("Original Image (RGB)")
    plt.axis("off")
    plt.show()

    # ---------------- Grayscale Conversion ----------------
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plt.figure(figsize=(6, 6))
    plt.imshow(gray_img, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")
    plt.show()

    # ---------------- Crop the Image ----------------
    # Crop from row 50 to 250 and column 100 to 350
    cropped_img = img[50:250, 100:350]

    cropped_rgb = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(5, 5))
    plt.imshow(cropped_rgb)
    plt.title("Cropped Image")
    plt.axis("off")
    plt.show()