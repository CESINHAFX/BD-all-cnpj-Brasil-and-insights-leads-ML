import csv
import io
import zipfile

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import CNAE


class Command(BaseCommand):
    def handle(self, *args, **options):
        archive_path = settings.BASE_DIR / "data" / "cnpj" / "2026-01" / "Cnaes.zip"
        cnae_batch = []
        batch_size = 1000

        with zipfile.ZipFile(archive_path) as archive:
            for member_name in archive.namelist():
                with archive.open(member_name) as binary_file:
                    text_file = io.TextIOWrapper(
                        binary_file,
                        encoding="latin1",
                        newline="",
                    )
                    reader = csv.reader(text_file, delimiter=";")

                    for raw in reader:
                        if len(raw) != 2:
                            continue
                        cnae_batch.append(CNAE(
                            code=raw[0],
                            description=raw[1],
                        ))
                        if len(cnae_batch) >= batch_size:
                            with transaction.atomic():
                                CNAE.objects.bulk_create(
                                    cnae_batch,
                                    ignore_conflicts=True,
                                )
                            cnae_batch.clear()
        if cnae_batch:
            with transaction.atomic():
                CNAE.objects.bulk_create(
                    cnae_batch,
                    ignore_conflicts=True,
                )
        self.stdout.write(self.style.SUCCESS("CNAE import completed."))


