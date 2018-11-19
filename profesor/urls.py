from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^competencia$', views.CompetenciaList.as_view()),
    url(r'competencia/(?P<pk>[0-9]+)$', views.CompetenciaDetail.as_view()),

    url(r'^tipo_objetivo$', views.TipoObjetivoList.as_view()),
    url(r'tipo_objetivo/(?P<pk>[0-9]+)$', views.TipoObjetivoDetail.as_view()),

    url(r'^objetivo$', views.ObjetivoList.as_view()),
    url(r'objetivo/(?P<pk>[0-9]+)$', views.ObjetivoDetail.as_view()),

    url(r'^competencia_objetivo$', views.CompetenciaObjetivoList.as_view()),
    url(r'competencia_objetivo/(?P<pk>[0-9]+)$', views.CompetenciaObjetivoDetail.as_view()),

    url(r'^curso$', views.CursoList.as_view()),
    url(r'curso/(?P<pk>[0-9]+)$', views.CursoDetail.as_view()),

    url(r'^competencia_curso$', views.CompetenciaCursoList.as_view()),
    url(r'competencia_curso/(?P<pk>[0-9]+)$', views.CompetenciaCursoDetail.as_view()),

    url(r'^tipo_assessment$', views.TipoAssessmentList.as_view()),
    url(r'tipo_assessment/(?P<pk>[0-9]+)$', views.TipoAssessmentDetail.as_view()),

    url(r'^assessment$', views.AssessmentList.as_view()),
    url(r'assessment/(?P<pk>[0-9]+)$', views.AssessmentDetail.as_view()),

    url(r'^objetivo_assessment$', views.ObjetivoAssessmentList.as_view()),
    url(r'objetivo_assessment/(?P<pk>[0-9]+)$', views.ObjetivoAssessmentDetail.as_view()),

    url(r'^momento_evaluativo$', views.MomentoEvaluativoList.as_view()),
    url(r'momento_evaluativo/(?P<pk>[0-9]+)$', views.MomentoEvaluativoDetail.as_view()),

    url(r'^usuario$', views.UsuarioList.as_view()),
    url(r'usuario/(?P<pk>[0-9]+)$', views.UsuarioDetail.as_view()),

    url(r'^perfil$', views.PerfilList.as_view()),
    url(r'perfil/(?P<pk>[0-9]+)$', views.PerfilDetail.as_view()),

    url(r'^usuario_perfil$', views.UsuarioPerfilList.as_view()),
    url(r'usuario_perfil/(?P<pk>[0-9]+)$', views.UsuarioPerfilDetail.as_view()),

    url(r'^usuario_curso$', views.UsuarioCursoList.as_view()),
    url(r'usuario_curso/(?P<pk>[0-9]+)$', views.UsuarioCursoDetail.as_view()),

    url(r'^evaluacion$', views.EvaluacionList.as_view()),
    url(r'evaluacion/(?P<pk>[0-9]+)$', views.EvaluacionDetail.as_view()),

    url(r'^variables_configuracion$', views.VariablesConfiguracionList.as_view()),
    url(r'variables_configuracion/(?P<pk>[0-9]+)$', views.VariablesConfiguracionDetail.as_view()),

    url(r'^buscar_objetivos', views.BuscarObjetivosPorIdCompetenciaList.as_view()),

    url(r'^profesor$', views.ProfesorList.as_view()),
    url(r'profesor/(?P<pk>[0-9]+)$', views.ProfesorDetail.as_view()),

    url(r'^estudiante$', views.EstudianteList.as_view()),
    url(r'estudiante/(?P<pk>[0-9]+)$', views.EstudianteDetail.as_view()),

    url(r'^variable_nombre', views.BuscarVariablePorNombreList.as_view()),
]