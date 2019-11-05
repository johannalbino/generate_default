import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext

from .forms import GenerateForm
from .models import OptionGenerate as modelOption
from .classes import gerar_default_cl


# Create your views here.


def index(request):
    template_name = 'index.html'

    return render(request, template_name)


def generate(request):
    template_name = 'gerar.html'
    context = {}

    form = GenerateForm(request.POST or None, request.FILES or None)
    context['form'] = form

    if form.is_valid():
        cliente = request.POST['client_name']
        setor = request.POST['departament_name']
        mes = request.POST['mounth']
        ano = request.POST['year']

        return generate_file(cliente, setor, mes, ano)

    return render(request, template_name, context)


def setores(request):
    template_name = 'setores.html'

    return render(request, template_name)


def generate_file(cliente, setor, mes, ano):
    padrao = gerar_default_cl.GenerateDefault()
    file_name = setor.lower() + '_padrao.sh'
    context = padrao.generate_file(cliente, setor, mes, ano)
    content = ''

    for i in context:
        content += i + '\n'

    response = HttpResponse(content, content_type='text/plain; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(file_name)

    return response
