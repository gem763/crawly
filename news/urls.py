from django.urls import path
from . import views as v

urlpatterns = [
    path('update/', v.update, name='update'),
    path('test/', v.test, name='test'),
]
