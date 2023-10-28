import requests
import json

ZZXD = str(input('''   ____   _____   ____  
  / ___| | ____| |  _ \ 
 | |     |  _|   | |_) |
 | |___  | |___  |  __/ 
  \____| |_____| |_|    
                        
OLA SEJA BEM VINDO A CONSULTA CEP
|----------------------------------------------|
|\033[2;49;91m[00]CLIQUE 00 SE DESEJA SAIR!                 |
|\033[2;49;36m[1]CLIQUE 1 PARA AVANÇAR!                     |
|----------------------------------------------|
ESCOLHA SUA OPÇÃO:'''))

if ZZXD == '00':
	print('\033[2;49;91mvoce saiu! :(')
	print('''DESENVOLVIDO POR:
[!]ZIIP
[!]INSTAGRAM: @ziip_019]
[!]GIT HUB: https://github.com/ziippk''')
	exit()
else:
	ziipXD = input('clique enter para avançar ->>')

cep = input('DIGITE O CEP PARA REALIZAR A CONSULTA:')

if len(cep) != 8:
	print('quantidade de digitos invalida!')
	print('digite o cep novamente e corretamente.')
	print('nao digite o cep com traços')
	exit()

requests = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep)).text

print(requests)

print('''DESENVOLVIDO POR:
[!]ZIIP
[!]INSTAGRAM: @ziip_019
[!]GIT HUB: https://github.com/ziippk''')
