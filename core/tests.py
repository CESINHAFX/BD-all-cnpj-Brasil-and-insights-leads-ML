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