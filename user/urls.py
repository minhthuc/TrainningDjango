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
    path('role/', v.role_index, name='role_index'),
    path('role/create/', v.create_role, name='create_role'),
    path('role/<int:role_id>', v.detail_role, name='role_detail'),
    path('getrole/', v.get_choice_field_role),
    path('search/', v.search),
    path('add_user_to_role/', v.add_user_to_role),
]