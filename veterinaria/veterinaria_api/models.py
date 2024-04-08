from django.db import models


class Estado(models.Model):
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Propietario(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.EmailField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    historial_medico = models.TextField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)
    especializacion = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Sala(models.Model):
    numero = models.IntegerField(unique=True)
    tipo = models.CharField(max_length=255)
    capacidad = models.IntegerField()

    def __str__(self):
        return f"Sala {self.numero} - {self.tipo}"


class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    observaciones = models.TextField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cita para {self.paciente} el {self.fecha_hora}"


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.CharField(max_length=255)
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f"Consulta {self.motivo} - {self.fecha}"
