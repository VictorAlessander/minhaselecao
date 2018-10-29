# Generated by Django 2.1.2 on 2018-10-29 22:04

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extensionista',
            fields=[
                ('id_extensionista', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome_completo', models.CharField(max_length=100, null=True, verbose_name='Nome completo')),
                ('telefone', models.CharField(max_length=11, null=True, verbose_name='Telefone/Celular')),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='E-mail')),
                ('matricula_extensionista', models.CharField(max_length=10, null=True, verbose_name='Matrícula')),
                ('curso', models.CharField(choices=[('Gestão da Tecnologia da Informação', 'Gestão da Tecnologia da Informação'), ('Ciência da Computação', 'Ciência da Computação'), ('Sistemas para Internet', 'Sistemas para Internet'), ('Redes de Computadores', 'Redes de Computadores'), ('Análise e Desenvolvimento de Sistemas', 'Análise e Desenvolvimento de Sistemas')], max_length=100, null=True)),
                ('periodo', models.CharField(choices=[('1º', '1º'), ('2º', '2º'), ('3º', '3º'), ('4º', '4º'), ('5º', '5º'), ('6º', '6º'), ('7º', '7º'), ('8º', '8º')], max_length=100, null=True)),
                ('habilidade_dominio', models.TextField(max_length=200, null=True, verbose_name='Cite duas habilidades que você domina')),
                ('habilidade_aprendizado', models.TextField(max_length=200, null=True, verbose_name='Cite duas habilidades que gostaria de aprender')),
                ('experiencia_profissional', models.TextField(max_length=200, null=True, verbose_name='Resuma sua experiência profissional')),
                ('outras_habilidades', models.TextField(max_length=200, null=True, verbose_name='Cite outras habilidades profissionais')),
                ('interesse_1', models.CharField(max_length=200, null=True, verbose_name='Gerente de Projetos')),
                ('interesse_2', models.CharField(max_length=200, null=True, verbose_name='Analista de Requesitos')),
                ('interesse_3', models.CharField(max_length=200, null=True, verbose_name='Desenvolvedor Front-End')),
                ('interesse_4', models.CharField(max_length=200, null=True, verbose_name='Desenvolvedor Back-End')),
                ('interesse_5', models.CharField(max_length=200, null=True, verbose_name='Administrador de Banco de Dados')),
                ('interesse_6', models.CharField(max_length=200, null=True, verbose_name='Desenvolvedor de Jogos')),
                ('interesse_7', models.CharField(max_length=200, null=True, verbose_name='Desenvolvedor de Jogos / Artista 2D, 3D')),
                ('interesse_8', models.CharField(max_length=200, null=True, verbose_name='Desenvolvedor de Jogos / Designer de Interface')),
                ('interesse_9', models.CharField(max_length=200, null=True, verbose_name='Engenheiro de Qualidade e Testes')),
                ('interesse_10', models.CharField(max_length=200, null=True, verbose_name='Gerente de Configuração e Infra Estrutura')),
                ('interesse_11', models.CharField(max_length=200, null=True, verbose_name='Administrador de Redes')),
                ('interesse_12', models.CharField(max_length=200, null=True, verbose_name='Analista de Testes')),
                ('interesse_13', models.CharField(max_length=200, null=True, verbose_name='Automatizador de Teste')),
                ('interesse_14', models.CharField(max_length=200, null=True, verbose_name='Testador')),
                ('interesse_15', models.CharField(max_length=200, null=True, verbose_name='Desenvolvedor de Chatboot')),
                ('interesse_16', models.CharField(max_length=200, null=True, verbose_name='Analista de Dados e Business Intelligence')),
                ('espera_1', models.CharField(max_length=200, null=True, verbose_name='Desenvolvimento Profissional')),
                ('espera_2', models.CharField(max_length=200, null=True, verbose_name='Desenvolver uma ideia empreendedora')),
                ('espera_3', models.CharField(max_length=300, null=True, verbose_name='Montar um Negócio')),
                ('espera_4', models.CharField(max_length=200, null=True, verbose_name='Adquirir Prática')),
                ('espera_5', models.CharField(max_length=200, null=True, verbose_name='Vivenciar Trabalho em Equipe')),
                ('espera_6', models.CharField(max_length=200, null=True, verbose_name='Conhecer como Funciona um Ambiente Empresarial')),
                ('espera_7', models.CharField(max_length=200, null=True, verbose_name='Ampliar meu Networking')),
                ('espera_8', models.CharField(max_length=200, null=True, verbose_name='Participar de Produção Científica')),
            ],
            options={
                'db_table': 'extensionista',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id_frequencia', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('segunda', models.BooleanField(null=True, verbose_name='Segunda-Feira')),
                ('terca', models.BooleanField(null=True, verbose_name='Terça-Feira')),
                ('quarta', models.BooleanField(null=True, verbose_name='Quarta-Feira')),
                ('quinta', models.BooleanField(null=True, verbose_name='Quinta-Feira')),
                ('sexta', models.BooleanField(null=True, verbose_name='Sexta-Feira')),
                ('segunda_saida', models.BooleanField(null=True, verbose_name='Saída Segunda-Feira')),
                ('terca_saida', models.BooleanField(null=True, verbose_name='Saída Terça-Feira')),
                ('quarta_saida', models.BooleanField(null=True, verbose_name='Saída Quarta-Feira')),
                ('quinta_saida', models.BooleanField(null=True, verbose_name='Saída Quinta-Feira')),
                ('sexta_saida', models.BooleanField(null=True, verbose_name='Saída Sexta-Feira')),
                ('segunda_justificado', models.BooleanField(null=True, verbose_name='Justificativa Segunda-Feira')),
                ('terca_justificado', models.BooleanField(null=True, verbose_name='Justificativa Terça-Feira')),
                ('quarta_justificado', models.BooleanField(null=True, verbose_name='Justificativa Quarta-Feira')),
                ('quinta_justificado', models.BooleanField(null=True, verbose_name='Justificativa Quinta-Feira')),
                ('sexta_justificado', models.BooleanField(null=True, verbose_name='Justificativa Sexta-Feira')),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id_workshop', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome_workshop', models.CharField(max_length=100, null=True, verbose_name='Tema Workshop')),
            ],
            options={
                'db_table': 'workshop',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserCadastro',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('matricula', models.CharField(max_length=10, unique=True, verbose_name='Matrícula')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=50, verbose_name='Sobrenome')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'usercadastro',
                'managed': True,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FrequenciaGeral',
            fields=[
                ('frequencia_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AppSelecao.Frequencia')),
                ('documentacao', models.BooleanField(default=False, verbose_name='Documentação')),
            ],
            options={
                'db_table': 'frequenciageral',
                'managed': True,
            },
            bases=('AppSelecao.frequencia',),
        ),
        migrations.CreateModel(
            name='FrequenciaWorkshop',
            fields=[
                ('frequencia_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AppSelecao.Frequencia')),
            ],
            options={
                'db_table': 'frequenciaworkspace',
                'managed': True,
            },
            bases=('AppSelecao.frequencia',),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='frequencia_extensionista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppSelecao.Extensionista'),
        ),
        migrations.AddField(
            model_name='extensionista',
            name='workshop_extensionista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppSelecao.Workshop'),
        ),
    ]
