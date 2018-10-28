from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# @login_required é a TAG que habilita a autorização, na def que ela estiver, a def só pode ser acessada por usuarios autenticados

# DEF QUE DA ACESSO A HOEMPAGE

def home(request):
    form = ExtensionistaBuscarForm
    queryset = None
    erro = None

    if request.method == 'POST':
        form = ExtensionistaBuscarForm(request.POST or None)

        if form.is_valid():
            matricula = request.POST['matricula_extensionista']

            try:
                queryset = Extensionista.objects.get(matricula_extensionista=str(matricula))
                return redirect('atualizar', id=queryset.id_extensionista)
            except ObjectDoesNotExist:
                erro = 'Matrícula não encontrada'

    return render(request, 'home.html',  {'form': form, 'erro': erro})


# DEF QUE HABILITA O CADASTRO NO PROJETO

def cadastro(request):
    form = ColaboradorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'cadastro_form.html', {'form': form})

# DEF QUE MOSTRA OS CADASTRO PARA SEREM EDITADOS

@login_required()
def cadastro_list(request):
    extensionista = Extensionista.objects.all()
    return render(request, 'cadastro_list.html', {'extensionista': extensionista})

# DEF DE EDICAO DE CADASTRO

@login_required()
def cadastro_update(request, id):
    extensionista = get_object_or_404(Extensionista, pk=id)
    form = ExtensionistaEditForm(request.POST or None, request.FILES or None, instance=extensionista)
    if form.is_valid():
        form.save()
        return redirect('cadastro_list')

    return render(request, 'cadastro_teste.html', {'form': form})


# DEF QUE DA ACESSO A DASHBOARD PRINCIPAL

@login_required()
def index(request):
    usuario = UserCadastro.objects.all()
    return render(request, 'index.html', {'usuario': usuario})

# DEF QUE DA ACESSO AO FORMULARIO DO IMERCIONISTA

def imersionista_form(request):
    form = ExtensionistaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'extensionista_form.html', {'form': form})

# DEF QUE DA ACESSO AO IMERCIONISTA EDITAR SEU CADASTRO

def imersionista_update(request, id):
    extensionista = get_object_or_404(Extensionista, pk=id)
    form = ExtensionistaForm(request.POST or None, request.FILES or None, instance=extensionista)
    if form.is_valid():
        form.save()
        extensionista.criarFrequenciaWorkshop(extensionista)
        return redirect('login')

    return render(request, 'extensionista_form.html', {'form': form})

# DEF QUE LISTA OS ALUNOS PELA SUA ESCOLHA DE WORKSHOP

@login_required()
def listar_alunos(request, id):
    #aluno = Extensionista.objects.filter(workshop_extensionista=id)
    #workshop = get_object_or_404(Workshop, pk=id)
    frequencias = FrequenciaWorkshop.objects.filter(frequencia_extensionista__workshop_extensionista=id)
    frequenciaWorkshopForm = FrequenciaWorkshopForm(request.POST or None)

    #return render(request, 'lista_alunos.html', {'aluno': aluno, 'workshop': workshop})
    return render(request, 'lista_alunos.html', {'frequencias': frequencias, 'frequenciaWorkshopForm': frequenciaWorkshopForm})


# DEF QUE LISTA OS WORKSHOPS NA DASHBOARD DO SISTEMA

@login_required()
def listar_workshop(request):
    workshop = Workshop.objects.all
    return render(request, 'frequencia.html', {'workshop': workshop})

# DEF QUE HABILITA A LISTA DE PRESENÇA

@login_required()
def presenca(request, id):
    presenca = get_object_or_404(FrequenciaWorkshop, pk=id)
    form = FrequenciaWorkshopForm(request.POST or None, request.FILES or None, instance=presenca)

    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, '1.html', {'form': form})

# DEF QUE EDITA O IMERSIONISTA E CRIA UMA ID EM FREQUENCIA


def imersionista_update_teste(request, id):
    extensionista = get_object_or_404(Extensionista, pk=id)
    form = ExtensionistaForm(request.POST or None, request.FILES or None, instance=extensionista)
    # form2 = FrequenciaForm(request.POST or None)
    # if form.is_valid() and form2.is_valid():
    if form.is_valid():


        imersionista_criado = form.save()
        # id_frequencia = imersionista_criado.pk
        #frequencia_extensionista = imersionista_criado.pk

        # imersionista_membro = form2.save(commit=False)
        # imersionista_membro.frequencia = Frequencia(pk=id_frequencia)
       # imersionista_membro.frequencia = Frequencia(pk=frequencia_extensionista)

        # imersionista_membro.save()

        return redirect('login')
    # return render(request, 'extensionista_form.html', {'form': form}, {'form2': form2})
    return render(request, 'extensionista_form.html', {'form': form})


# PAGINA QUE MOSTRA OS USUARIOS CADASTRADOS

@login_required()
def usuarios(request):
    return render(request, 'users.html')

# DEF QUE MOSTRA OS PROFESSORES CADASTRADOS

@login_required()
def professor_list(request):
    users = UserCadastro.objects.all()

    return render(request, 'professor_list.html', {'users': users})

# DEF QUE DELETA OS PROFESSORES CADASTRADOS

@login_required()
def professor_delete(request, id):
    users = get_object_or_404(UserCadastro, pk=id)
    form = ColaboradorForm(request.POST or None, request.FILES or None, instance=users)

    if request.method == 'POST':
        users.delete()
        return redirect('professor_list')

    return render(request, 'professor_delete_confirm.html', {'users':users})

# DEF QUE MOSTRA OS EXTENSIONISTA CADASTRADOS

@login_required()
def extensionista_list(request):
    extensionista = Extensionista.objects.all()

    return render(request, 'extensionista_list.html', {'extensionista': extensionista})

# DEF QUE DELETA OS EXTENSIONISTAS CADASTRADOS

@login_required()
def extensionista_delete(request, id):
    extensionista = get_object_or_404(Extensionista, pk=id)
    form = ExtensionistaForm(request.POST or None, request.FILES or None, instance=extensionista)

    if request.method == 'POST':
        extensionista.delete()
        return redirect('extensionista_list')

    return render(request, 'extensionista_delete_confirm.html', {'extensionista': extensionista})



# DEF PARA CRIAR WORKSHOP


@login_required()
def criar_workshop(request):
    form = WorkshopForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_workshop_admin')
    return render(request, 'criar_workshop.html', {'form': form})


# DEF PARA LISTAR WORKSHOPS

@login_required()
def listar_workshop_admin(request):
    workshop = Workshop.objects.all
    return render(request, 'lista_workshop.html', {'workshop': workshop})

# DEF PARA DELETAR WORKSHOP

@login_required()
def workshop_delete(request, id):
    workshop = get_object_or_404(Workshop, pk=id)
    form = WorkshopForm(request.POST or None, request.FILES or None, instance=workshop)

    if request.method == 'POST':
        workshop.delete()
        return redirect('workshop_list')

    return render(request, 'extensionista_delete_confirm.html', {'workshop': workshop})