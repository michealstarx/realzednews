from django.urls import path

from .views import home_page, article, images, hottest

urlpatterns = [
    path('', home_page, name="home_page"),
    path('article/<int:id>/', article, name="article"),
    path('hot/<int:id>/', hottest, name="hot"),
    path('images', images, name="images")
]