from django.urls import path
from . import views
from django.views.generic import TemplateView

# URLConf
urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'))
]
