import requests
import json

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

# Fornecedor
fornecedor = "GILSON CLAUDIO DOS SANTOS TEIXEIRA"

# Obtendo os contratos para cada mês
contratos_fornecedor = []

for mes in range(1, 13):
    # URL da API para o mês específico
    api_url = f"{base_url}?ano=2023&mes={mes}&codigo_ug=110121"

    # Obtendo os dados da API para o mês específico
    dados = obter_dados_da_api(api_url)

    if dados is not None:
        # Filtrar os contratos do fornecedor específico
        contratos_mes = [contrato for contrato in dados if contrato["credor_nome"].strip() == fornecedor]
        contratos_fornecedor.extend(contratos_mes)

# Salvar os dados filtrados em um arquivo JSON
nome_arquivo = "contratos.json"
salvar_dados_em_json(contratos_fornecedor, nome_arquivo)
print("Contratos do fornecedor", fornecedor, "salvos em", nome_arquivo)
