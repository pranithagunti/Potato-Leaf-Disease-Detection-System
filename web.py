import streamlit as st
import tensorflow as tf
import numpy as np

def model_prediction(test_image):
    model= tf.keras.models.load_model("C:/Users/saipr/AICTE-Internship-files/trained_plant_disease_model.keras")
    image= tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr=np.array([input_arr])
    predictions= model.predict(input_arr)
    return np.argmax(predictions)
st.sidebar.title("Plant Disease system for Sustainable Agriculture")
app_mode = st.sidebar.selectbox('select page',['Home','Disease Recognition'])

from PIL import Image
img= Image.open("C:/Users/saipr/AICTE-Internship-files/Diseases.png")
st.image(img)

if(app_mode=='HOME'):
    st.markdown("<h1 style='text-align: center;'>Plant Disease Detection System for Sustainable Agriculture", unsafe_allow_html=True)

elif(app_mode=='Disease Recognition'):
    st.header('Plant Disease Detection System For Sustainable Agriculture')


test_image= st.file_uploader('Choose an image:')
if(st.button('Show Image')):
    st.image(test_image,width=4,use_column_width=True)

if (st.button('Predict')):
    st.snow()
    st.write('our prediction')
    result_index = model_prediction(test_image)
    class_name=['Potato___Early_blight','Potato___Late_blight','Potato___healthy']
    st.success('Model is predicting its a {}'.format(class_name[result_index]))




# import streamlit as st
# import tensorflow as tf
# import numpy as np
# from PIL import Image
# import io
# import os

# # Load Model Function
# def model_prediction(test_image):
#     model_path = "C:/Users/saipr/AICTE-Internship-files/trained_plant_disease_model.keras"
    
#     # Ensure the model file exists
#     if not os.path.exists(model_path):
#         st.error(f"Error: Model file '{model_path}' not found!")
#         return None

#     model = tf.keras.models.load_model(model_path)

#     # Load image from BytesIO
#     image = Image.open(test_image).convert("RGB")
#     image = image.resize((128, 128))

#     # Convert to numpy array
#     input_arr = np.array(image) / 255.0  # Normalize
#     input_arr = np.expand_dims(input_arr, axis=0)  # Add batch dimension

#     predictions = model.predict(input_arr)
#     return np.argmax(predictions)

# # Streamlit App
# st.sidebar.title("Plant Disease System for Sustainable Agriculture")
# app_mode = st.sidebar.selectbox('Select Page', ['Home', 'Disease Recognition'])

# # Display Image at the Top
# img_path = "C:/Users/saipr/AICTE-Internship-files/Diseases.png"
# if os.path.exists(img_path):
#     img = Image.open(img_path)
#     st.image(img, use_column_width=True)
# else:
#     st.error("Error: Image file not found!")

# # Home Page
# if app_mode == 'Home':
#     st.markdown("<h1 style='text-align: center;'>Plant Disease Detection System for Sustainable Agriculture</h1>", unsafe_allow_html=True)

# # Disease Recognition Page
# elif app_mode == 'Disease Recognition':
#     st.header('Plant Disease Detection System For Sustainable Agriculture')

#     # File Uploader
#     test_image = st.file_uploader('Choose an image:', type=['jpg', 'png', 'jpeg'])

#     if test_image is not None:
#         st.image(test_image, use_column_width=True)  # Show uploaded image

#     # Predict Button
#     if st.button('Predict'):
#         if test_image is not None:
#             st.snow()
#             st.write('Our Prediction:')
#             result_index = model_prediction(test_image)

#             if result_index is not None:
#                 class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
#                 st.success(f'Model is predicting: **{class_names[result_index]}**')
#         else:
#             st.warning("Please upload an image first!")
