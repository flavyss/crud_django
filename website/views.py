from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_dj
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Funcionario

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro/cadastro.html')
    else:
        nome = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

    user = User.objects.filter(username=nome, email=email).first()
    
    if user:
        return HttpResponse("ja existe um usuario com esse nome")
    
    user = User.objects.create_user(username=nome, email=email, password=senha)
    user.save()

    return HttpResponse("Usuario Cadastrado com sucesso")

def login(request):
    if request.method == 'GET':
            return render(request, 'login/login.html')
    else:
        nome = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=nome, password=senha)

        if user:
            login_dj(request, user)
            return redirect('home')
        else:
            return HttpResponse("os dados nao existem ou estao errados")

@login_required(login_url="/login/")
def home(request):
    user=request.user
    funcionario = Funcionario.objects.all()
    return render(request, 'home/home.html', {'user': user, 'funcionario': funcionario})

@login_required(login_url="/login/")
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/login/")
def create(request):
    if request.method == 'GET':
        return render(request, 'criar/criar.html')
    else:
        nome_dig = request.POST.get('nome')
        sobrenome_dig = request.POST.get('sobrenome')
        cpf_dig = request.POST.get('cpf')
        tempo_de_servico_dig = request.POST.get('tempo')
        remuneracao_dig = request.POST.get('remuneracao')
        cdp_dig = request.POST.get('cdp')


        funcionario = Funcionario(
            nome=nome_dig,
            sobrenome=sobrenome_dig,
            cpf=cpf_dig,
            tempo_de_servico=tempo_de_servico_dig,
            remuneracao=remuneracao_dig,
            cdp=cdp_dig
        )
        funcionario.save()

        messages.success(request, 'Funcionario registrado com sucesso')

        return redirect('/create/')

@login_required(login_url="/login/")
def delete(request, id):
    funcionario = Funcionario.objects.get(id=id)
    funcionario.delete()
    return redirect('/')

@login_required(login_url="/login/")
def update(request, id):
    user=request.user
    funcionario = Funcionario.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'update/update.html', {'user': user, 'funcionario': funcionario})
    else:
        nome_dig = request.POST.get('nome')
        sobrenome_dig = request.POST.get('sobrenome')
        cpf_dig = request.POST.get('cpf')
        tempo_de_servico_dig = request.POST.get('tempo')
        remuneracao_dig = request.POST.get('remuneracao')
        cdp_dig = request.POST.get('cdp')

        funcionario.nome = nome_dig
        funcionario.sobrenome = sobrenome_dig
        funcionario.cpf = cpf_dig
        funcionario.tempo_de_servico = tempo_de_servico_dig
        funcionario.remuneracao = remuneracao_dig
        funcionario.cdp = cdp_dig
        funcionario.save()

        messages.success(request, 'editado com sucesso')

        return redirect(f'/update/{id}')