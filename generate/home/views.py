from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import (render,
                              redirect,
                              get_object_or_404)
from .forms import (GenerateForm,
                    DepartamentForm,
                    DepartamentFormSelect,
                    DirectoryForm)
from .models import (Departament,
                     Directory)
from .classes import GenerateDefaultFile
from .classes.Utils import (departament as dep,
                            departament_name)


def index(request):
    template_name = 'index.html'

    return render(request, template_name)


def generate(request):
    template_name = 'gerar.html'
    context = {}

    form = GenerateForm(request.POST or None, request.FILES or None)
    context['form'] = form

    if request.method == 'POST':
        setor = ''
        cliente = request.POST['client_name']
        id_setor = request.POST['departament_name']
        if id_setor == '1':
            setor = 'Fiscal'
        elif id_setor == '2':
            setor = 'Contabil'
        elif id_setor == '3':
            setor = 'Materiais'
        elif id_setor == '4':
            setor = 'Financeiro'
        elif id_setor == '5':
            setor = 'NFCE'
        mes = request.POST['mounth']
        ano = request.POST['year']

        return generate_file(cliente, setor, mes, ano)

    return render(request, template_name, context)


def departament(request):
    template_name = 'departament.html'
    context = {}
    context['departament'] = Departament.objects.all()
    return render(request, template_name, context)


def new_departament(request):
    template_name = 'new_departament.html'
    context = {}
    form = DepartamentForm(request.POST or None, request.FILES or None)
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../departament')

    return render(request, template_name, context)


def del_departament(request, id):
    departament = get_object_or_404(Departament, pk=id)
    departament.delete()
    return redirect('departament')


def my_program(request, id):
    template_name = 'my_program.html'
    context = {}
    context['form'] = Directory.objects.filter(departament_name=id)
    context['title'] = dep(id)
    context['id_departament'] = id
    return render(request, template_name, context)


def programs(request):
    template_name = 'programs.html'
    context = {}
    form = DepartamentFormSelect
    context['form'] = form

    if request.method == 'POST':
        id_departament_name = int(request.POST['departament_name'])
        return redirect('my_program', id_departament_name)

    return render(request, template_name, context)


def del_program(request, id):
    id_departament = Directory.objects.filter(pk=id)
    program = get_object_or_404(Directory, pk=id)
    program.delete()
    return redirect('my_program', id_departament)


def new_program(request, id_departament):
    template_name = 'new_program.html'
    context = {}
    form = DirectoryForm(request.POST or None, request.FILES or None)
    context['form'] = form
    context['id_departament'] = id_departament

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('my_program', id_departament)

    return render(request, template_name, context)


def generate_file(client, departament, mounth, year):
    name_departament = departament_name(departament)
    default = GenerateDefaultFile.GenerateDefault(
        list(Directory.objects.filter(departament_name=name_departament)),
        list(Directory.objects.filter(departament_name=6)),
        list(Directory.objects.filter(departament_name=7))
    )
    file_name = departament.lower() + '_padrao.sh'
    context = default.generate_file(client, departament, mounth, year)
    content = ''

    for i in context:
        content += i + '\n'

    response = HttpResponse(content, content_type='text/plain; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename={file_name}'

    return response
