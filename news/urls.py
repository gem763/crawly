from django.urls import path
from . import views as v

urlpatterns = [
    path('update/', v.update, name='update'),
    path('newscrawl_and_bigquerize/', v.newscrawl_and_bigquerize, name='newscrawl_and_bigquerize'),
    path('test/', v.test, name='test'),
]
