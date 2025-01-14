"""musician_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# πχ1 Αν ο χρήστης κάνει search "admin" τότε πήγαινέ τον στο admin.site.urls

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from users_core import views as user_view


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('user/', include('users_core.urls')),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('profile/', user_view.profile, name='profile'),
    path('upload/', user_view.upload, name='upload'),
    path('song_list/', user_view.composition_list, name='song_list'),
    path('song_list/upload', user_view.upload_song, name='upload_song'),
    path('lyrics_list/',user_view.lyrics_list, name='lyrics_list'),
    path('lyrics_list/upload', user_view.upload_lyrics, name='upload_lyrics'),
    path('search/', user_view.profile_search, name='profile_search'),
    path('profile/<int:prof_id>', user_view.profile_appearance, name='profile_appearance'),
    path('messages/', include('postman.urls')),
    path('song_delete/<int:song_id>', user_view.song_delete, name='song_delete'),
    path('lyric_delete/<int:lyric_id>',  user_view.lyric_delete, name='lyric_delete'),
    path('song_list/<int:prof_id>', user_view.other_composition_list, name='other_song_list'),
    path('lyrics_list/<int:prof_id>', user_view.other_lyrics_list, name='other_lyrics_list'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# path('music/', include('music_up_down_load.urls'), name='music_up_down_load'),
