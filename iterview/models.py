from django.db import models
#Modelos de las clases

#empresa
class Empresa(models.Model):
		nombre_empresa = models.CharField('empresa', max_length=60, default='Nombre Empresa')

		def __str__(self):
			return self.nombre_empresa


#entrevistado
class Entrevistado(models.Model): 
		nombre = models.CharField('nombre', max_length=60)
		apellido = models.CharField('apellido', max_length=60)
		email = models.EmailField('direccion email', max_length=128)
		contraseña = models.CharField('contraseña', max_length=60)

		def __str__(self):
			return self.nombre + ' ' + self.apellido


#entrevistador
class Entrevistador(models.Model): 
		nombre = models.CharField('nombre', max_length=60)
		apellido = models.CharField('apellido', max_length=60)
		rol = models.CharField('rol', max_length=60)
		empresa = models.ForeignKey(Empresa, blank=True, null=True, on_delete=models.DO_NOTHING)
		email = models.EmailField('direccion email', max_length=128)
		contraseña = models.CharField('contrase単a', max_length=60)

		def __str__(self):
			return self.nombre


#Reunion
class Reunion(models.Model):
		cantidad = models.PositiveIntegerField()
		duracion = models.PositiveIntegerField()
		link = models.URLField('link reunion', max_length=280, default='ejemplo.com')

		def __str__(self):
			return str(self.cantidad) + ',' + str(self.duracion)

#agendar
class Agendar(models.Model):
		nombre_agenda = models.CharField('Nombre', max_length=60)
		lenguaje_programacion = models.CharField('Lenguaje programación', max_length=60)
		fecha = models.DateTimeField('Fecha reunión')
		entrevistado = models.ForeignKey(Entrevistado, blank=True, null=True, on_delete=models.DO_NOTHING)
		entrevistador = models.ForeignKey(Entrevistador, blank=True, null=True, on_delete=models.DO_NOTHING)

		def __str__(self):
			return str(self.nombre_agenda) + " / " +str(self.lenguaje_programacion)