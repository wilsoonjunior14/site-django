from django.shortcuts import render
from django.http import HttpResponse
import random
from os import path
from datetime  import datetime

from core.models import Poster

# Create your views here.
from exemplo.settings import STATIC_FOLDER_FILES, STATIC_URL
from django.core.files.storage import FileSystemStorage


def index(request):
	return render(request, 'index.html', {'page': 'template'})

# log in on app
def login(request):
	return render(request, 'index.html', {'page': 'template'})


# url for administrators
def admin(request):

	posters = Poster.objects.all()

	return render(request, 'admin.html', {'posters': posters})


def addPoster(request):

	data = {'imagem': '', 'titulo': '', 'descricao': '', 'success': False, 'error': False, 'msg': ''}

	print (request.method)
	if (request.method == 'POST'):

		if(request.FILES.get('imagem', False)):
			data['imagem'] = uploaded_file(request.FILES['imagem'])
		data['titulo'] = request.POST.get('titulo')
		data['descricao'] = request.POST.get('descricao')

		if (data['imagem'].__len__() <= 0 or ( not(".png" in data['imagem']) and not(".jpg" in data['imagem']) and not(".jpeg" in data['imagem']) )):
			data['error'] = True
			data['msg']   = "Pôster é obrigatório! Formatos aceitos: .png, .jpg, .jpeg"

		elif ( data['titulo'].__len__() <= 0 or data['titulo'].__len__() > 255):
			data['error'] = True
			data['msg'] = "Titulo do pôster é obrigatório e não pode ultrapassar 255 caracteres"

		elif ( data['descricao'].__len__() <= 0 or data['descricao'].__len__() > 500 ):
			data['error'] = True
			data['msg'] = "Descrição do pôster é obrigatório e não pode ultrapassar 500 caracteres"

		else:

			newPost = Poster(titulo=data['titulo'], descricao=data['descricao'], imagem=data['imagem'])
			newPost.save()
			data['success'] = True
			data['msg'] = "Pôster adicionado com sucesso!"


	return render(request, 'add.html', data)

def uploaded_file(f):
	fs = FileSystemStorage()
	filename = fs.save(f.name, f)

	return fs.url(filename)

