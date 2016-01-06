from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.home_page, name="home_page"),
    url(r"^about-us/$", views.about_page, name="about_page"),
    url(r"^blog/$", views.blog_page, name="blog_page"),
    url(r"^nyc-neighborhoods/$", views.neighborhoods_page, name="neighborhoods_page"),
    url(r"^neighborhoods/(?P<neighborhood>.*)$", views.show_neighborhood, name="show_neighborhood"),
    url(r"^top/$", views.top_buildings_main, name="top_buildings_main"),
    url(r"top/(?P<neighborhood>.*)$", views.show_top_buildings, name="show_top_buildings"),
]