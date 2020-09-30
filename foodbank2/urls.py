from django.urls import path, include
from . import views
from rest_framework import routers  #Allows us to create GET and POST requests
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('foodbank', views.FoodBankView)


urlpatterns = [
    path('', include(router.urls)),
]
