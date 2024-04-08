import matplotlib.pyplot as plt
import numpy as np
from skimage import io
import mediapipe as mp
import cv2
import math
import os
import keras
import tensorflow as tf
from PIL import Image, ImageDraw

from django.conf import settings


model_path =  os.path.join( settings.ML_MODELS_PATH, settings.MP_LANDMARK_MODEL)  

BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE, output_face_blendshapes=True)


def crop_facebox(result_list, pixels):
    result = result_list[0]
    x, y, width, height = result['box']
    croped = pixels[y:y+height, x:x+width].copy()
    return croped

def _normalized_to_pixel_coordinates(
        normalized_x: float, normalized_y: float, image_width: int,
        image_height: int):
    x_px = min(math.floor(normalized_x * image_width), image_width - 1)
    y_px = min(math.floor(normalized_y * image_height), image_height - 1)
    return x_px, y_px

def crop_forehead(image, landmarks):
    image_rows, image_cols, _ = image.shape

    landmark_left = landmarks[68] #251
    landmark_right = landmarks[298] #251
    x_left, y_left = _normalized_to_pixel_coordinates(landmark_left.x, landmark_left.y, image_cols, image_rows ) 
    x_right, y_right = _normalized_to_pixel_coordinates(landmark_right.x, landmark_right.y, image_cols, image_rows ) 

    y = max(y_left, y_right)

    cropped_image = image[0:y, x_left + 10:x_right-10 ].copy()

    return cropped_image

def preprocess_image_to_analysis(tmp_file_path, img_path, detector):
    GENERAL_BRIGHT_MEAN = 44.11764705882353

    pixels = io.imread(img_path, plugin='matplotlib')[:,:,:3]
    faces = detector.detect_faces(pixels)
    croped = crop_facebox(faces, pixels)
    nd_img = croped
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data= np.asarray(nd_img.copy()))
    
    with FaceLandmarker.create_from_options(options) as landmarker:
        face_landmarker_result = landmarker.detect(mp_image)
    
    cropped_img = crop_forehead(nd_img, face_landmarker_result.face_landmarks[0])
    
    resized = cv2.resize(cropped_img, (200, 80))

    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    avg = np.mean(hsv[:,:, 2])
    per = (avg/255)*100

    for a in hsv:
        for b in a:
            current_per = (b[2]/255)*100
            updated = ((current_per) * GENERAL_BRIGHT_MEAN) / per

            b[2] = (b[2]*updated)/current_per

    adjusted_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    grayscale_image = cv2.cvtColor(adjusted_img, cv2.COLOR_RGB2GRAY)
    plt.imsave(tmp_file_path, grayscale_image, cmap='gray')

    open_img=Image.open(tmp_file_path).convert("RGB")


    h,w=open_img.size
    alpha = Image.new("L", open_img.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.ellipse((0, 15, h, w-5),
                    fill=255)

    open_img.putalpha(alpha)
    open_img = open_img.crop((0, 15, h, w-5))
    open_img = open_img.convert("RGBA")

    background = Image.new("RGBA", open_img.size, (255, 255, 255, 255))
    
    filled_image = Image.alpha_composite(background, open_img)
    filled_image = filled_image.convert("RGB")

    filled_image.save(tmp_file_path)


def predict_wrinkle_level(tmp_file_path, saved_model):
    img_load = keras.utils.load_img(
            tmp_file_path, target_size=[60, 200]
        )

    img_array = keras.utils.img_to_array(img_load)
    img_array = tf.expand_dims(img_array, 0)

    predictions = saved_model.predict(img_array)
    score = float(predictions[0])
    return score
