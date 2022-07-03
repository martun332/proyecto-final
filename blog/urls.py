from django.urls import include, path
from .views import inicio, nosotros

urlpatterns = [
    path('', inicio, name='pagina_index'),
    path('nosotros/', nosotros, name='pagina_nosotros'),
]