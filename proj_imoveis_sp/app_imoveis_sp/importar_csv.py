# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
import csv
##from app_imoveis_sp.models import imovel
from app_imoveis_sp.models import imovel
def importar_imoveis (caminho):
    with open(caminho, 'r') as file: 
        leitor = csv.DictReader(file)
        for linha in leitor:
            imovel.objects.create(
                num_contrib = linha['NUMERO DO CONTRIBUINTE'],
                nome_logradoro_imovel = linha['NOME DE LOGRADOURO DO IMOVEL'],
                num_imovel = linha['NUMERO DO IMOVEL'],
                complemento_imovel = linha['COMPLEMENTO DO IMOVEL'],
                bairro_imovel = linha['BAIRRO DO IMOVEL'],
                cep_imovel = linha['CEP DO IMOVEL'],
                area_tereno = linha['AREA DO TERRENO'],
                metro_quad_terreno = linha['VALOR DO M2 DO TERRENO']
            )


# if __name__ == "__main__":
    # csv_caminho = "../base_csv/imoveis_sp.csv"
    # importar_imoveis(csv_caminho)