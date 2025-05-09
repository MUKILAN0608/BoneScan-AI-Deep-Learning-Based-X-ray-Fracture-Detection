import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.callbacks import ModelCheckpoint

# Load dataset
train_dir = r'C:\Users\Mukil\2nd year intership Bone reconstruction\Bone Fracture Dataset\training'
test_dir = r'C:\Users\Mukil\2nd year intership Bone reconstruction\Bone Fracture Dataset\testing'

datagen = ImageDataGenerator(rescale=1./255)

# Training data generator
train_generator = datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    color_mode='grayscale',
    shuffle=True
)

# Testing data generator (for validation or evaluation)
test_generator = datagen.flow_from_directory(
    test_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    color_mode='grayscale',
    shuffle=False
)

# Define the CNN model
model = Sequential([
    tf.keras.layers.Input(shape=(224, 224, 1)),
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),

    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train model with validation data
history = model.fit(
    train_generator,
    epochs=10,
    validation_data=test_generator  # validate on test set during training
)

# Save model in SavedModel format
model.save('bone_fracture_model')
