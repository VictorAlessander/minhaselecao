from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms


class ColaboradorForm(UserCreationForm):
    class Meta:
        model = UserCadastro
        fields = ['matricula', 'email', 'first_name', 'last_name']


class ExtensionistaEditForm(ModelForm):
    class Meta:
        model = Extensionista
        fields = ['nome_completo', 'matricula_extensionista', 'email', 'curso', 'periodo', 'workshop_extensionista']



class ExtensionistaForm(ModelForm):
    class Meta:
        model = Extensionista
        fields = ['nome_completo', 'matricula_extensionista', 'telefone', 'email', 'curso', 'periodo',
                  'email', 'workshop_extensionista', 'habilidade_dominio', 'habilidade_aprendizado',
                  'experiencia_profissional', 'outras_habilidades', 'interesse_1', 'interesse_2',
                  'interesse_3', 'interesse_4', 'interesse_5', 'interesse_6',  'interesse_7',
                  'interesse_8', 'interesse_9', 'interesse_10', 'interesse_11', 'interesse_12',
                  'interesse_13', 'interesse_14', 'interesse_15', 'interesse_16', 'espera_1',
                  'espera_2', 'espera_3', 'espera_4', 'espera_5', 'espera_6', 'espera_7', 'espera_8']


        widgets = {
            'interesse_1': forms.RadioSelect(choices=INTERESSE, attrs={'display': 'inline-block'}),
            'interesse_2': forms.RadioSelect(choices=INTERESSE),
            'interesse_3': forms.RadioSelect(choices=INTERESSE),
            'interesse_4': forms.RadioSelect(choices=INTERESSE),
            'interesse_5': forms.RadioSelect(choices=INTERESSE),
            'interesse_6': forms.RadioSelect(choices=INTERESSE),
            'interesse_7': forms.RadioSelect(choices=INTERESSE),
            'interesse_8': forms.RadioSelect(choices=INTERESSE),
            'interesse_9': forms.RadioSelect(choices=INTERESSE),
            'interesse_10': forms.RadioSelect(choices=INTERESSE),
            'interesse_11': forms.RadioSelect(choices=INTERESSE),
            'interesse_12': forms.RadioSelect(choices=INTERESSE),
            'interesse_13': forms.RadioSelect(choices=INTERESSE),
            'interesse_14': forms.RadioSelect(choices=INTERESSE),
            'interesse_15': forms.RadioSelect(choices=INTERESSE),
            'interesse_16': forms.RadioSelect(choices=INTERESSE),
            'espera_1': forms.RadioSelect(choices=INTERESSE),
            'espera_2': forms.RadioSelect(choices=INTERESSE),
            'espera_3': forms.RadioSelect(choices=INTERESSE),
            'espera_4': forms.RadioSelect(choices=INTERESSE),
            'espera_5': forms.RadioSelect(choices=INTERESSE),
            'espera_6': forms.RadioSelect(choices=INTERESSE),
            'espera_7': forms.RadioSelect(choices=INTERESSE),
            'espera_8': forms.RadioSelect(choices=INTERESSE),
        }


class ExtensionistaBuscarForm(ModelForm):
    class Meta:
        model = Extensionista
        fields = ('matricula_extensionista', )


class FrequenciaWorkshopForm(ModelForm):
    class Meta:
        model = FrequenciaWorkshop
        fields = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'segunda_saida', 'terca_saida', 'quarta_saida', 'quinta_saida', 'sexta_saida',
                  'segunda_justificado', 'terca_justificado', 'quarta_justificado', 'quinta_justificado', 'sexta_justificado']

        widgets = {
            'segunda': forms.CheckboxInput(),
            'terca': forms.CheckboxInput(),
            'quarta': forms.CheckboxInput(),
            'quinta': forms.CheckboxInput(),
            'sexta': forms.CheckboxInput(),
        }


class WorkshopForm(ModelForm):
    class Meta:
        model = Workshop
        fields = ['nome_workshop']