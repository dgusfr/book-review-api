from celery import Celery

c_app = Celery("bookly")
c_app.config_from_object("src.core.config")
