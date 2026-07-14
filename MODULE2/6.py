import cv2


# Load OpenCV Haar Cascade classifiers
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

eye_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

smile_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)


# Start webcam
camera = cv2.VideoCapture(0)

print("Face Emotion Detector Started")
print("Press 'q' to close")


while True:

    success, image = camera.read()

    if not success:
        print("Unable to access camera")
        break


    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    # Detect faces
    detected_faces = face_detector.detectMultiScale(
        gray_frame,
        scaleFactor=1.2,
        minNeighbors=6,
        minSize=(70, 70)
    )


    for face_x, face_y, face_width, face_height in detected_faces:

        # Extract face area
        face_region_gray = gray_frame[
            face_y:face_y + face_height,
            face_x:face_x + face_width
        ]

        face_region_color = image[
            face_y:face_y + face_height,
            face_x:face_x + face_width
        ]


        # Detect smile
        smile_found = smile_detector.detectMultiScale(
            face_region_gray,
            scaleFactor=1.7,
            minNeighbors=18
        )


        # Detect eyes
        eyes_found = eye_detector.detectMultiScale(
            face_region_gray,
            scaleFactor=1.1,
            minNeighbors=5
        )


        # Decide emotion
        if len(smile_found) > 0:
            status = "Happy"
            box_color = (0, 255, 0)

        elif len(eyes_found) == 0:
            status = "Eyes Closed"
            box_color = (0, 255, 255)

        else:
            status = "Normal"
            box_color = (255, 150, 0)


        # Draw face rectangle
        cv2.rectangle(
            image,
            (face_x, face_y),
            (face_x + face_width, face_y + face_height),
            box_color,
            2
        )


        # Add emotion text
        cv2.putText(
            image,
            status,
            (face_x, face_y - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            box_color,
            2
        )


        # Draw eye detection boxes
        for eye_x, eye_y, eye_w, eye_h in eyes_found:

            cv2.rectangle(
                face_region_color,
                (eye_x, eye_y),
                (eye_x + eye_w, eye_y + eye_h),
                (255, 0, 0),
                2
            )


    # Show number of detected faces
    cv2.putText(
        image,
        "Detected Faces: " + str(len(detected_faces)),
        (10, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )


    # Display output
    cv2.imshow(
        "Live Face Emotion Detection",
        image
    )


    # Exit condition
    if cv2.waitKey(1) == ord("q"):
        break



# Release camera resources
camera.release()
cv2.destroyAllWindows()