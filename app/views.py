from django.shortcuts import render
from app.forms import FormClienteForm
from app.forms import MassaForm

# Create your views here.
def mostrar_index(request):
    formulario = FormClienteForm(request.POST or None)
    msg = ''

    if formulario.is_valid():
        formulario.save()
        formulario = FormClienteForm()
        msg = 'Pedido realizado com sucesso'

    contexto = {
        'form' : formulario,
        'msg' : msg
    }
    return render(request, 'index.html', contexto)


def mostrar_pedidos(request):
    return render(request, 'pedidos.html')