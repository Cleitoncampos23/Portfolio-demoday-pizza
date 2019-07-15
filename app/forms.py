from django import forms
from app.models import FormCliente
from app.models import Massa, Ingrediente

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

    def __init__(self, tipo, *args,**kwargs):
        self.tipo = tipo
        super(MassaForm,self).__init__(*args,**kwargs)
        self.fields['ingredientes'] = forms.ModelMultipleChoiceField(queryset=Ingrediente.objects.filter(tipo=tipo))

    class Meta:
        model = Massa
        fields = [
            'massa',
            'molho'
        ]

# class MassaForm(forms.ModelForm):
#     class Meta:
#         model = Massa
#         fields = [
#             'molho',
#         ]

# class MassaForm(forms.ModelForm):
#     class Meta:
#         model = Massa
#         fields = [
#             'ingredientes_salgada',
#         ]

# class MassaForm(forms.ModelForm):
#     class Meta:
#         model = Massa
#         fields = [
#             'ingredientes_integral',
        
#         ]

# class MassaForm(forms.ModelForm):
#     class Meta:
#         model = Massa
#         fields = [
#             'ingredientes_doce',
#         ]

# class MassaForm(forms.ModelForm):
#     class Meta:
#         model = Massa
#         fields = [
#             'ingredientes_veg',
#         ]