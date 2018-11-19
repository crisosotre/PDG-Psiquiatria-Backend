from rest_framework import serializers
from .models import Competencia, Competencia_Curso, Competencia_Objetivo, Objetivo, Tipo_Objetivo, Curso, Momento_Evaluativo, Objetivo_Assessment, Assessment, Tipo_Assessment, Usuario, Usuario_Curso, Usuario_Perfil, Evaluacion, Perfil, Variables_Configuracion

class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = ('id_competencia', 'desc_competencia')

class TipoObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Objetivo
        fields = ('id_tipo_objetivo', 'nombre')

class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objetivo
        fields = ('id_objetivo', 'desc_objetivo', 'id_tipo_objetivo')

class CompetenciaObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia_Objetivo
        fields = ('id_comp_obj', 'id_competencia', 'id_objetivo')

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id_curso', 'nombre')

class CompetenciaCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia_Curso
        fields = ('id_comp_cur', 'id_competencia', 'id_curso')

class TipoAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Assessment
        fields = ('id_tipo_assessment', 'nombre')

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ('id_assessment', 'nombre', 'abreviatura', 'id_tipo_assessment')

class ObjetivoAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objetivo_Assessment
        fields = ('id_obj_assess', 'id_objetivo', 'id_assessment')

class MomentoEvaluativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Momento_Evaluativo
        fields = ('id_momento_evaluativo', 'ponderacion', 'id_curso', 'id_obj_assess')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id_usuario', 'nombre', 'apellido', 'correo', 'contrasena', 'url_foto')

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ('id_perfil', 'nombre')

class UsuarioPerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_Perfil
        fields = ('id_usuario_perfil', 'id_usuario', 'id_perfil')

class UsuarioCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_Curso
        fields = ('id_usuario_curso', 'id_usuario', 'id_curso')

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = ('id_evaluacion', 'calificacion', 'id_momento_evaluativo', 'id_usuario_curso', 'id_usuario_perfil')

class VariablesConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variables_Configuracion
        fields = ('id_var_conf', 'nombre', 'valor')