from django.contrib import admin
from django.urls import path
from blog.views import main_page, about_page, post_page, reviews_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home'),
    path('about/', about_page, name='about'),
    path('post/', post_page, name='post'),
    path('reviews/', reviews_page, name='reviews'),
]