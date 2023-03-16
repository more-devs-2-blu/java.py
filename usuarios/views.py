from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Cidadao
from django.db.models import Q


def Cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')

    nomeCompleto = request.POST.get('nomeCompleto')
    cpf_cnpj = request.POST.get('cpf_cnpj')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    cep = request.POST.get('cep')
    uf = request.POST.get('uf')
    cidade = request.POST.get('cidade')
    bairro = request.POST.get('bairro')
    rua = request.POST.get('rua')
    complemento = request.POST.get('complemento')

    cepLimpo = [str(digit) for digit in cep if digit.isdigit()]

    cepLimpo = ''.join(cepLimpo)

    user = Cidadao.objects.filter(Q(cpf_cnpj=email) | Q(email=email)).first()
    if user:
        return render(request, 'usuarios/cadastro.html')

    cpfCnpjLimpo = [str(digit) for digit in cpf_cnpj if digit.isdigit()]

    cpf_cnpj = ''.join(cpfCnpjLimpo)

    nome = nomeCompleto.split()[0]
    sobrenome = ' '.join(nomeCompleto.split()[1:])
    user = Cidadao.objects.create_user(
        username=cpf_cnpj, password=senha, email=email, cpf_cnpj = cpf_cnpj)

    user.first_name = nome
    user.last_name = sobrenome

    user.save()

    return render(request, 'usuarios/login.html')


def Login(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')

    cpf = request.POST.get('cpf')
    senha = request.POST.get('senha')
    user = None
    try:
        user = Cidadao.objects.get(cpf_cnpj=cpf)
    except Cidadao.DoesNotExist:
        # email não existe
        messages.error(request, 'Usuário ou senha inválida')
        return render(request, 'usuarios/login.html')

    if user.check_password(senha):
        # senha válida, autenticar usuário
        user = authenticate(request, username=cpf, password=senha)
        if user is not None:
            login(request, user)
            return redirect('home')

    messages.error(request, 'Usuário ou senha inválida')
    return render(request, 'usuarios/login.html')


def Logout(request):
    logout(request)
    return redirect('login')