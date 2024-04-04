# -*- coding: utf-8 -*-
# coding: utf-8

import requests
import json
import os
import base64

# URL da API
# url = "https://api-mtls.sandbox.bankly.com.br/document-analysis/{documentNumber}/deepface"
url = "https://api-mtls.sandbox.bankly.com.br/document-analysis/05852252905/deepface"

# Seu token de acesso
# ler o arquivo .secret/Credentials/.PASSPHRASE

caminho_passphrase_token = os.path.abspath('.secret/Credentials/.PASSPHRASE')
f = open(caminho_passphrase_token, encoding='utf-8', errors='replace')
lines = f.readlines()
f.close()

# "seu_token_de_acesso"#
access_token = lines[0].strip('\n')

# print(f'access_token: {access_token}')

# converter imagem da foto de selfie para base64
# caminho_selfie = os.path.abspath('mock/selfie_teste_enio.jpeg')
# caminho_documento = os.path.abspath('mock/selfie_teste_enio.jpeg')
caminho_documento = os.path.abspath('mock/cnh_teste_enio.jpeg')
# caminho_documento = os.path.abspath('mock/documento_teste_enio.jpeg')

with open(caminho_documento, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()
base64_da_imagem_do_documento = str(encoded_string)

# print(f'base64_da_imagem_do_documento = \n\n\n{base64_da_imagem_do_documento}\n\n\n')

# Dados do documento
document_data = {
    # "documentType": "SELFIE",
    "documentType": "CNH",
    "documentSide": "FRONT",
    "image": "@" + caminho_documento,
    # "provider": "UNICO_CHECK",
    "provider": "BANKLY"
    # "providerMetadata": {
    #     "isLastDocument": True,
    #     "encrypted": base64_da_imagem_do_documento,
    # "providerMetadata": "{\"isLastDocument\": true,\"encrypted\": \"/9j/4AAQSkZJRgABAQAAAQABAAD/2wCE****************G2JPEDKdi3kUzIZCr5mnGAdT//2Q==\"}"

    # }
}

# Headers da requisição
headers = {
    "api-version": "1",
    "x-correlation-id": "GUID",
    "Authorization": "Bearer " + access_token
}

# print(f'headers: {headers}')

# Fazendo a requisição POST
response = requests.post(url, headers=headers, json=document_data)

# Verificando a resposta
if response.status_code == 200:
    print("Documento enviado com sucesso!")
else:
    print(f"Erro ao enviar o documento: \n{response.content}\n")