from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$",views.home, name = "home"),
    url(r"^search/", views.search_movie, name = 'search'),
    url(r"^video/(.+)/$", views.video, name = 'video')
]