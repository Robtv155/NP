# \* Ejercicio

1. Crear nuevo modelo (libre elección , ej. `comentarios`, `categoria`), con un enlace o ForeignKey a `Post`.
2. Comprobar en `Shell` que se ha creado correctamente
3. Asociar los modelos creados con el `User` logueado
4. Comprobar en `Shell` las asociaciones

> > > from nueva_app.models import Post, Tag
> > > Tag.objects.create(name="Django")
