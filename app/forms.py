from django import forms
from app.models import FormCliente
from app.models import Massa

class FormClienteForm(forms.ModelForm):
    class Meta:
        model = FormCliente
        fields = [
            'nome',
            'endereco',
            'telefone',
            'estado',
            'cidade',
            'pizzarias',
        ]

class MassaForm(forms.ModelForm):
    class Meta:
        model = Massa
        fields = [
            'massa',
            'molho',
            'ingredientes_salgada',
            'ingredientes_integral',
            'ingredientes_doce',
            'ingredientes_veg',
        ]