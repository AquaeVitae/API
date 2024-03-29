import traceback
from functools import wraps

from celery import shared_task
from analysis.models import FacialAnalysis


def analysis_error_handler(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception:
            analysis_id = kwargs.get("analysis_id") 
            if not analysis_id:
                raise Exception("Analysis Tasks should have an analysis id!")
            
            instance = FacialAnalysis.objects.get(id=analysis_id)
            error_message = f"{self.name}-{traceback.format_exc()}"
            instance.error = instance.error + "\n" + error_message  if instance.error else error_message
            instance.save(update_fields=["error"])

    return wrapper

@shared_task(bind=True)
@analysis_error_handler
def process_wrinkles_facial_analysis(self, analysis_id=None):
    instance = FacialAnalysis.objects.get(id=analysis_id)
    return "Done sending mails"

@shared_task
def set_as_done(*args, analysis_id=None):
    instance = FacialAnalysis.objects.get(id=analysis_id)
    if not instance.autorized_to_store and instance.image:
        instance.image.delete(save=False)

    instance.is_done=True
    instance.save(update_fields=["is_done", "image"])
