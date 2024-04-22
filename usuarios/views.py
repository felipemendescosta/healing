from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirmar_senha')

        if senha != confirma_senha:
            messages.add_message(request, constants.ERROR,"A senha e o confirmar senha devem ser iguais")
            return redirect('/usuarios/cadastro')
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR,"A senha deve ser maior que 6 caracteres")

            return redirect ('/usuarios/cadastro')
        
        users = User.objects.filter(username = username)
        print(users.exists())

        if users.exists():
            return redirect('/usuarios/cadastro')
        
        user = User.objects.create_user(
            username = username,
            email = email,
            password = senha
        )

        return redirect("/usuarios/login")

def login_view(request):
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = auth.authenticate(request,username=username,password=senha)
        
        if user:
            auth.login(request,user)
            return redirect("/pacientes/home") #TODO vai dar erro
        
        messages.add_message(request, constants.ERROR, "Usuario ou Senha Inválidos")
        return redirect("/usuarios/login")
    
def sair(request):
    auth.logout(request)
    return redirect("/usuarios/")    

