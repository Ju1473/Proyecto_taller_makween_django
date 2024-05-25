

def upload_to_mecanicos(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        return 'mecanicos/Imagen {}.{}'.format(instance.pk, ext)
    else:
        count = instance.__class__.objects.count() + 1
        return 'mecanicos/Imagen {}.{}'.format(count, ext)

def upload_to_trabajos(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        return 'trabajos/Imagen {}.{}'.format(instance.pk, ext)
    else:
        count = instance.__class__.objects.count() + 1
        return 'trabajos/Imagen {}.{}'.format(count, ext)