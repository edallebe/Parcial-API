from django.db import models

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'T001Autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'T002Editorial'
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    anio_publicacion = models.PositiveIntegerField()
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")
    id_editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name="libros")

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'T003Libro'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'


class Miembro(models.Model):
    id_miembro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_membresia = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'T004Miembro'
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'


class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="prestamos")
    id_miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE, related_name="prestamos")

    def __str__(self):
        return f"Préstamo de {self.id_libro} a {self.id_miembro}"

    class Meta:
        db_table = 'T005Prestamo'
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'
