from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import (
    Especialidad, Medico, Paciente,
    ConsultaMedica, Tratamiento,
    Medicamento, RecetaMedica, EstadoConsulta
)
from .serializers import (
    EspecialidadSerializer, MedicoSerializer, PacienteSerializer,
    ConsultaMedicaSerializer, TratamientoSerializer,
    MedicamentoSerializer, RecetaMedicaSerializer, EstadoConsultaSerializer
)

# -----------------------------
# VIEWS - API CRUD
# -----------------------------

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class EstadoConsultaViewSet(viewsets.ModelViewSet):
    queryset = EstadoConsulta.objects.all()
    serializer_class = EstadoConsultaSerializer


class ConsultaMedicaViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer


class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer


class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


class RecetaMedicaViewSet(viewsets.ModelViewSet):
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer
