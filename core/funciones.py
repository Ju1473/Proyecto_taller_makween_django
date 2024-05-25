

def custom_upload_to(folder):
    def _upload_to(instance, filename):
        # Obtiene la extensión del archivo
        ext = filename.split('.')[-1]
        # Genera el nombre del archivo
        if instance.pk:
            # Si el objeto ya tiene una clave primaria, significa que ya está en la base de datos
            # Asigna un nombre basado en la cantidad de imágenes ya existentes más uno
            return '{}/Imagen {}.{}'.format(folder, instance.pk, ext)
        else:
            # Si el objeto aún no tiene una clave primaria, significa que es nuevo
            # Asigna un nombre basado en la cantidad total de objetos más uno
            count = instance.__class__.objects.count() + 1
            return '{}/Imagen {}.{}'.format(folder, count, ext)
    return _upload_to