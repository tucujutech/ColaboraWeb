from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.views.generic.base import View

from core.models import Colaborador, Formacao, Departamento, Funcao, TipoFormacao


# ============= Login View ==========================================
class LoginView(View):
    def get(self,request):
        return render(request, template_name='login/login.html')



def dashboard(request, template_name='core/dashboard.html'):
    colabCount = Colaborador.objects.count()
    formaCount = Formacao.objects.count()
    return render(request, template_name, context={'colabCount':colabCount,'formaCount':formaCount})

# =============== Security ================================================
# ============ Here starts User classes ===================================


class RegUser(View):

    def get (self, request, *args, **kwargs):
       return render(request, template_name='user/userRegistro.html')

    def post(self, request, *args, **kwargs):
           if request.method == 'POST':
              username = request.POST['username']
              #first_name=request.POST['first_name']
              #last_name=request.POST['second_name']
              email = request.POST['email']
              password = request.POST['password']
              tipo = request.POST['tipo_user']
              if tipo == 'Administrador':
                user = User.objects.create_user(username, email, password)
                user.is_staff = True
                user.save()
              else:
                user = User.objects.create_user(username,  email, password)
           return redirect('Colaborador/listuser/')


# ======================  Here starts Colaborador classes =====================

class ColaboradorCreate(View):
    def get(self, request):
        funcao = Funcao.objects.values_list('nomeFuncao', flat=True)
        departamento = Departamento.objects.values_list('nomeDepartamento',flat=True)
        context = {'funcao':funcao, 'departamento':departamento}
        return render(request,template_name='core/colaborador/newColaborador.html', context = context)

    def post(self, request):
        if request.method == 'POST':
            nome= request.POST['nome']
            nascimento= request.POST['nascimento']
            rg= request.POST['rg']
            cpf= request.POST['cpf']
            telefone= request.POST['telefone']
            cnh = request.POST['cnh']
            cnh_tipo= request.POST['cnh_tipo']
            sexo_choices = request.POST['sexo']
            #foto_colaborador = request.POST['foto_colaborador']
            funcao = request.POST['funcao']
            funcao = Funcao.objects.get(nomeFuncao = funcao)
            departamento = request.POST['departamento']
            departamento = Departamento.objects.get(nomeDepartamento = departamento)

            colaborador,created= Colaborador.objects.get_or_create(nome=nome,
                                                    nascimento=nascimento, rg=rg,
                                                    cpf=cpf, telefone=telefone,
                                                    cnh=cnh, cnh_tipo=cnh_tipo, sexo_choices=sexo_choices,
                                                           funcao =funcao, departamento=departamento)

            colaborador.save()
        return redirect('colabList')


class ColabList(View):
    def get(self, request):
        model = Colaborador.objects.all()
        template_name = 'core/colaborador/colabList.html'
        paginator = Paginator(model, 6)
        page = request.GET.get('page')
        object_list = paginator.get_page(page)
        return render(request, template_name,{'object_list':object_list})


# is missing detail view and generate report view



# Is missing the Update class for Colaborator

class ColabDelete(DeleteView):
    model = Colaborador
    template_name = 'colaborador/colab_delete.html'
    success_url = reverse_lazy('colabList/')


# =================== Here starts Academics Formations classes ===========================
class FormacaoView(View):

    def get(self,request):
        colaborador = Colaborador.objects.values_list('nome', flat=True)
        tipo_formacao = TipoFormacao.objects.values_list('tipo_formacao', flat=True)
        context = {'colaborador':colaborador, 'tipoformacao':tipo_formacao}
        template_name = 'core/formacao/formacaoRegister.html'
        return render(request,template_name=template_name, context=context)


    def post(self, request):
        colaborador = request.POST['colaborador']
        colaborador = Colaborador.objects.get(nome=colaborador)
        tipo_formacao = request.POST['tipo_formacao']
        tipo_formacao = TipoFormacao.objects.get(tipo_formacao=tipo_formacao)
        nome_curso = request.POST['nome_curso']
        instituicao = request.POST['instituicao']
        dt_inicio = request.POST['dt_inicio']
        dt_termino = request.POST['dt_termino']

        formacao=Formacao.objects.create(colaborador=colaborador, tipo_formacao=tipo_formacao, nome_curso=nome_curso, instituicao=instituicao,
                                         dt_inicio=dt_inicio, dt_termino=dt_termino)
        formacao.save()
        return redirect('formacaoList')

    def FormacaoDelete(self, pk):
        formacao = Formacao.objects.get(pk =pk)
        formacao.delete()
        return redirect('formacaoList')


class FormacaoList(ListView):
    model = Formacao
    template_name = 'core/formacao/formacaoList.html'

class FormacaoDelete(DeleteView):
    model = Formacao
    template_name = 'formacao/formaDelete.html'
    success_url = reverse_lazy('formaList/')
