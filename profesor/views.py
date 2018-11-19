# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics
from .models import Competencia, Competencia_Curso, Competencia_Objetivo, Objetivo, Tipo_Objetivo, Curso, Momento_Evaluativo, Objetivo_Assessment, Assessment, Tipo_Assessment, Usuario, Usuario_Curso, Usuario_Perfil, Evaluacion, Perfil, Variables_Configuracion
from .serializers import CompetenciaSerializer, CompetenciaCursoSerializer, CompetenciaObjetivoSerializer, ObjetivoSerializer, TipoObjetivoSerializer, CursoSerializer, MomentoEvaluativoSerializer, ObjetivoAssessmentSerializer, AssessmentSerializer, TipoAssessmentSerializer, UsuarioSerializer, UsuarioCursoSerializer, UsuarioPerfilSerializer, EvaluacionSerializer, PerfilSerializer, VariablesConfiguracionSerializer
from django.db.models import Q
# # Create your views here.

class CompetenciaList(generics.ListCreateAPIView):
    queryset = Competencia.objects.all()
    serializer_class = CompetenciaSerializer

class CompetenciaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competencia.objects.all()
    serializer_class = CompetenciaSerializer

class TipoObjetivoList(generics.ListCreateAPIView):
    queryset = Tipo_Objetivo.objects.all()
    serializer_class = TipoObjetivoSerializer

class TipoObjetivoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tipo_Objetivo.objects.all()
    serializer_class =  TipoObjetivoSerializer
    
class ObjetivoList(generics.ListCreateAPIView):
    queryset = Objetivo.objects.all()
    serializer_class = ObjetivoSerializer

class ObjetivoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Objetivo.objects.all()
    serializer_class = ObjetivoSerializer

class CompetenciaObjetivoList(generics.ListCreateAPIView):
    queryset = Competencia_Objetivo.objects.all()
    serializer_class = CompetenciaObjetivoSerializer

class CompetenciaObjetivoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competencia_Objetivo.objects.all()
    serializer_class = CompetenciaObjetivoSerializer

class CursoList(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CompetenciaCursoList(generics.ListCreateAPIView):
    queryset = Competencia_Curso.objects.all()
    serializer_class = CompetenciaCursoSerializer

class CompetenciaCursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competencia_Curso.objects.all()
    serializer_class = CompetenciaCursoSerializer

class TipoAssessmentList(generics.ListCreateAPIView):
    queryset = Tipo_Assessment.objects.all()
    serializer_class = TipoAssessmentSerializer

class TipoAssessmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tipo_Assessment.objects.all()
    serializer_class = TipoAssessmentSerializer

class AssessmentList(generics.ListCreateAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

class AssessmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

class ObjetivoAssessmentList(generics.ListCreateAPIView):
    queryset = Objetivo_Assessment.objects.all()
    serializer_class = ObjetivoAssessmentSerializer

class ObjetivoAssessmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Objetivo_Assessment.objects.all()
    serializer_class = ObjetivoAssessmentSerializer

class MomentoEvaluativoList(generics.ListCreateAPIView):
    queryset = Momento_Evaluativo.objects.all()
    serializer_class = MomentoEvaluativoSerializer

class MomentoEvaluativoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Momento_Evaluativo.objects.all()
    serializer_class = MomentoEvaluativoSerializer

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PerfilList(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class PerfilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class UsuarioPerfilList(generics.ListCreateAPIView):
    queryset = Usuario_Perfil.objects.all()
    serializer_class = UsuarioPerfilSerializer

class UsuarioPerfilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario_Perfil.objects.all()
    serializer_class = UsuarioPerfilSerializer

class UsuarioCursoList(generics.ListCreateAPIView):
    queryset = Usuario_Curso.objects.all()
    serializer_class = UsuarioCursoSerializer

class UsuarioCursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario_Curso.objects.all()
    serializer_class = UsuarioCursoSerializer

class EvaluacionList(generics.ListCreateAPIView):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer

class EvaluacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer

class VariablesConfiguracionList(generics.ListCreateAPIView):
    queryset = Variables_Configuracion.objects.all()
    serializer_class = VariablesConfiguracionSerializer

class VariablesConfiguracionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Variables_Configuracion.objects.all()
    serializer_class = VariablesConfiguracionSerializer

class BuscarObjetivosPorIdCompetenciaList(generics.ListCreateAPIView):
    serializer_class = ObjetivoSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Objetivo.objects.all()
        parametro = self.request.GET.get("q")
        if parametro:
            queryset = queryset.filter(competencia_objetivo__id_competencia__exact=parametro)
        return queryset

class ProfesorList(generics.ListCreateAPIView):
    queryset = Usuario.objects.filter(usuario_perfil__id_perfil__exact=1)
    serializer_class = UsuarioSerializer

class ProfesorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.filter(usuario_perfil__id_perfil__exact=1)
    serializer_class = UsuarioSerializer

class EstudianteList(generics.ListCreateAPIView):
    queryset = Usuario.objects.filter(usuario_perfil__id_perfil__exact=2)
    serializer_class = UsuarioSerializer

class EstudianteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.filter(usuario_perfil__id_perfil__exact=2)
    serializer_class = UsuarioSerializer

class BuscarVariablePorNombreList(generics.ListCreateAPIView):
    serializer_class = VariablesConfiguracionSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Variables_Configuracion.objects.all()
        parametro = self.request.GET.get("q")
        if parametro:
            queryset = queryset.filter(nombre__exact=parametro)
        return queryset
