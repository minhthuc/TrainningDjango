from django.urls import path
from . import views as v

app_name = 'user'
urlpatterns = [
    path('', v.index, name = "index"),
    path('<int:user_id>/', v.detail, name = "details"),
    path('create/', v.create, name = 'create'),
    path('getUser/', v.getUser, name = 'getUser'),
    path('<int:user_id>/update/',v.update, name = 'update'),
    path('<int:user_id>/delete/', v.delete, name = 'delete'),

    #Role path
    path('role/', v.role_index, name = 'role_index'),
    path('role/getrole/', v.get_choice_field_role, name='get_role'),
]