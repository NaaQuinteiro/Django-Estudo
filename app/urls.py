from django.urls import path
from .views import * 

urlpatterns = [
    path('livro/', LivroView.as_view(), name='Hello_world'),
    path('livro/<int:id>', LivroView.as_view(), name='Hello_world_by_id')
]
