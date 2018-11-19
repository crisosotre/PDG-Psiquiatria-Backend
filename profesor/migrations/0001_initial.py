# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id_assessment', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('abreviatura', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id_competencia', models.IntegerField(primary_key=True, serialize=False)),
                ('desc_competencia', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Competencia_Curso',
            fields=[
                ('id_comp_cur', models.IntegerField(primary_key=True, serialize=False)),
                ('id_competencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Competencia')),
            ],
        ),
        migrations.CreateModel(
            name='Competencia_Objetivo',
            fields=[
                ('id_comp_obj', models.IntegerField(primary_key=True, serialize=False)),
                ('id_competencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Competencia')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id_evaluacion', models.IntegerField(primary_key=True, serialize=False)),
                ('calificacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Momento_Evaluativo',
            fields=[
                ('id_momento_evaluativo', models.IntegerField(primary_key=True, serialize=False)),
                ('ponderacion', models.DecimalField(decimal_places=2, max_digits=3)),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id_objetivo', models.IntegerField(primary_key=True, serialize=False)),
                ('desc_objetivo', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Objetivo_Assessment',
            fields=[
                ('id_obj_assess', models.IntegerField(primary_key=True, serialize=False)),
                ('id_assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Assessment')),
                ('id_objetivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Objetivo')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id_perfil', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Assessment',
            fields=[
                ('id_tipo_assessment', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Objetivo',
            fields=[
                ('id_tipo_objetivo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=500)),
                ('url_foto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Curso',
            fields=[
                ('id_usuario_curso', models.IntegerField(primary_key=True, serialize=False)),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Curso')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Perfil',
            fields=[
                ('id_usuario_perfil', models.IntegerField(primary_key=True, serialize=False)),
                ('id_perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Perfil')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Variables_Configuracion',
            fields=[
                ('id_var_conf', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.AddField(
            model_name='objetivo',
            name='id_tipo_objetivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Tipo_Objetivo'),
        ),
        migrations.AddField(
            model_name='momento_evaluativo',
            name='id_obj_assess',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Objetivo_Assessment'),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='id_momento_evaluativo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Momento_Evaluativo'),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='id_usuario_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Usuario_Curso'),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='id_usuario_perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Usuario_Perfil'),
        ),
        migrations.AddField(
            model_name='competencia_objetivo',
            name='id_objetivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Objetivo'),
        ),
        migrations.AddField(
            model_name='competencia_curso',
            name='id_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Curso'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='id_tipo_assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.Tipo_Assessment'),
        ),
    ]