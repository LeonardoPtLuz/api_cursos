from rest_framework import serializers
from .models import Curso, Avaliacao
from django.db.models import Avg

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

    def validate_avaliacao(self, valor):
        if valor in range(1, 11):
            return valor
        raise serializers.ValidationError('Nota deve ser apenas entre 1 e 10')


class CursoSerializer(serializers.ModelSerializer):
    
    #NESTED RELATIONSHIP
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #HYPERLINKED RELATED FIELD
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    #PRIMARY KEY RELATED FIELD
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

        #fields = '__all__'

    #MEDIA DAS AVALIAÇÕES
    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        if media is None:
            return 0
        return round(media*2)/2
    #IMPLEMENTAR get_media_avaliacoes() EM MODEL(SIGNALS)!!!!!!!