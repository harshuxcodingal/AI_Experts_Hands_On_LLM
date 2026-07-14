import cv2
import matplotlib.pyplot as plt


# Function to display an image
def show_image(title, img):

    plt.figure(figsize=(6, 6))

    if len(img.shape) == 2:
        plt.imshow(img, cmap="gray")
    else:
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(rgb)

    plt.title(title)
    plt.axis("off")
    plt.show()


# Load the image
def load_image(path):

    img = cv2.imread(path)

    if img is None:
        print("Error: Unable to load the image.")
        return None

    return img


# Sobel Edge Detection
def sobel_edge(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = int(input("Enter Sobel Kernel Size (Odd Number): "))

    x_edge = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=kernel)
    y_edge = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=kernel)

    result = cv2.addWeighted(
        cv2.convertScaleAbs(x_edge),
        0.5,
        cv2.convertScaleAbs(y_edge),
        0.5,
        0
    )

    show_image("Sobel Edge Detection", result)


# Canny Edge Detection
def canny_edge(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    lower = int(input("Enter Lower Threshold: "))
    upper = int(input("Enter Upper Threshold: "))

    edges = cv2.Canny(gray, lower, upper)

    show_image("Canny Edge Detection", edges)


# Laplacian Edge Detection
def laplacian_edge(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    lap = cv2.Laplacian(gray, cv2.CV_64F)

    result = cv2.convertScaleAbs(lap)

    show_image("Laplacian Edge Detection", result)


# Gaussian Blur
def gaussian_blur(img):

    kernel = int(input("Enter Gaussian Kernel Size (Odd Number): "))

    blur = cv2.GaussianBlur(img, (kernel, kernel), 0)

    show_image("Gaussian Blur", blur)


# Median Blur
def median_blur(img):

    kernel = int(input("Enter Median Kernel Size (Odd Number): "))

    blur = cv2.medianBlur(img, kernel)

    show_image("Median Blur", blur)


# Main Menu
def main():

    image = load_image("images/example.jpg")

    if image is None:
        return

    while True:

        print("\n===== Image Processing Menu =====")
        print("1. Sobel Edge Detection")
        print("2. Canny Edge Detection")
        print("3. Laplacian Edge Detection")
        print("4. Gaussian Blur")
        print("5. Median Blur")
        print("6. Show Original Image")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sobel_edge(image)

        elif choice == "2":
            canny_edge(image)

        elif choice == "3":
            laplacian_edge(image)

        elif choice == "4":
            gaussian_blur(image)

        elif choice == "5":
            median_blur(image)

        elif choice == "6":
            show_image("Original Image", image)

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()