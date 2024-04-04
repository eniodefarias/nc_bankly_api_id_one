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
	 - CLIENT_ID -> .secret/Credentials/.CLIENT_ID
	 - CLIENT_SECRET -> .secret/Credentials/.CLIENT_SECRET
	 - COMPANY_KEY -> .secret/Credentials/.COMPANY_KEY
	 - certificate PEM -> .secret/Credentials/certificate.pem
	 - private PEM ->  .secret/Credentials/private.pem

	 
 - ATENÇÃO: por segurança do projeto, os arquivos do diretório ".secret/Credentials/*" estão listados no .gitignore do REPO.


## Mão na massa

### ~~Testando~~
 - ~~para fazer um teste direto, utilizado o Insomnia para testar as rotas com um valor fixo~~
 
### executando o python

python3 app.py
 
 
# Observações, desenvolvimento e notas:

consegui fazer:

(1)autenticação do scope certificate.create para pegar o token

---

estava tentando agora:

(2)utilizar o token anterior para pegar os certificates

mas esse não consegui, eu uso o token gerado, mas retorna dizendo que o token não permite autenticação

---


(3)montei o payload para tentar usar o ID One, mas como eu não não consegui as credenciais do (2) esse não foi pra frente

---


(4)tava também olhando como faria a integração com Unico e Facematch pra depois validar o documento do (3) com o selfie que tambem seria em (3)



## considerações finais:
provavelmente eu devo tá deixando passar algo na credencias(2) ou comi bola e faltou algo no token do (1)
o que eu faria agora seria começar a rever tudo de novo,
separar as requisições uma da outra
e recomeçar a testar um pouco mais devagar.

estou considerando que a documentação do bakly tá certa.
mas as vezes parece que ela se perde um pouquinho
