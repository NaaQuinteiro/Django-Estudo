from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
import json
# aba para criação de metodos = ao controler do projeto

class LivroView(APIView):
    #funções para chamar as classes, o request é do que ele está requisitando
    def get(self, request, id=''):

        if id:
            
            livros = Livros.objects.filter(id=id).first()

            if not livros:
                return Response(status=404, data={'mensagem': 'livro nao encontrado'})

            serializer = LivroSerializer(livros, many=False)
            return Response(status=200, data=serializer.data)
        else:

            livros = Livros.objects.all()
            serializer = LivroSerializer(livros, many=True)
            return Response(status=201, data=serializer.data)
        
    def post(self, request):
        #o body é o corpo da requisição
        # body = json.loads(request.body)
        #o loads ele converte bytes, strings e arrey de bytes para json (o documennto precisa estar em formato json)
        # serializer = LivroSerializer(body, many=False)
        body = request.data
        serializer = LivroSerializer(data=body, many=False)

        if not serializer.is_valid():
             return Response(status=400, data={'mensagem': 'dado ruim'})
        serializer.save()
        # print(serializer)

        return Response(status=201, data=serializer.data)
    
    def put(self, request, id, titulo):
        update_livro = self.get(id, titulo)
        if not update_livro:
            return Response(status=404, data={'Mensagem': 'id nao existe'})
      
        data = {
            'titulo': request.data.get('titulo')
        }

        serializer = LivroSerializer(instance=update_livro,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=404)


    


