from django.urls import path

from . import views
app_name = 'pol'
urlpatterns = [
    # ex: /polls/
    path('', views.home_view, name='index'),
]