from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
# =========================== Here starts Department classes ==============================
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic.base import View

from organizacionalApp.models import Departamento, Funcao


class DerpartmentView(View):
    def get(self,request):
        template_name='departamento/departamento.html'
        departamento= Departamento.objects.all()

        return render(request, template_name,context={'object_list':departamento})

    def post(self,request):
        nomeDepartamento = request.POST['nomeDepartamento']
        descricao = request.POST['descricao']

        departamento = Departamento.objects.create(nomeDepartamento=nomeDepartamento, descricao=descricao)
        departamento.save()
        messages.success(request,'Departamento Registrado Com Sucesso!')
        return redirect('departamentos')

    def DepartmentDelete(self, pk):
        departamento = Departamento.objects.get(pk=pk)
        departamento.delete()
        return redirect('departamentos')


# ==================== Here starts Função classes ===============================================
class FuncaoView(View):

    def get(self, request):
        funcaolista= Funcao.objects.all()
        template_name = 'funcao/funcaoView.html'
        return render(request, template_name, context={'object2':funcaolista})

    def post(self,request):
        nomeFuncao= request.POST['nomeFuncao']
        funcao=Funcao.objects.create(nomeFuncao=nomeFuncao)
        funcao.save()
        return redirect('funcaoView')

    def FuncaoDelete(self,pk):
        funcao = Funcao.objects.get(pk=pk)
        funcao.delete()
        return redirect('funcaoView')


class FuncaoDelete(DeleteView):
    model = Funcao
    template_name = 'funcao/funcaoDelete.html'
    success_url = reverse_lazy('funcao/')


# ======================================================================

