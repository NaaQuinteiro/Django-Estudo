from django.db import models

# Create your models here.

#criando uma tabela do banco de dados
class Genero(models.Model):
    #tupla feita para delimitar oque o ususario pode escolher
    #elas se repetem pois uma sera mostrada para o banco e o usuario 
    GENEROS = [
        ('Suspense', 'Suspense'),
        ('Romance', 'Romance'),
        ('Ação', 'Ação')
    ]

    #atributo "CharField" equivalent ao Varchar do bamco de dados
    #choices é para mostrar as opções que o usuario tem
    #max_lenght=150 equivale ao tanto de caracter o usuario pode digitar
    tipo = models.CharField(max_length=150, choices=GENEROS)

class Livros(models.Model):
    #o null ele pode ser vazio ou não, colccamos como True então ele pode aceitar uma campo vazio
    titulo = models.CharField(max_length=150, null=True)
    # teste = models.CharField(max_length=150, null=True)

class GeneroLivro(models.Model):
    #chaves estrangeiras
    #related_name é o nome atribuido a chave primaria (commit do nome)
    #on_delete=models.CASCADE é o efeito domino na aplicação onde a linha relacionada aquele ao um campo é deletada 
    fk_livro = models.ForeignKey(Livros,related_name ='livro_genero',on_delete=models.CASCADE)
    fk_genero = models.ForeignKey(Genero, related_name='genero_genero', on_delete=models.CASCADE)


