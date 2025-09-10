# 📚 Documentación del Proyecto API Biblioteca

Este proyecto es una **API REST** construida con **Django y Django REST Framework (DRF)**.  
El objetivo es gestionar una **biblioteca**, incluyendo autores, editoriales, libros, miembros y préstamos.  

## Autor
Edwin Alexis Leiva Bello

---

## 🗄️ Modelos de Datos

1. **Autor**
   - `id_autor` (PK)
   - `nombre`
   - `apellido`
   - `biografia` (opcional)

2. **Editorial**
   - `id_editorial` (PK)
   - `nombre`
   - `direccion`
   - `telefono` (opcional)

3. **Libro**
   - `id_libro` (PK)
   - `titulo`
   - `resumen`
   - `isbn` (único)
   - `anio_publicacion`
   - `id_autor` (FK → Autor)
   - `id_editorial` (FK → Editorial)

4. **Miembro**
   - `id_miembro` (PK)
   - `nombre`
   - `apellido`
   - `email` (único)
   - `fecha_membresia`

5. **Préstamo**
   - `id_prestamo` (PK)
   - `fecha_prestamo`
   - `fecha_devolucion` (opcional)
   - `id_libro` (FK → Libro)
   - `id_miembro` (FK → Miembro)

---

## 🔗 Endpoints de la API

Base URL:
https://documenter.getpostman.com/view/48087758/2sB3HnMLmd 

### Autor
- `GET /autores/` → Lista autores  
- `POST /autores/` → Crear autor  
- `GET /autores/{id}/` → Detalle de un autor  
- `PUT /autores/{id}/` → Actualizar autor  
- `DELETE /autores/{id}/` → Eliminar autor  

### Editorial
- `GET /editoriales/`  
- `POST /editoriales/`  
- `GET /editoriales/{id}/`  
- `PUT /editoriales/{id}/`  
- `DELETE /editoriales/{id}/`  

### Libro
- `GET /libros/`  
  - Filtros: `?id_autor=1`, `?id_editorial=2`  
- `POST /libros/`  
- `GET /libros/{id}/`  
- `PUT /libros/{id}/`  
- `DELETE /libros/{id}/`  

### Miembro
- `GET /miembros/`  
- `POST /miembros/`  
- `GET /miembros/{id}/`  
- `PUT /miembros/{id}/`  
- `DELETE /miembros/{id}/`  

### Préstamo
- `GET /prestamos/`  
  - Filtros: `?fecha_prestamo=YYYY-MM-DD`, `?id_miembro=3`  
- `POST /prestamos/`  
- `GET /prestamos/{id}/`  
- `PUT /prestamos/{id}/`  
- `DELETE /prestamos/{id}/`  

---