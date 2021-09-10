from django.conf.urls import url
from .import views

urlpatterns = [
    url(r"home/$", views.index),
    url(r"education/$", views.education),
    url(r"career/$", views.career),
    url(r'contact-us/$', views.contact_us),
    url(r'about/$', views.about),
    
]