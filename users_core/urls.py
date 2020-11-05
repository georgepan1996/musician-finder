
from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'users_core'

urlpatterns = [
    path('signup/', views.signup, name='signup'),

]