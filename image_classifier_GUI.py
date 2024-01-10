import cv2
import numpy as np
import tensorflow as tf

# Load your pre-trained model
model = tf.keras.models.load_model('model_99')

# Function to preprocess the image
def preprocess_image(image):
    # This needs to be adjusted according to your model's input requirements
    processed_image = cv2.resize(image, (256, 256))  # Example resize to 224x224
    processed_image = processed_image / 255.0  # Normalize
    return processed_image

# Initialize camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Display the captured frame
        cv2.imshow('Feldhase vs Kaninchen', frame)

        # Preprocess the image
        processed_frame = preprocess_image(frame)

        # Add batch dimension and make prediction
        prediction = model.predict(np.expand_dims(processed_frame, axis=0))

        # Classify and print result
        # Modify this depending on how your model outputs predictions
        classification = 'Feldhase' if prediction[0][0] > 0.5 else 'Kaninchen'
        print(f'Classification: {classification}')

        # Break the loop with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()

#%%
