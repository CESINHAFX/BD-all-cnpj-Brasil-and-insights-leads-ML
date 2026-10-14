import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory

from django.core.management import call_command
from django.test import TestCase, override_settings

from core.models import CNAE


class ImportCnaeTestCase(TestCase):
    def test_import_cnae(self):
        with TemporaryDirectory() as temp_root:
            archive_path = Path(temp_root) / "data" / "cnpj" / "2026-01" / "Cnaes.zip"
            archive_path.parent.mkdir(parents=True)
            conteudo = (
                "1231234;cultivo de açai\n"
                "1234567;cultivo trigo\n"
                "7894561;cultivo cana;combustivel\n"
            )
            with zipfile.ZipFile(archive_path, "w") as zipf:
                zipf.writestr("Cnaes.csv", conteudo.encode("latin-1"))

            with override_settings(BASE_DIR=Path(temp_root)):
                call_command("import_cnae")

        self.assertTrue(CNAE.objects.filter(code="1231234", description="cultivo de açai").exists())
        self.assertTrue(CNAE.objects.filter(code="1234567", description="cultivo trigo").exists())
        self.assertFalse(CNAE.objects.filter(code="7894561").exists())

    def test_sec_Pathtransversal_import_cnae(self):
        #criou o arquivo malicioso, o conteudo, e manteve em latin-1 para evitar diretorios ".../"
        with TemporaryDirectory() as temp_root:
            #local do diretorio temporario do TemporaryDirectory
            archive_path = Path(temp_root) / "data" / "cnpj" / "2026-01" / "Cnaes.zip"
            archive_path.parent.mkdir(parents=True)
            conteudo = (
                "1234567;fora.csv\n"
            )
            #usa a função zipzip para criar o arquivo e adicionar o conteúdo dentro do zip, com latin 1
            with zipfile.ZipFile(archive_path, "w") as zipf:
                zipf.writestr("../fora.csv", conteudo.encode("latin-1"))
            #override faz usar o caminho temporário como BASE_DIR, e importa os dados com o codigo import_cnae
            with override_settings(BASE_DIR=Path(temp_root)):
                call_command("import_cnae")
            #verifica se o arquivo n foi gravado fora do diretorio definido pelo arquive_path
            self.assertFalse((Path(temp_root).parent / "fora.csv").exists())
            #verificar os dados 
            self.assertTrue(CNAE.objects.filter(code="1234567", description="fora.csv").exists())

    def test_valintegration_import_cnae(self):
        with TemporaryDirectory() as temp_root:
            archive_path = Path(temp_root) / "data" / "cnpj" / "2026-01" / "Cnaes.zip"
            archive_path.parent.mkdir(parents=True)
            conteudo = (
                "12312345;cultivo de açai\n"
            )
            with zipfile.ZipFile(archive_path, "w") as zipf:
                zipf.writestr("Cnaes.csv", conteudo.encode("latin-1"))

            with override_settings(BASE_DIR=Path(temp_root)):
                call_command("import_cnae")

        self.assertFalse(CNAE.objects.filter(code="12312345", description="cultivo de açai").exists())
    def test_sqlinjection_import_cnae_invalid_code(self):
        with TemporaryDirectory() as temp_root:
            archive_path = Path(temp_root) / "data" / "cnpj" / "2026-01" / "Cnaes.zip"
            archive_path.parent.mkdir(parents=True)
            conteudo = (
                '1234567;"\')DROP TABLE CNAE;--"\n'
            )
            with zipfile.ZipFile(archive_path, "w") as zipf:
                zipf.writestr("Cnaes.csv", conteudo.encode("latin-1"))

            with override_settings(BASE_DIR=Path(temp_root)):
                call_command("import_cnae")

        self.assertTrue(
            CNAE.objects.filter(
                code="1234567",
                description="\')DROP TABLE CNAE;--"
            ).exists()
        )
    def test_indempotencia_import_cnae(self):
        with TemporaryDirectory() as temp_root:
            archive_path = Path(temp_root) / "data" / "cnpj" / "2026-01" / "Cnaes.zip"
            archive_path.parent.mkdir(parents=True)
            conteudo = (
                "2345678;criador de galinha\n"
            )
            with zipfile.ZipFile(archive_path, "w") as zipf:
                zipf.writestr("Cnaes.csv", conteudo.encode("latin-1"))
                

            with override_settings(BASE_DIR=Path(temp_root)):
                
                call_command("import_cnae")
                antigo = list(CNAE.objects.values_list("code", "description"))

            conteudo = (
                "2345678;criador de frango\n"
            )
            with zipfile.ZipFile(archive_path, "w") as zipf:
                zipf.writestr("Cnaes.csv", conteudo.encode("latin-1"))
            with override_settings(BASE_DIR=Path(temp_root)):
                call_command("import_cnae")
                novo = list(CNAE.objects.values_list("code", "description"))
            self.assertEqual(len(antigo), 1)
            self.assertEqual(len(novo), 1)
            self.assertEqual(antigo , novo)
            self.assertEqual(novo, [("2345678", "criador de galinha")])