from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),

    # Pacientes
    path('pacientes/', views.listar_pacientes, name='pacientes_listar'),
    path('pacientes/crear/', views.crear_paciente, name='crear_paciente'),
    path('pacientes/editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:id>/', views.eliminar_paciente, name='eliminar_paciente'),

    # Médicos
    path('medicos/', views.listar_medicos, name='medicos_listar'),
    path('medicos/crear/', views.crear_medico, name='crear_medico'),
    path('medicos/editar/<int:id>/', views.editar_medico, name='editar_medico'),
    path('medicos/eliminar/<int:id>/', views.eliminar_medico, name='eliminar_medico'),

    # Especialidades
    path('especialidades/', views.listar_especialidades, name='especialidades_listar'),
    path('especialidades/crear/', views.crear_especialidad, name='crear_especialidad'),
    path('especialidades/editar/<int:id>/', views.editar_especialidad, name='editar_especialidad'),
    path('especialidades/eliminar/<int:id>/', views.eliminar_especialidad, name='eliminar_especialidad'),

    # Consultas
    path('consultas/', views.listar_consultas, name='consultas_listar'),
    path('consultas/crear/', views.crear_consulta, name='crear_consulta'),
    path('consultas/editar/<int:id>/', views.editar_consulta, name='editar_consulta'),
    path('consultas/eliminar/<int:id>/', views.eliminar_consulta, name='eliminar_consulta'),

    # Tratamientos
    path('tratamientos/', views.listar_tratamientos, name='tratamientos_listar'),
    path('tratamientos/crear/', views.crear_tratamiento, name='crear_tratamiento'),
    path('tratamientos/editar/<int:id>/', views.editar_tratamiento, name='editar_tratamiento'),
    path('tratamientos/eliminar/<int:id>/', views.eliminar_tratamiento, name='eliminar_tratamiento'),

    # Medicamentos
    path('medicamentos/', views.listar_medicamentos, name='medicamentos_listar'),
    path('medicamentos/crear/', views.crear_medicamento, name='crear_medicamento'),
    path('medicamentos/editar/<int:id>/', views.editar_medicamento, name='editar_medicamento'),
    path('medicamentos/eliminar/<int:id>/', views.eliminar_medicamento, name='eliminar_medicamento'),

    # Recetas médicas
    path('recetas/', views.listar_recetas, name='recetas_listar'),
    path('recetas/crear/', views.crear_receta, name='crear_receta'),
    path('recetas/editar/<int:id>/', views.editar_receta, name='editar_receta'),
    path('recetas/eliminar/<int:id>/', views.eliminar_receta, name='eliminar_receta'),
]
