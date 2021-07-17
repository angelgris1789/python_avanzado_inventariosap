#importo os y sys para setting y setup de app Django
import os
import sys


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventariosap.settings')
importer = sys.modules['__main__'].__spec__

#Genero línea en el caso que el importador sea pydoc
try:
    if importer.name == 'pydoc':
        import django
        django.setup()
except:
    pass
