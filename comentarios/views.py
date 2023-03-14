from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Comentario


#@login_required
def Cadastro(request):
    if request.method == "GET":
        return render(request, 'comentarios/cadastro.html')

    resumo = request.POST.get('resumo')
    categoria = int(request.POST.get('categoria'))
    descricao = request.POST.get('descricao')
    cep = request.POST.get('cep')
    uf = request.POST.get('uf')
    cidade = request.POST.get('cidade')
    bairro = request.POST.get('bairro')
    rua = request.POST.get('rua')
    complemento = request.POST.get('complemento')

    cepLimpo = [str(digit) for digit in cep if digit.isdigit()]

    cepLimpo = ''.join(cepLimpo)

    comentario = Comentario(
        resumo = resumo, 
        descricao = descricao, 
        topico= categoria, 
        cidadao= request.user,
        uf= uf,
        bairro= bairro,
        rua= rua,
        complemento= complemento,
        cidade= cidade,
        )

    comentario.save()

    return redirect('home')

'''
def Listagem(request):
    List = Comentario.objects.all()
    return render(request, 'comentarios/listagem.html', {'List': List})
'''

def Listagem(request):
    value = int(request.GET.get('value'))


    if value != 0:
        List = Comentario.objects.filter(topico=value)
        return render(request, 'comentarios/listagem.html', {'List': List})
    else:
        List = Comentario.objects.all()
        return render(request, 'comentarios/listagem.html', {'List': List})