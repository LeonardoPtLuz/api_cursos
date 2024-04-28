from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }

        model = Avaliacao

        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )

        #fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
        )

        #fields = '__all__'