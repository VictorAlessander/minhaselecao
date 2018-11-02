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

# DEF PARA EDITAR DESEMPENHO DO IMERCIONISTA

@login_required()
def desempenho_update(request, id):
    extensionista = get_object_or_404(Extensionista, pk=id)
    aluno = Extensionista.objects.filter(id_extensionista=id)
    aluno2 = Extensionista.objects.get(id_extensionista=id)
    form = DesmepenhoForm(request.POST or None, request.FILES or None, instance=extensionista)

    if form.is_valid():
        form.save()
        return redirect('listar_workshop_desempenho')

    return render(request, 'desempenho_form.html', {'form': form, 'aluno':aluno, 'aluno2':aluno2})

@login_required()
def listar_alunos_desempenho(request, id):
    aluno = Extensionista.objects.filter(workshop_extensionista=id)
    workshop = get_object_or_404(Workshop, pk=id)

    return render(request, 'lista_alunos_desempenho.html', {'aluno': aluno, 'workshop': workshop})

@login_required()
def listar_workshop_desempenho(request):
    workshop = Workshop.objects.all
    return render(request, 'listar_workshop_desempenho.html', {'workshop': workshop})


# DEF QUE LISTA OS ALUNOS PELA SUA ESCOLHA DE WORKSHOP

@login_required()
def listar_alunos(request, id):
    aluno = Extensionista.objects.filter(workshop_extensionista=id)
    workshop = get_object_or_404(Workshop, pk=id)
    #frequencias = FrequenciaWorkshop.objects.filter(frequencia_extensionista__workshop_extensionista=id)
    #frequenciaWorkshopForm = FrequenciaWorkshopForm(request.POST or None, request.FILES or None)

    return render(request, 'lista_alunos.html', {'aluno': aluno, 'workshop': workshop})
    #return render(request, 'lista_alunos.html', {'frequencias': frequencias, 'frequenciaWorkshopForm': frequenciaWorkshopForm})


# DEF QUE LISTA OS WORKSHOPS NA DASHBOARD DO SISTEMA

@login_required()
def listar_workshop(request):
    workshop = Workshop.objects.all
    return render(request, 'frequencia.html', {'workshop': workshop})

# DEF QUE HABILITA A LISTA DE PRESENÇA

@login_required()
def presenca(request, id):
    presenca = get_object_or_404(Extensionista, pk=id)
    aluno = Extensionista.objects.filter(id_extensionista=id)
    form = FrequenciaForm(request.POST or None, request.FILES or None, instance=presenca)

    if form.is_valid():
        form.save()
        return redirect('frequencia')
    return render(request, '1.html', {'form': form, 'aluno':aluno})

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
        return redirect('lista_workshop_admin')

    return render(request, 'extensionista_delete_confirm.html', {'workshop': workshop})


# DEF PARA VISUALIZAÇÃO DO PERFIL

@login_required()
def perfil(request, id):
    veterano = UserCadastro.objects.get(pk=id)
    aluno = UserCadastro.objects.filter(id=id)

    return render(request, 'perfil.html', {'veterano':veterano, 'aluno':aluno})


def frequencia_nova(request, id):
    alunos = FrequenciaWorkshop.objects.all()
    dias = [{
        'nome': 'segunda',
        'id': 1
    },
        {
            'nome': 'terca',
            'id': 2
        },
        {
            'nome': 'quarta',
            'id': 3
        }]

    diatarget = None
    for dia in dias:
        if dia['id'] == id:
            diatarget = dia


    return render(request, 'frequencia_teste_2.html', {'alunos':alunos, 'dia': diatarget})

def frequencia_dia(request):
    dias = [{
        'nome': 'segunda',
        'id': 1
    },
        {
            'nome': 'terca',
            'id': 2
        },
        {
            'nome': 'quarta',
            'id': 3
        }]

    return render(request, 'frequencia_dia.html', {'dias': dias})


def frequencia_oquequiser(request):

    if request.method == 'POST':
        dia = request.POST.get('dia');
        alunos = request.POST.getlist('alunos')[0];
        print(dia)
        for aluno in alunos:
            print(aluno)
            # alunotarget = FrequenciaWorkshop.objects.filter(frequencia_extensionista=aluno['nome'])
            # alunotarget[dia] = aluno.frequencia
            # alunotarget.save();
            # print(alunotarget)


def equipes(resquest):
    workshopsFilterTrue = {}
    workshopsFilterFalse = {}

    alunos = Extensionista.objects.all()
    workshops = Workshop.objects.all()

    for workshop in workshops:
        if workshop.nome_workshop:
            workshopsFilterTrue[workshop.nome_workshop] = []
            workshopsFilterFalse[workshop.nome_workshop] = []

    for aluno in alunos:
        workshop = aluno.workshop_extensionista.nome_workshop
        if aluno.desempenho == True:
            workshopsFilterTrue[workshop].append(aluno)
        else:
            workshopsFilterFalse[workshop].append(aluno)

    print(workshopsFilterTrue)
    print(workshopsFilterFalse)


    azul = workshopsFilterTrue[workshop]
    print(azul)


    for i in workshopsFilterTrue:
        print(i)

    for j in azul:
        print(j)

    return render(resquest, 'equipe.html', {'workshopsFilterTrue':workshopsFilterTrue, 'workshopsFilterFalse':workshopsFilterFalse, 'alunos':alunos, 'i':i})







