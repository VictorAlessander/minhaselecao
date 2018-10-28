from django.urls import path
from .views import *


urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('cadastro/list/', cadastro_list, name='cadastro_list'),
    path('dados/update/<int:id>/', cadastro_update, name='cadastro_update'),
    path('index/', index, name='index'),
    path('formulario/', imersionista_form, name='formulario'),
    path('', home, name='home'),
    path('update/98404834211<int:id>3210983094032740/', imersionista_update, name='atualizar'),
    path('lista/<int:id>/', listar_alunos, name='lista'),
    path('frequencia/', listar_workshop, name='frequencia'),
    path('teste/<int:id>/', presenca, name='presenca'),
    path('users/', usuarios, name='users'),
    path('users/professor/', professor_list, name='professor_list'),
    path('users/professor/<int:id>/', professor_delete, name='professor_delete'),
    path('users/extensionista/', extensionista_list, name='extensionista_list'),
    path('users/extensionista/<int:id>/', extensionista_delete, name='extensionista_delete'),
    path('lista_worshop/', listar_workshop_admin, name='lista_workshop_admin'),
    path('criar_workshop/', criar_workshop, name='criar_workshop'),
]