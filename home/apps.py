from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    retriever = None

    def ready(self):
        from .utils import create_retriever
        self.retriever = create_retriever()

