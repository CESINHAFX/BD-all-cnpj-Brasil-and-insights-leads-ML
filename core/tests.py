from django.test import TestCase
from django.test import TestCase
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # Substitua "myproject" pelo nome do seu projeto Django
from core.models import CNAE
from django.core.wsgi import get_wsgi_application
# Substitua "some_module" pelo módulo correto que você deseja importar
from django.core.management import call_command

#bibliotecas e frameworks utilizado no material
# Create your tests here.
#testar a importação de CNAE
def clean_data():
    try:
        CNAE.objects.all().delete()
    except Exception as e:
        print(f"Erro ao limpar os dados: {e}")
def ImportCnaeTestCase(TestCase):
    try:
        clean_data()
        call_command('import_cnae')#como faz para ler somente as 5 primeiras linhas?
        cnaes = CNAE.objects.filter(code='0111301',description="Cultivo de arroz")
        print(f"Registros encontrados: {cnaes.count()}")
        self.assertTrue(cnaes.exists())
    except Exception as e:
        print(f"Erro ao limpar os dados antes do teste: {e}")





