from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Contato
from django.http import Http404
from django.db import models, IntegrityError
from django.db.models import Q, Value
from django.db.models.functions import Concat






def index(request):
	# Buscar todos os contatos
	contatos = Contato.objects.filter(mostra=True).order_by('-id')
	paginator = Paginator(contatos, 25) # Show 25 contacts per page.
	page_number = request.GET.get('page')
	contatos = paginator.get_page(page_number)
	return render(request, 'contatos/index.html', {'contatos': contatos})


def ver_contato(request, contato_id):
	# Buscar o contato pelo ID
	contato = Contato.objects.get(id=contato_id)
	if not contato.mostra:
		raise Http404
	return render(request, 'contatos/ver_contato.html', {'contato': contato})	


def busca(request):
	termo = request.GET.get('termo')
	if termo is None or not termo:
		raise Http404()
	campos = Concat('nome', Value(' '), 'sobrenome')
	# contatos = Contato.objects.filter(Q(nome__icontains=termo) | Q(sobrenome__icontains=termo), mostra=True).order_by('-id')
	contatos = Contato.objects.annotate(nome_completo=campos).filter(Q(nome_completo__icontains=termo)).order_by('-id')
	paginator = Paginator(contatos, 25) # Show 25 contacts per page.
	page_number = request.GET.get('page')
	contatos = paginator.get_page(page_number)
	return render(request, 'contatos/busca.html', {'contatos': contatos})