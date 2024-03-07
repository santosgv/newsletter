import datetime
from django.contrib.auth.decorators import login_required
from .utils import email_html
from django.shortcuts import  render,redirect,get_object_or_404
from django.core.paginator import Paginator
import os
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

from django.contrib import sitemaps

from django.http import FileResponse,JsonResponse
from django.contrib import messages
from django.contrib.messages import constants
import logging

logger = logging.getLogger('MyApp')


def index(request):
     return render(request,'index.html')

def blog(request):
     return render(request,'blog.html')

def formulario(request):
    if request.method =="POST":
        email = request.POST.get('email')
        valida = Email.objects.filter(email=email)
        if valida.exists():
            messages.add_message(request, constants.ERROR, 'Email Ja cadastrado')
            logger.info(f'Email Ja cadastrado {email} '+str(datetime.datetime.now())+' horas!')
            return redirect("/")
        cadastrar = Email.objects.create(
            email=email
        )
        cadastrar.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso')
        return redirect("/")
    
def unsubscriber(request,id):
    email = Email.objects.get(id=id)
    email.ativo =False
    email.save()
    return HttpResponse('Cancelado sua Inscriçao')

@login_required(login_url='/admin/login/?next=/admin/') 
def enviar_emeil(request):
    try:
        path_template = os.path.join(settings.BASE_DIR, 'Core/templates/emails/email.html')
        base_url = request.build_absolute_uri('/')
        emails = Email.objects.filter(ativo=True).all()
        posts = Imagem.objects.only('nome','descricao').filter(destaque=True).all().order_by('-id')[:15]

        for email in emails:
            email_html(path_template, 'Novos Desenhos', [email,],posts=posts,email=email,base_url=base_url)
            messages.add_message(request, constants.SUCCESS, 'Emais enviados com sucesso')
            return redirect("/")
        
    except Exception as msg:
        messages.add_message(request, constants.ERROR, f'Nao foi possivel enviar os Emails consulte o arquivo de Log')
        logger.critical(f'{msg} '+str(datetime.datetime.now())+' horas!')
        return redirect("/")



class Sitemap(sitemaps.Sitemap):
    i18n = True
    changefreq ='monthly'
    priority = 0.7

    def items(self):
        return Imagem.objects.all()        

    def lastmod(self, obj):
        return obj.data_upload
