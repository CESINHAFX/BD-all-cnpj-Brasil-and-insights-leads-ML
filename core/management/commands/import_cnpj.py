import zipfile

from core.models import Company
import csv
from decimal import Decimal
from django.db import transaction
companies = []
total = 0
with zipfile.ZipFile(open('/home/arch/Downloads/BD-all-cnpj-Brasil-and-insights-leads-ML/data/cnpj/2026-01/Cnaes.zip')) as zip_ref:
    for row in zip_ref.namelist():
        with zip_ref.open(row) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                company = Company(
                    cnpj=row['cnpj'],
                    legal_name=row['razao_social'],
                    trade_name=row['nome_fantasia'],
                    date_opened=row['data_abertura'] if row['data_abertura'] else None,
                    registration_status=row['situacao_cadastral'],
                    capital_social=Decimal(row['capital_social'].replace(',', '.')) if row['capital_social'] else None,
                    legal_nature_code=row['codigo_natureza_juridica'],
                    address=row['logradouro'],
                    city=row['municipio'],
                    state=row['uf'],
                    zip_code=row['cep'],
                    phone_number=row['telefone'] if row['telefone'] else None,
                    email=row['email'] if row['email'] else None,
                    website=row['site'] if row['site'] else None
                )
                companies.append(company)

    if len(companies) == 5000:
            with transaction.atomic():
                Company.objects.bulk_create(companies)
                total += len(companies)
            companies = []
            print(total)

if len(companies) > 0:
    with transaction.atomic():
        Company.objects.bulk_create(companies)
        total += len(companies)
  

    companies = []
    print(total)
                


