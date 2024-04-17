import os
import traceback
from functools import wraps

from keras.saving import load_model
from mtcnn.mtcnn import MTCNN
from celery import shared_task, Task
from django.conf import settings

from analysis.models import FacialAnalysis, Predictions


@shared_task
def set_as_done(*args, analysis_id=None):
    instance = FacialAnalysis.objects.get(id=analysis_id)

    predictions = list()
    error_message = ""

    for prediction in args[0]:
        if not prediction:
            continue

        if isinstance(prediction, str):
            error_message += prediction + "\n"
            continue
        
        predictions.append(Predictions(**prediction, analysis_id=analysis_id))
    
    instance.predictions.bulk_create(predictions)

    updated_fields = ["is_done"]

    if error_message:
        instance.error = error_message
        updated_fields.append("error")

    if not instance.autorized_to_store and instance.image:
        instance.image.delete(save=False)
        updated_fields.append("image")

    instance.is_done=True
    instance.save(update_fields=updated_fields)


def analysis_error_handler(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        analysis_id = kwargs.pop("analysis_id") 
        if not analysis_id:
            raise Exception("Analysis Tasks should have an analysis id!")
        instance = FacialAnalysis.objects.get(id=analysis_id)

        try:
            return func(self, instance=instance, *args, **kwargs)

        except Exception:
            error_message = f"{self.name}-{traceback.format_exc()}"
            return error_message

    return wrapper


class PredictTask(Task):
    abstract = True

    def __init__(self):
        super().__init__()
        self.mtcnn_model = None
        self.wrinkles_model = None

    def __call__(self, *args, **kwargs):
        try:
            if not self.mtcnn_model:
                self.mtcnn_model = MTCNN()

            if not self.wrinkles_model:
                self.wrinkles_model = load_model(os.path.join(settings.ML_MODELS_PATH, settings.WRINKLES_MODEL))
        except:
            pass

        return self.run(*args, **kwargs)
