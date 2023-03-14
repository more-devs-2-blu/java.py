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
        topico = categoria, 
        cidadao = request.user,
        uf = uf,
        bairro = bairro,
        rua = rua,
        complemento = complemento,
        cidade = cidade,
        )

    comentario.save()

    return redirect('home')

'''
def Listagem(request):
    List = Comentario.objects.all()
    return render(request, 'comentarios/listagem.html', {'List': List})
'''

def Listagem(request):
    # Tenta converter o valor do parâmetro "value" para um inteiro.
    # Se a conversão falhar, define o valor padrão como zero.
    try:
        value = int(request.GET.get('value', '0'))
    except ValueError:
        value = 0

    # Verifica se o valor é diferente de zero.
    if value != 0:
        # Filtra os comentários pelo tópico especificado.
        List = Comentario.objects.filter(topico=value)
    else:
        # Obtém todos os comentários.
        List = Comentario.objects.all()

    # Renderiza o template com a lista de comentários.
    return render(request, 'comentarios/listagem.html', {'List': List})