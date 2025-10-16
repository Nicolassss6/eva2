from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente, Medico, Especialidad, ConsultaMedica, Tratamiento, Medicamento, RecetaMedica
from .forms import PacienteForm, MedicoForm, EspecialidadForm, ConsultaMedicaForm, TratamientoForm, MedicamentoForm, RecetaMedicaForm

# -----------------------------
# PACIENTES
# -----------------------------
def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/listar.html', {'pacientes': pacientes})

def crear_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pacientes_listar')
    return render(request, 'pacientes/crear.html', {'form': form})

def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('pacientes_listar')
    return render(request, 'pacientes/editar.html', {'form': form})

def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('pacientes_listar')


# -----------------------------
# MÉDICOS
# -----------------------------
def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos/listar.html', {'medicos': medicos})

def crear_medico(request):
    form = MedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('medicos_listar')
    return render(request, 'medicos/crear.html', {'form': form})

def editar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    form = MedicoForm(request.POST or None, instance=medico)
    if form.is_valid():
        form.save()
        return redirect('medicos_listar')
    return render(request, 'medicos/editar.html', {'form': form})

def eliminar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    medico.delete()
    return redirect('medicos_listar')


# -----------------------------
# ESPECIALIDADES
# -----------------------------
def listar_especialidades(request):
    especialidades = Especialidad.objects.all()
    return render(request, 'especialidades/listar.html', {'especialidades': especialidades})

def crear_especialidad(request):
    form = EspecialidadForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('especialidades_listar')
    return render(request, 'especialidades/crear.html', {'form': form})

def editar_especialidad(request, id):
    especialidad = get_object_or_404(Especialidad, id=id)
    form = EspecialidadForm(request.POST or None, instance=especialidad)
    if form.is_valid():
        form.save()
        return redirect('especialidades_listar')
    return render(request, 'especialidades/editar.html', {'form': form})

def eliminar_especialidad(request, id):
    especialidad = get_object_or_404(Especialidad, id=id)
    especialidad.delete()
    return redirect('especialidades_listar')


# -----------------------------
# CONSULTAS MÉDICAS
# -----------------------------
def listar_consultas(request):
    consultas = ConsultaMedica.objects.all()
    return render(request, 'consultas/listar.html', {'consultas': consultas})

def crear_consulta(request):
    form = ConsultaMedicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('consultas_listar')
    return render(request, 'consultas/crear.html', {'form': form})

def editar_consulta(request, id):
    consulta = get_object_or_404(ConsultaMedica, id=id)
    form = ConsultaMedicaForm(request.POST or None, instance=consulta)
    if form.is_valid():
        form.save()
        return redirect('consultas_listar')
    return render(request, 'consultas/editar.html', {'form': form})

def eliminar_consulta(request, id):
    consulta = get_object_or_404(ConsultaMedica, id=id)
    consulta.delete()
    return redirect('consultas_listar')


# -----------------------------
# TRATAMIENTOS
# -----------------------------
def listar_tratamientos(request):
    tratamientos = Tratamiento.objects.all()
    return render(request, 'tratamientos/listar.html', {'tratamientos': tratamientos})

def crear_tratamiento(request):
    form = TratamientoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tratamientos_listar')
    return render(request, 'tratamientos/crear.html', {'form': form})

def editar_tratamiento(request, id):
    tratamiento = get_object_or_404(Tratamiento, id=id)
    form = TratamientoForm(request.POST or None, instance=tratamiento)
    if form.is_valid():
        form.save()
        return redirect('tratamientos_listar')
    return render(request, 'tratamientos/editar.html', {'form': form})

def eliminar_tratamiento(request, id):
    tratamiento = get_object_or_404(Tratamiento, id=id)
    tratamiento.delete()
    return redirect('tratamientos_listar')


# -----------------------------
# MEDICAMENTOS
# -----------------------------
def listar_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamentos/listar.html', {'medicamentos': medicamentos})

def crear_medicamento(request):
    form = MedicamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('medicamentos_listar')
    return render(request, 'medicamentos/crear.html', {'form': form})

def editar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    form = MedicamentoForm(request.POST or None, instance=medicamento)
    if form.is_valid():
        form.save()
        return redirect('medicamentos_listar')
    return render(request, 'medicamentos/editar.html', {'form': form})

def eliminar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    medicamento.delete()
    return redirect('medicamentos_listar')


# -----------------------------
# RECETAS MÉDICAS
# -----------------------------
def listar_recetas(request):
    recetas = RecetaMedica.objects.all()
    return render(request, 'recetas/listar.html', {'recetas': recetas})

def crear_receta(request):
    form = RecetaMedicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('recetas_listar')
    return render(request, 'recetas/crear.html', {'form': form})

def editar_receta(request, id):
    receta = get_object_or_404(RecetaMedica, id=id)
    form = RecetaMedicaForm(request.POST or None, instance=receta)
    if form.is_valid():
        form.save()
        return redirect('recetas_listar')
    return render(request, 'recetas/editar.html', {'form': form})

def eliminar_receta(request, id):
    receta = get_object_or_404(RecetaMedica, id=id)
    receta.delete()
    return redirect('recetas_listar')
