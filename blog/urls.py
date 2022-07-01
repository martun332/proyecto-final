from django.urls import include, path
from .views import inicio, nosotros

urlpatterns = [
    path('', inicio),
    path('nosotros/', nosotros),
]