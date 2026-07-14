# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize pixel values (0-255 → 0-1)
x_train = x_train / 255.0
x_test = x_test / 255.0

# Keep a copy of the original test images for visualization
x_test_images = x_test.copy()

# Flatten images (28x28 → 784)
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

# Data Augmentation
datagen = ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1
)

datagen.fit(x_train)

# Build the Neural Network
model = models.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(128, activation=tf.keras.layers.LeakyReLU(negative_slope=0.1)),
    layers.Dense(64, activation=tf.keras.layers.LeakyReLU(negative_slope=0.1)),
    layers.Dense(10, activation="softmax")
])

# Compile the model
model.compile(
    optimizer="rmsprop",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train the model
model.fit(
    datagen.flow(x_train, y_train, batch_size=32),
    epochs=10
)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test)

print(f"\nTest Accuracy: {test_accuracy:.4f}")

# Make predictions
predictions = model.predict(x_test)

# Display the first test image and prediction
plt.imshow(x_test_images[0], cmap="gray")
plt.title(f"Predicted Digit: {predictions[0].argmax()}")
plt.axis("off")
plt.show()