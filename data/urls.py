from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('upload', upload, name='upload'),
    path('filelist', file_list, name='file_list'),
    path('file', file_download, name='file'),
]
