# MNIST Digit Recognizer 🖼️

## Description  
This app uses a pre-trained **TensorFlow Keras model** to recognize handwritten digits from images uploaded by the user. The model is trained on the **MNIST dataset**, which contains images of handwritten digits from 0 to 9.

## Features  
- **Image Upload**: Users can upload an image of a handwritten digit (PNG, JPG, or JPEG).  
- **Digit Prediction**: The app predicts the digit in the image using the pre-trained model.  
- **Real-time Results**: Once an image is uploaded and the "Predict" button is pressed, the app displays the predicted digit.

## Installation  
To run the application locally, follow these steps:

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/mnist-digit-recognizer.git
   cd mnist-digit-recognizer
Install the required dependencies:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py


Input Features
The app requires the following input:

Image of Handwritten Digit: Upload an image of a handwritten digit (0-9) in PNG, JPG, or JPEG format.
Model Details
The model used in this app is a Convolutional Neural Network (CNN) trained on the MNIST dataset, which consists of grayscale images of handwritten digits. The app processes the uploaded image, resizes it to the required input size, and then feeds it to the model for prediction.

Image Preprocessing
The image is resized to 28x28 pixels.
The image is converted to grayscale (if not already).
The pixel values are normalized to a range of 0 to 1.
Files
app.py: Main application file for the Streamlit app.
dig_model.keras: Pre-trained TensorFlow Keras model for digit recognition.
requirements.txt: List of Python dependencies.
Dependencies
Streamlit
TensorFlow
Pillow
NumPy
Install them using:
pip install streamlit tensorflow pillow numpy

Example Usage
Upload an image of a handwritten digit (from 0 to 9).
Click the "Predict" button.
The app will display the predicted digit.
Screenshots
Here’s how the app looks:

Author
👨‍💻 Nader Nageh Mansour
Email: nadernageh22508@gmail.com
GitHub: [Your GitHub Profile](https://github.com/nader108)
License
This project is licensed under the MIT License.
Feel free to use it, modify it, and share it.


