# projeto: nc_bankly_api_id_one

## escopo e briefing

 - consumir a api ID One do serviço Bankly
 - utilizar mocks de "copia de identificação"(ex: rg, cnh, etc) com foto e "foto de selfie"
 - utilizar as imagens do mock para conseguir gerar um registro na api o mais rápido possivel
 
## ferramental, linguagem, frameworks e apetrechos

 - linguagem: python
 - libs: requests, json
 - ~~teste de endpoint: Postman ou Insomnia~~
 
## pré requisitos:
 - criar alguns mocks com os dados para simulação:
   - cpf válido (use um gerador online)
   - rg com foto
   - cnh com foto
   - foto de selfie com algulos/posição/expressão facial/cabelo/barba/etc diferentes dos documentos
 - para teste um teste rápido, basta uns 3 ou 4 no máximo 
 
 
 - utilizar a API Facematch do https://developers.unico.io/docs/ para comparar a selfie com o doc
 
 
 - credenciais de acesso:
   - salve os dados/senhas/arquivos com a exata nomeclaruta e dentro dos diretorios abaixo. CUIDADO: os nomes são case-sentive
	 - PASSPHRASE -> .secret/Credentials/.PASSPHRASE
	 - certificate PEM -> .secret/Credentials/certificate.pem
	 - private PEM ->  .secret/Credentials/private.pem
 - ATENÇÃO: por segurança do projeto, os arquivos do diretório ".secret/Credentials/*" estão listados no .gitignore do REPO.


## Mão na massa

### ~~Testando~~
 - ~~para fazer um teste direto, utilizado o Insomnia para testar as rotas com um valor fixo~~
 
### executando o python


 
