from django.urls import path
from . import views

urlpatterns = [
    # CRUD Pacientes
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/crear/', views.crear_paciente, name='crear_paciente'),
    path('pacientes/editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:id>/', views.eliminar_paciente, name='eliminar_paciente'),

    # CRUD Médicos
    path('medicos/', views.listar_medicos, name='listar_medicos'),
    path('medicos/crear/', views.crear_medico, name='crear_medico'),
    path('medicos/editar/<int:id>/', views.editar_medico, name='editar_medico'),
    path('medicos/eliminar/<int:id>/', views.eliminar_medico, name='eliminar_medico'),

    # CRUD Especialidades
    path('especialidades/', views.listar_especialidades, name='listar_especialidades'),
    path('especialidades/crear/', views.crear_especialidad, name='crear_especialidad'),
    path('especialidades/editar/<int:id>/', views.editar_especialidad, name='editar_especialidad'),
    path('especialidades/eliminar/<int:id>/', views.eliminar_especialidad, name='eliminar_especialidad'),

    # CRUD Consultas Médicas
    path('consultas/', views.listar_consultas, name='listar_consultas'),
    path('consultas/crear/', views.crear_consulta, name='crear_consulta'),
    path('consultas/editar/<int:id>/', views.editar_consulta, name='editar_consulta'),
    path('consultas/eliminar/<int:id>/', views.eliminar_consulta, name='eliminar_consulta'),

    # CRUD Tratamientos
    path('tratamientos/', views.listar_tratamientos, name='listar_tratamientos'),
    path('tratamientos/crear/', views.crear_tratamiento, name='crear_tratamiento'),
    path('tratamientos/editar/<int:id>/', views.editar_tratamiento, name='editar_tratamiento'),
    path('tratamientos/eliminar/<int:id>/', views.eliminar_tratamiento, name='eliminar_tratamiento'),

    # CRUD Medicamentos
    path('medicamentos/', views.listar_medicamentos, name='listar_medicamentos'),
    path('medicamentos/crear/', views.crear_medicamento, name='crear_medicamento'),
    path('medicamentos/editar/<int:id>/', views.editar_medicamento, name='editar_medicamento'),
    path('medicamentos/eliminar/<int:id>/', views.eliminar_medicamento, name='eliminar_medicamento'),

    # CRUD Recetas Médicas
    path('recetas/', views.listar_recetas, name='listar_recetas'),
    path('recetas/crear/', views.crear_receta, name='crear_receta'),
    path('recetas/editar/<int:id>/', views.editar_receta, name='editar_receta'),
    path('recetas/eliminar/<int:id>/', views.eliminar_receta, name='eliminar_receta'),
]


















