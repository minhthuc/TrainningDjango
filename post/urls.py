from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name = "index"),
    path('<int:post_id>/', v.detail, name = "details"),
    path('create/', v.create, name = 'create'),
]