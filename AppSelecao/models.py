from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# ESCOLHA DE CURSOS

C1 = 'Gestão da Tecnologia da Informação'
C2 = 'Ciência da Computação'
C3 = 'Sistemas para Internet'
C4 = 'Redes de Computadores'
C5 = 'Análise e Desenvolvimento de Sistemas'
CURSO = (
    (C1, 'Gestão da Tecnologia da Informação'),
    (C2, 'Ciência da Computação'),
    (C3, 'Sistemas para Internet'),
    (C4, 'Redes de Computadores'),
    (C5, 'Análise e Desenvolvimento de Sistemas'),
)

# ESCOLHA DE PERIODO

P1 = '1º'
P2 = '2º'
P3 = '3º'
P4 = '4º'
P5 = '5º'
P6 = '6º'
P7 = '7º'
P8 = '8º'
PERIODO = (
    (P1, '1º'),
    (P2, '2º'),
    (P3, '3º'),
    (P4, '4º'),
    (P5, '5º'),
    (P6, '6º'),
    (P7, '7º'),
    (P8, '8º'),
)


# ESCOLHA DE INTERESSE
# ESCOLHA DE PERIODO

I1 = '1'
I2 = '2'
I3 = '3'
I4 = '4'
I5 = '5'
INTERESSE = (
    (I1, '1'),
    (I2, '2'),
    (I3, '3'),
    (I4, '4'),
    (I5, '5'),
)

# MODELO DE USUARIO DO PROJETO

class UserCadastro(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    username = models.CharField(max_length=30, unique=True, name='username', blank=True, null=True)
    matricula = models.CharField(max_length=10, unique=True, verbose_name='Matrícula')
    email = models.EmailField(max_length=254, unique=True, verbose_name='E-mail')
    first_name = models.CharField(max_length=50, verbose_name='Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')


    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = ['username', 'email', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        managed = True
        db_table = 'usercadastro'


# MODELO PARA CRIAÇAO DE WORKSHOPS

class Workshop(models.Model):
    id_workshop = models.AutoField(primary_key=True, unique=True, null=False)
    nome_workshop = models.CharField(max_length=100, null=True, verbose_name='Tema Workshop')

    def __str__(self):
        return self.nome_workshop

    class Meta:
        managed = True
        db_table = 'workshop'

# MODELO PARA EXTENSIONISTA

class Extensionista(models.Model):
    id_extensionista = models.AutoField(primary_key=True, unique=True, null=False)
    nome_completo = models.CharField(max_length=100, null=True, verbose_name='Nome completo')
    telefone = models.CharField(max_length=11, null=True, verbose_name='Telefone/Celular')
    email = models.EmailField(max_length=100, null=True, verbose_name='E-mail')
    matricula_extensionista = models.CharField(max_length=10, null=True, verbose_name='Matrícula')
    curso = models.CharField(max_length=100, null=True, choices=CURSO)
    periodo = models.CharField(max_length=100, null=True, choices=PERIODO)
    habilidade_dominio = models.TextField(max_length=200, null=True, verbose_name='Cite duas habilidades que você domina')
    habilidade_aprendizado = models.TextField(max_length=200, null=True, verbose_name='Cite duas habilidades que gostaria de aprender')
    experiencia_profissional = models.TextField(max_length=200, null=True, verbose_name='Resuma sua experiência profissional')
    outras_habilidades = models.TextField(max_length=200, null=True, verbose_name='Cite outras habilidades profissionais')
    workshop_extensionista = models.ForeignKey(Workshop, on_delete=models.CASCADE, null=True)
    interesse_1 = models.CharField(max_length=200, verbose_name='Gerente de Projetos', null=True)
    interesse_2 = models.CharField(max_length=200, verbose_name='Analista de Requesitos', null=True)
    interesse_3 = models.CharField(max_length=200, verbose_name='Desenvolvedor Front-End', null=True)
    interesse_4 = models.CharField(max_length=200, verbose_name='Desenvolvedor Back-End', null=True)
    interesse_5 = models.CharField(max_length=200, verbose_name='Administrador de Banco de Dados', null=True)
    interesse_6 = models.CharField(max_length=200, verbose_name='Desenvolvedor de Jogos', null=True)
    interesse_7 = models.CharField(max_length=200, verbose_name='Desenvolvedor de Jogos / Artista 2D, 3D', null=True)
    interesse_8 = models.CharField(max_length=200, verbose_name='Desenvolvedor de Jogos / Designer de Interface', null=True)
    interesse_9 = models.CharField(max_length=200, verbose_name='Engenheiro de Qualidade e Testes', null=True)
    interesse_10 = models.CharField(max_length=200, verbose_name='Gerente de Configuração e Infra Estrutura', null=True)
    interesse_11 = models.CharField(max_length=200, verbose_name='Administrador de Redes', null=True)
    interesse_12 = models.CharField(max_length=200, verbose_name='Analista de Testes', null=True)
    interesse_13 = models.CharField(max_length=200, verbose_name='Automatizador de Teste', null=True)
    interesse_14 = models.CharField(max_length=200, verbose_name='Testador', null=True)
    interesse_15 = models.CharField(max_length=200, verbose_name='Desenvolvedor de Chatboot', null=True)
    interesse_16 = models.CharField(max_length=200, verbose_name='Analista de Dados e Business Intelligence', null=True)
    espera_1 = models.CharField(max_length=200, verbose_name='Desenvolvimento Profissional', null=True)
    espera_2 = models.CharField(max_length=200, verbose_name='Desenvolver uma ideia empreendedora', null=True)
    espera_3 = models.CharField(max_length=300, verbose_name='Montar um Negócio', null=True)
    espera_4 = models.CharField(max_length=200, verbose_name='Adquirir Prática', null=True)
    espera_5 = models.CharField(max_length=200, verbose_name='Vivenciar Trabalho em Equipe', null=True)
    espera_6 = models.CharField(max_length=200, verbose_name='Conhecer como Funciona um Ambiente Empresarial', null=True)
    espera_7 = models.CharField(max_length=200, verbose_name='Ampliar meu Networking', null=True)
    espera_8 = models.CharField(max_length=200, verbose_name='Participar de Produção Científica', null=True)
    desempenho = models.BooleanField(null=True, default=False, verbose_name='Destaque')
    comentario = models.TextField(max_length=1000, verbose_name='Comentário')
    segunda = models.BooleanField(null=True, verbose_name='Segunda-Feira')
    terca = models.BooleanField(null=True, verbose_name='Terça-Feira')
    quarta = models.BooleanField(null=True, verbose_name='Quarta-Feira')
    quinta = models.BooleanField(null=True, verbose_name='Quinta-Feira')
    sexta = models.BooleanField(null=True, verbose_name='Sexta-Feira')
    segunda_saida = models.BooleanField(null=True, verbose_name='Saída Segunda-Feira')
    terca_saida = models.BooleanField(null=True, verbose_name='Saída Terça-Feira')
    quarta_saida = models.BooleanField(null=True, verbose_name='Saída Quarta-Feira')
    quinta_saida = models.BooleanField(null=True, verbose_name='Saída Quinta-Feira')
    sexta_saida = models.BooleanField(null=True, verbose_name='Saída Sexta-Feira')
    segunda_justificado = models.BooleanField(null=True, verbose_name='Justificativa Segunda-Feira')
    terca_justificado = models.BooleanField(null=True, verbose_name='Justificativa Terça-Feira')
    quarta_justificado = models.BooleanField(null=True, verbose_name='Justificativa Quarta-Feira')
    quinta_justificado = models.BooleanField(null=True, verbose_name='Justificativa Quinta-Feira')
    sexta_justificado = models.BooleanField(null=True, verbose_name='Justificativa Sexta-Feira')


    def __str__(self):
        return str(self.nome_completo)

    def criarFrequenciaWorkshop(self, extensionista):
        FrequenciaWorkshop.objects.create(
            frequencia_extensionista=extensionista
        )

    def criarFrequenciaGeral(self, exntensionista):
        FrequenciaGeral.objects.create(
            frequencia_extensionista=exntensionista
        )

    class Meta:
        managed = True
        db_table = 'extensionista'



# MODELO PARA REGISTRO DE FREQUENCIA

class Frequencia(models.Model):
    id_frequencia = models.AutoField(primary_key=True, unique=True, null=False)
    segunda = models.BooleanField(null=True, verbose_name='Segunda-Feira')
    terca = models.BooleanField(null=True, verbose_name='Terça-Feira')
    quarta = models.BooleanField(null=True, verbose_name='Quarta-Feira')
    quinta = models.BooleanField(null=True, verbose_name='Quinta-Feira')
    sexta = models.BooleanField(null=True, verbose_name='Sexta-Feira')
    segunda_saida = models.BooleanField(null=True, verbose_name='Saída Segunda-Feira')
    terca_saida = models.BooleanField(null=True, verbose_name='Saída Terça-Feira')
    quarta_saida = models.BooleanField(null=True, verbose_name='Saída Quarta-Feira')
    quinta_saida = models.BooleanField(null=True, verbose_name='Saída Quinta-Feira')
    sexta_saida = models.BooleanField(null=True, verbose_name='Saída Sexta-Feira')
    segunda_justificado = models.BooleanField(null=True, verbose_name='Justificativa Segunda-Feira')
    terca_justificado = models.BooleanField(null=True, verbose_name='Justificativa Terça-Feira')
    quarta_justificado = models.BooleanField(null=True, verbose_name='Justificativa Quarta-Feira')
    quinta_justificado = models.BooleanField(null=True, verbose_name='Justificativa Quinta-Feira')
    sexta_justificado = models.BooleanField(null=True, verbose_name='Justificativa Sexta-Feira')
    frequencia_extensionista = models.ForeignKey(Extensionista, on_delete=models.CASCADE, null=True)


class FrequenciaWorkshop(Frequencia):

    class Meta:
        managed = True
        db_table = 'frequenciaworkspace'


    def __str__(self):
        return 'Frequência de ' + str(self.frequencia_extensionista)


class FrequenciaGeral(Frequencia):

    documentacao = models.BooleanField(default=False, verbose_name='Documentação')

    class Meta:
        managed = True
        db_table = 'frequenciageral'

    def __str__(self):
        return 'Frequência de {}'.format(str(self.frequencia_extensionista))
