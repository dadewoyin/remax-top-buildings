from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.home_page, name="home_page"),
    url(r"^about-us/$", views.about_page, name="about_page"),
    url(r"^blog/$", views.blog_page, name="blog_page"),
    url(r"^nyc-neighborhoods/$", views.neighborhoods_page, name="neighborhoods_page"),
]