from rest_framework.serializers import ModelSerializer
from .models import *

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livros
        many = True
        fields ='__all__'

class LivroSerializerTitulo(ModelSerializer):
    class Meta:
        model = Livros
        many = True
        fields =('titulo',)


#serializer para quando fomos criar, para passar a senha
#class UserSerializerCreate()

#serializer para quando fomos retornar sem a senha
#class UserSerializerGet()


