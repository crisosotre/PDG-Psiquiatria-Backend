# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Competencia(models.Model):
    id_competencia = models.IntegerField(primary_key=True)
    desc_competencia = models.CharField(max_length=400)

class Tipo_Objetivo(models.Model):
    id_tipo_objetivo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Objetivo(models.Model):
    id_objetivo = models.IntegerField(primary_key=True)
    desc_objetivo = models.CharField(max_length=400)
    id_tipo_objetivo = models.ForeignKey(Tipo_Objetivo, on_delete=models.CASCADE)
    
class Competencia_Objetivo(models.Model):
    id_comp_obj = models.IntegerField(primary_key=True)
    id_competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    id_objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE)

class Curso(models.Model):
    id_curso = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Competencia_Curso(models.Model):
    id_comp_cur = models.IntegerField(primary_key=True)
    id_competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Tipo_Assessment(models.Model):
    id_tipo_assessment = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Assessment(models.Model):
    id_assessment = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=10)
    id_tipo_assessment = models.ForeignKey(Tipo_Assessment, on_delete=models.CASCADE)

class Objetivo_Assessment(models.Model):
    id_obj_assess = models.IntegerField(primary_key=True)
    id_objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE)
    id_assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)

class Momento_Evaluativo(models.Model):
    id_momento_evaluativo = models.IntegerField(primary_key=True)
    ponderacion = models.DecimalField(max_digits=3, decimal_places=2)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_obj_assess = models.ForeignKey(Objetivo_Assessment, on_delete=models.CASCADE)

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=500)
    url_foto = models.CharField(max_length=100)

class Perfil(models.Model):
    id_perfil = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Usuario_Perfil(models.Model):
    id_usuario_perfil = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

class Usuario_Curso(models.Model):
    id_usuario_curso = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Evaluacion(models.Model):
    id_evaluacion = models.IntegerField(primary_key=True)
    calificacion = models.IntegerField()
    id_momento_evaluativo = models.ForeignKey(Momento_Evaluativo, on_delete=models.CASCADE)
    id_usuario_curso = models.ForeignKey(Usuario_Curso, on_delete=models.CASCADE)
    id_usuario_perfil = models.ForeignKey(Usuario_Perfil, on_delete=models.CASCADE)

class Variables_Configuracion(models.Model):
    id_var_conf = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=3, decimal_places=2)

