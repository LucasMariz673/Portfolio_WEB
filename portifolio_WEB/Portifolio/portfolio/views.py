from django.shortcuts import render
from core.models import Pessoal
from .models import Certificado, Projeto

def home(request):
    dados =  Pessoal.objects.first()
    certificados = Certificado.objects.all()
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/home.html', {
        'dados': dados,
        'certificados': certificados,
        'projetos': projetos
    })


def projetos(request):
    projeto = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projeto})
    #return render(request, 'portfolio/projetos.html')

