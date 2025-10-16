from django.urls import path
from . import views

urlpatterns = [
    # PACIENTES
    path('pacientes/', views.listar_pacientes, name='pacientes_listar'),
    path('pacientes/crear/', views.crear_paciente, name='pacientes_crear'),
    path('pacientes/editar/<int:id>/', views.editar_paciente, name='pacientes_editar'),
    path('pacientes/eliminar/<int:id>/', views.eliminar_paciente, name='pacientes_eliminar'),

    # MÉDICOS
    path('medicos/', views.listar_medicos, name='medicos_listar'),
    path('medicos/crear/', views.crear_medico, name='medicos_crear'),
    path('medicos/editar/<int:id>/', views.editar_medico, name='medicos_editar'),
    path('medicos/eliminar/<int:id>/', views.eliminar_medico, name='medicos_eliminar'),

    # ESPECIALIDADES
    path('especialidades/', views.listar_especialidades, name='especialidades_listar'),
    path('especialidades/crear/', views.crear_especialidad, name='especialidades_crear'),
    path('especialidades/editar/<int:id>/', views.editar_especialidad, name='especialidades_editar'),
    path('especialidades/eliminar/<int:id>/', views.eliminar_especialidad, name='especialidades_eliminar'),

    # CONSULTAS MÉDICAS
    path('consultas/', views.listar_consultas, name='consultas_listar'),
    path('consultas/crear/', views.crear_consulta, name='consultas_crear'),
    path('consultas/editar/<int:id>/', views.editar_consulta, name='consultas_editar'),
    path('consultas/eliminar/<int:id>/', views.eliminar_consulta, name='consultas_eliminar'),

    # TRATAMIENTOS
    path('tratamientos/', views.listar_tratamientos, name='tratamientos_listar'),
    path('tratamientos/crear/', views.crear_tratamiento, name='tratamientos_crear'),
    path('tratamientos/editar/<int:id>/', views.editar_tratamiento, name='tratamientos_editar'),
    path('tratamientos/eliminar/<int:id>/', views.eliminar_tratamiento, name='tratamientos_eliminar'),

    # MEDICAMENTOS
    path('medicamentos/', views.listar_medicamentos, name='medicamentos_listar'),
    path('medicamentos/crear/', views.crear_medicamento, name='medicamentos_crear'),
    path('medicamentos/editar/<int:id>/', views.editar_medicamento, name='medicamentos_editar'),
    path('medicamentos/eliminar/<int:id>/', views.eliminar_medicamento, name='medicamentos_eliminar'),

    # RECETAS MÉDICAS
    path('recetas/', views.listar_recetas, name='recetas_listar'),
    path('recetas/crear/', views.crear_receta, name='recetas_crear'),
    path('recetas/editar/<int:id>/', views.editar_receta, name='recetas_editar'),
    path('recetas/eliminar/<int:id>/', views.eliminar_receta, name='recetas_eliminar'),
]
