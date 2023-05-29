from django.urls import path
from boni1.views import *
app_name='bhavani'
urlpatterns=[
    path('specific1/',specific1,name='specific1'),
]

