from django.shortcuts import render
from .forms import ContatoForms, ProdutoModelForm
from django.contrib import messages
from .models import Produto
from django.shortcuts import redirect

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html',context)


def contato(request):
    form = ContatoForms(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForms()
        else:
            messages.error(request, 'Erro ao enviar seu E-mail!')
    context = {
        'form' : form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method)== 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():

                form.save()

                messages.success(request, 'Produto salvo com sucesso.')
                form = ProdutoModelForm()
            else:
                messages.error(request,'Erro ao salvar o Produto.')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')