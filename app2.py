# -*- coding: utf-8 -*-
# coding: utf-8

import requests
import json
import os
import base64

def ler_primeira_linha(file):
    caminho_file = os.path.abspath(file)
    f = open(caminho_file, encoding='utf-8', errors='replace')
    lines = f.readlines()
    f.close()
    return lines[0].strip('\n')

#####################################################
#           parametros de login
# ref: https://docs.bankly.com.br/reference/token-de-acesso

url_create_token = "https://login.sandbox.bankly.com.br/connect/token"

client_id = ler_primeira_linha('.secret/Credentials/.CLIENT_ID')
client_secret = ler_primeira_linha('.secret/Credentials/.CLIENT_SECRET')
passphrase = ler_primeira_linha('.secret/Credentials/.PASSPHRASE')
company_key = ler_primeira_linha('.secret/Credentials/.COMPANY_KEY')


payload_token = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    # "scope": "certificate.create",
    "scope": ' certificate.create',
    # "scope": "kyc.document.deepface.write"
}
headers_token = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded"
}

response_create = requests.post(url_create_token, data=payload_token, headers=headers_token)
certificate_create_response = response_create.text
print(f'\n\ncertificate_create_response = {certificate_create_response}')

token = response_create.json()['access_token']
print(f'\n\n\ntoken=\n{token}\n\n\n')




#certificado
# https://docs.bankly.com.br/reference/download-certificado

url_certificado = f"https://api.sandbox.bankly.com.br/partners/{company_key}/certificates"

payload_certificado = {
    "passphrase": passphrase,
    "ttlInDays": 20
}
headers_certificado = {
    "accept": "application/json",
    "api-version": "1.0",
    "authorization": token,
    "content-type": "application/json"
}

response_certificado = requests.post(url_certificado, json=payload_certificado, headers=headers_certificado)

response_certificado_txt = response_certificado.text

print(f'\n++++++++++++++++++++++\nresponse_certificado_txt = {response_certificado_txt}\n\n++++++++++++++++++++++\n')



#
# payload_token2 = {
#     "grant_type": "client_credentials",
#     "client_id": client_id,
#     "client_secret": client_secret,
#     # "scope": "certificate.create",
#     "scope": "kyc.document.deepface.write"
# }
#
# response_create2 = requests.post(url_create_token, data=payload_token2, headers=headers_token)
# certificate_create_response2 = response_create2.text
# print(f'certificate_create_response2 = {certificate_create_response2}')
#


#
#####################################################




#####################################################
#

# header

# curl --request POST \
#       --url "https://login.sandbox.bankly.com.br/connect/token" \
#       --header "Accept: application/json" \
#       --header "Content-Type: application/x-www-form-urlencoded"  \
#       --data "grant_type=client_credentials
#               &client_id={{yourClientId}}
#               &client_secret={{yourClientSecret}}
#               &scope={{yourScope}}"

#####################################################
#           parametros de envio ID ONE
# ref: https://docs.bankly.com.br/reference/id-one-envio-documentos
#ref certo: https://docs.bankly.com.br/docs/envio-documentos-analise-id-one

cpf = '05852252905'

url_id_one = f'https://api-mtls.sandbox.bankly.com.br/document-analysis/{cpf}/deepface'

caminho_documento = os.path.abspath('mock/cnh_teste_enio.jpeg')
print(f'caminho_documento={caminho_documento}')

document_data = {
    # "documentType": "SELFIE",
    "documentType": "CNH",
    "documentSide": "FRONT",
    "image": caminho_documento,
    # 'image': '@"/var/robo/PROJETOS_ROBOS/enio.farias/nc_bankly_api_id_one/mock/cnh_teste_enio.jpeg"',
    # "provider": "UNICO_CHECK",
    "provider": "BANKLY"
}

headers = {
    "api-version": "1",
    "x-correlation-id": "GUID",
    "Authorization": token
}

response = requests.post(url_id_one, headers=headers, json=document_data)

text_response = response.text

# print(f'\ntext_response: {text_response}\n')

if response.status_code == 200:
    print("Documento enviado com sucesso!")
else:
    print(f"\n------------------\nErro ao enviar o documento: \n{response.content}\n------------------\n")