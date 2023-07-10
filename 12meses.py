import requests
import json
from datetime import date, timedelta

def obter_dados_da_api(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao fazer a requisição. Código de status:", response.status_code)
        return None

def salvar_dados_em_json(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo)

# URL base da API
base_url = "https://transparencia.ma.gov.br/api/consulta-despesas"

# Códigos das secretarias
codigos_secretarias = ["190201", "610101", "120101", "140101", "130101","610202" ,"630101","610201","560101", "120207", "540101", "110125"]

# Obtendo os contratos para os últimos 12 meses de cada secretaria
contratos_secretarias = []

for codigo_secretaria in codigos_secretarias:
    for i in range(12):
        # Obtendo o mês e ano atual e calculando o mês anterior
        data_atual = date.today()
        mes_ano = (data_atual - timedelta(days=i*30)).strftime("%Y-%m")

        # URL da API para o mês e secretaria específicos
        api_url = f"{base_url}?ano={mes_ano[:4]}&mes={mes_ano[5:7]}&codigo_ug={codigo_secretaria}"

        # Obtendo os dados da API para o mês e secretaria específicos
        dados = obter_dados_da_api(api_url)

        if dados is not None:
            contratos_secretarias.extend(dados)

# Salvar os dados obtidos em um arquivo JSON
nome_arquivo = "contratos.json"
salvar_dados_em_json(contratos_secretarias, nome_arquivo)
print("Contratos de todas as secretarias salvos em", nome_arquivo)
