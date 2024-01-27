from django.urls import path

from .views import home_page, article, images

urlpatterns = [
    path('', home_page, name="home_page"),
    path('article/<int:id>/', article, name="article"),
    path('images', images, name="images")
]