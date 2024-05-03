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
    
    #NESTED RELATIONSHIP
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #HYPERLINKED RELATED FIELD
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    #PRIMARY KEY RELATED FIELD
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
        )

        #fields = '__all__'