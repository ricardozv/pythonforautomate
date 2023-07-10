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

# Fornecedores
fornecedores = ["INAGRO"]

# Códigos das secretarias
codigos_secretarias = ["190201", "610101", "120101", "140101", "130101", "630101", "560101"]

# Obtendo os contratos para cada mês e secretaria
contratos_fornecedores = []

for fornecedor in fornecedores:
    for codigo_secretaria in codigos_secretarias:
        for mes in range(1, 13):
            # URL da API para o mês e secretaria específicos
            api_url = f"{base_url}?ano=2023&mes={mes}&codigo_ug={codigo_secretaria}"

            # Obtendo os dados da API para o mês e secretaria específicos
            dados = obter_dados_da_api(api_url)

            if dados is not None:
                # Filtrar os contratos do fornecedor específico
                contratos_mes_secretaria = [contrato for contrato in dados if contrato["credor_nome"].strip() == fornecedor]
                contratos_fornecedores.extend(contratos_mes_secretaria)

# Salvar os dados filtrados em um arquivo JSON
nome_arquivo = "contratos.json"
salvar_dados_em_json(contratos_fornecedores, nome_arquivo)
print("Contratos dos fornecedores", fornecedores, "salvos em", nome_arquivo)
