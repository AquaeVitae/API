import os 

from celery import shared_task
from deepface import DeepFace
from django.conf import settings

from recommendations.constants import FormSkinDiseasesChoices
from analysis.utils import preprocess_image_to_analysis, predict_wrinkle_level

from .base import analysis_error_handler, PredictTask

@shared_task(bind=True, base=PredictTask)
@analysis_error_handler
def process_wrinkles_facial_analysis(self, instance=None):
    TMP_FILE_PATH = f"{settings.ANALYSIS_STORAGE_FOLDER}/{self.request.id}.{instance.image.path.split('.')[-1]}"
    try:
        preprocess_image_to_analysis(TMP_FILE_PATH, instance.image.path, self.mtcnn_model)
        score = predict_wrinkle_level(TMP_FILE_PATH, self.wrinkles_model)
        return {"prediction_type": FormSkinDiseasesChoices.WRINKLES, "value": score}
    except:
         raise
    finally:
        if os.path.isfile(TMP_FILE_PATH):
            os.remove(TMP_FILE_PATH)

@shared_task(bind=True)
@analysis_error_handler
def process_age_prediction(self, instance=None):
    objs = DeepFace.analyze(img_path = instance.image.path, 
        actions = ['age'],
        detector_backend="mtcnn",
        silent=True
    )
    if not objs:
        raise Exception("No face detected!")
    
    if len(objs) > 1:
        raise Exception("More then one face detected!")
    
    instance.estimated_age = objs[0]["age"]
    instance.save()
