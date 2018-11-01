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
    path('lista_workshop_desempenho/', listar_workshop_desempenho, name='listar_workshop_desempenho'),
    path('lista_alunos_workshop/<int:id>/', listar_alunos_desempenho, name='listar_alunos_desempenho'),
    path('desempenho_form/<int:id>', desempenho_update , name='desempenho_form'),
    path('deletar_workshop/<int:id>', workshop_delete, name='deletar_workshop'),
    path('perfil/<int:id>', perfil, name='perfil'),
    path('testedeequipes/', equipes, name='equipe'),


    path('testefrequencia/<int:id>', frequencia_nova, name='frequenciateste'),
    path('frequenciadia/', frequencia_dia, name='frequenciadia'),
    path('frequenciateste2/', frequencia_oquequiser, name='frequenciateste2')
]