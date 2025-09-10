from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializers import (
    AutorSerializer,
    EditorialSerializer,
    LibroSerializer,
    MiembroSerializer,
    PrestamoSerializer,
)

# ---------------- Autor ----------------
class AutorListCreateView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    # GET → listar todos los autores
    # POST → crear nuevo autor


class AutorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    # GET → obtener detalle de un autor
    # PUT → actualizar un autor
    # PATCH → actualizar parcialmente
    # DELETE → eliminar un autor


# ---------------- Editorial ----------------
class EditorialListCreateView(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    # GET → listar editoriales
    # POST → crear nueva editorial


class EditorialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    # GET → detalle editorial
    # PUT/PATCH → actualizar
    # DELETE → eliminar


# ---------------- Libro ----------------
class LibroListCreateView(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_autor', 'id_editorial']  
    # GET → listar libros (se puede filtrar ?id_autor=1 o ?id_editorial=2)
    # POST → crear libro


class LibroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    # GET → detalle de un libro
    # PUT/PATCH → actualizar libro
    # DELETE → eliminar libro


# ---------------- Miembro ----------------
class MiembroListCreateView(generics.ListCreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    # GET → listar miembros
    # POST → crear nuevo miembro


class MiembroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    # GET → detalle miembro
    # PUT/PATCH → actualizar miembro
    # DELETE → eliminar miembro


# ---------------- Prestamo ----------------
class PrestamoListCreateView(generics.ListCreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fecha_prestamo', 'id_miembro']  
    # GET → listar préstamos (se puede filtrar ?fecha_prestamo=YYYY-MM-DD o ?id_miembro=3)
    # POST → crear préstamo


class PrestamoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    # GET → detalle préstamo
    # PUT/PATCH → actualizar préstamo
    # DELETE → eliminar préstamo
