# database_django

 # Importamos la libreria
from libreria.models import Libro

# Creamos un libro nuevo con el metodo create()
# insertamos los datos
Libro.objects.create(titulo="biblia", 
autor="no se",anio_publicacion=1, )
<Libro: Libro object (1)>
Libro.objects.create(titulo="libro2", 
autor="cualquiera",anio_publicacion=2020 )
<Libro: Libro object (2)>


# Actualizar y modificar el titulo
# buscamos el registro con get()
# guardamos los cambios con el metodo save()

Libro.objects.get(titulo="libro2")
<Libro: Libro object (2)>
cambiar = Libro.objects.get(titulo="libro2")
cambiar.titulo = "El principito"
cambiar.save()

libro = Libro.objects.get(titulo="biblia")
libro.disponibilidad = False
libro.save() #Metodo para guarda em base de datos

# Eliminar dato con metodo delete()
# obtenemos el dato con get()
libro3 = Libro.objects.get(titulo="libro3") instanciamos el dato
libro3.delete() eliminamos 
(1, {'libreria.Libro': 1})



• Indica qué campo actuaría como clave primaria por defecto.

pOR DEFECTO LA CLAVE PRIMARIA ES EL ID

• Explica cómo se definiría una clave primaria compuesta si se quisiera hacer manualmente.
Para lograr el mismo comportamiento de una clave primaria compuesta de forma manual y correcta en Django, se utiliza la opción unique_together (o UniqueConstraint) dentro de la subclase Meta.
SERIA DE ESTA MANERA
class Meta:
        # Esto obliga a que la combinación de título y autor sea ÚNICA en la base de datos
        unique_together = (('titulo', 'autor'),)



Link git https://github.com/kandylorena/database_django.git