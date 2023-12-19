from django.urls import path     
from . import views    # le .   indique que le fichier de vues se trouve dans le même répertoire que ce fichier
urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy_session),
    # NINJA BONUS
    path('increm_session', views.increm_sess_two),
    # SENSEI BONUS
    path('specify_increm', views.specify_increment),
]