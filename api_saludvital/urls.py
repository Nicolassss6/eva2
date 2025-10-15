from django.urls import path, include
from rest_framework import routers
from .views import (
    EspecialidadViewSet, MedicoViewSet, PacienteViewSet,
    ConsultaMedicaViewSet, TratamientoViewSet,
    MedicamentoViewSet, RecetaMedicaViewSet, EstadoConsultaViewSet
)

router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'estados', EstadoConsultaViewSet)
router.register(r'consultas', ConsultaMedicaViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'recetas', RecetaMedicaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
