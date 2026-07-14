import cv2


# Function to display an image
def show_image(window_name, img):
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Function to apply the selected filter
def apply_filter(img, choice):

    output = img.copy()

    if choice == "1":
        # Keep only Red channel
        output[:, :, 0] = 0
        output[:, :, 1] = 0

    elif choice == "2":
        # Keep only Green channel
        output[:, :, 0] = 0
        output[:, :, 2] = 0

    elif choice == "3":
        # Keep only Blue channel
        output[:, :, 1] = 0
        output[:, :, 2] = 0

    elif choice == "4":
        # Increase Red
        output[:, :, 2] = cv2.add(output[:, :, 2], 40)

    elif choice == "5":
        # Increase Green
        output[:, :, 1] = cv2.add(output[:, :, 1], 40)

    elif choice == "6":
        # Increase Blue
        output[:, :, 0] = cv2.add(output[:, :, 0], 40)

    elif choice == "7":
        # Decrease Red
        output[:, :, 2] = cv2.subtract(output[:, :, 2], 40)

    elif choice == "8":
        # Decrease Green
        output[:, :, 1] = cv2.subtract(output[:, :, 1], 40)

    elif choice == "9":
        # Decrease Blue
        output[:, :, 0] = cv2.subtract(output[:, :, 0], 40)

    return output


# Function to save the image
def save_output(img):

    file_name = input("Enter the file name: ").strip()

    if file_name == "":
        file_name = "filtered_image"

    cv2.imwrite(f"images/{file_name}.jpg", img)

    print(f"Image saved as images/{file_name}.jpg")


# Main Program
def main():

    image = cv2.imread("images/example.jpg")

    if image is None:
        print("Error: Image not found.")
        return

    while True:

        print("\n===== Color Filter Menu =====")
        print("1. Red Tint")
        print("2. Green Tint")
        print("3. Blue Tint")
        print("4. Increase Red")
        print("5. Increase Green")
        print("6. Increase Blue")
        print("7. Decrease Red")
        print("8. Decrease Green")
        print("9. Decrease Blue")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == "0":
            print("Program Closed.")
            break

        if option not in [str(i) for i in range(1, 10)]:
            print("Invalid choice. Please try again.")
            continue

        result = apply_filter(image, option)

        show_image("Filtered Image", result)

        save = input("Do you want to save this image? (yes/no): ").lower()

        if save == "yes":
            save_output(result)


# Run the program
if __name__ == "__main__":
    main()