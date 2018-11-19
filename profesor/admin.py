# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Competencia, Competencia_Curso, Competencia_Objetivo, Objetivo, Tipo_Objetivo, Curso, Momento_Evaluativo, Objetivo_Assessment, Assessment, Tipo_Assessment, Usuario, Usuario_Curso, Usuario_Perfil, Evaluacion, Perfil, Variables_Configuracion

# Register your models here.

class AdminCompetencia(admin.ModelAdmin):
    list_display = ["id_competencia", "desc_competencia"]
    class Meta:
        model = Competencia

class AdminTipoObjetivo(admin.ModelAdmin):
    list_display = ["id_tipo_objetivo", "nombre"]
    class Meta:
        model = Tipo_Objetivo

class AdminObjetivo(admin.ModelAdmin):
    list_display = ["id_objetivo", "desc_objetivo", "id_tipo_objetivo"]
    class Meta:
        model = Objetivo

class AdminCompetenciaObjetivo(admin.ModelAdmin):
    list_display = ["id_comp_obj", "id_competencia", "id_objetivo"]
    class Meta:
        model = Competencia_Objetivo

class AdminCurso(admin.ModelAdmin):
    list_display = ["id_curso", "nombre"]
    class Meta:
        model = Curso

class AdminCompetenciaCurso(admin.ModelAdmin):
    list_display = ["id_comp_cur", "id_competencia", "id_curso"]
    class Meta:
        model = Competencia_Curso

class AdminTipoAssessment(admin.ModelAdmin):
    list_display = ["id_tipo_assessment", "nombre"]
    class Meta:
        model = Tipo_Assessment

class AdminAssessment(admin.ModelAdmin):
    list_display = ["id_assessment", "nombre", "abreviatura", "id_tipo_assessment"]
    class Meta:
        model = Assessment

class AdminObjetivoAssessment(admin.ModelAdmin):
    list_display = ["id_obj_assess", "id_objetivo", "id_assessment"]
    class Meta:
        model = Objetivo_Assessment

class AdminMomentoEvaluativo(admin.ModelAdmin):
    list_display = ["id_momento_evaluativo", "ponderacion", "id_curso", "id_obj_assess"]
    class Meta:
        model = Momento_Evaluativo

class AdminUsuario(admin.ModelAdmin):
    list_display = ["id_usuario", "nombre", "apellido", "correo", "contrasena", "url_foto"]
    class Meta:
        model = Usuario

class AdminPerfil(admin.ModelAdmin):
    list_display = ["id_perfil", "nombre"]
    class Meta:
        model = Perfil

class AdminUsuarioPerfil(admin.ModelAdmin):
    list_display = ["id_usuario_perfil", "id_usuario", "id_perfil"]
    class Meta:
        model = Usuario_Perfil

class AdminUsuarioCurso(admin.ModelAdmin):
    list_display = ["id_usuario_curso", "id_usuario", "id_curso"]
    class Meta:
        model = Usuario_Curso

class AdminEvaluacion(admin.ModelAdmin):
    list_display = ["id_evaluacion", "calificacion", "id_momento_evaluativo", "id_usuario_curso", "id_usuario_perfil"]
    class Meta:
        model = Evaluacion

class AdminVariablesConfiguracion(admin.ModelAdmin):
    list_display = ["id_var_conf", "nombre", "valor"]
    class Meta:
        model = Variables_Configuracion

admin.site.register(Competencia, AdminCompetencia)
admin.site.register(Tipo_Objetivo, AdminTipoObjetivo)
admin.site.register(Objetivo, AdminObjetivo)
admin.site.register(Competencia_Objetivo, AdminCompetenciaObjetivo)
admin.site.register(Curso, AdminCurso)
admin.site.register(Competencia_Curso, AdminCompetenciaCurso)
admin.site.register(Tipo_Assessment, AdminTipoAssessment)
admin.site.register(Assessment, AdminAssessment)
admin.site.register(Objetivo_Assessment, AdminObjetivoAssessment)
admin.site.register(Momento_Evaluativo, AdminMomentoEvaluativo)
admin.site.register(Usuario, AdminUsuario)
admin.site.register(Perfil, AdminPerfil)
admin.site.register(Usuario_Perfil, AdminUsuarioPerfil)
admin.site.register(Usuario_Curso, AdminUsuarioCurso)
admin.site.register(Evaluacion, AdminEvaluacion)
admin.site.register(Variables_Configuracion, AdminVariablesConfiguracion)