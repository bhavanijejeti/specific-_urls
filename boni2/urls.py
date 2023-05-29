from django.urls import path
from boni2.views import *
app_name='reddy'
urlpatterns=[
    path('specific2/',specific2, name='specific2'),
]