from django.urls import path

from devpro.core import views
# Pode ser from *

app_name = 'core'
urlpatterns = [
    path('authors/', views.authors, name='list-authors')
]
