import requests
import json

''' Feito por Kripto-Sec 
    Use apenas pra fins educacionais
    conhecimento não é crime
'''

torport = 9050
proxies = {
    'http': "socks5h://localhost:{}".format(torport),
    'https': "socks5h://localhost:{}".format(torport)
}


banner = '''
         ___  ____ ____ ____    _  _ _  _ _  _ ___ ____ ____ 
         |__] |__| [__  [__  __ |__| |  | |\ |  |  |___ |__/ 
         |    |  | ___] ___]    |  | |__| | \|  |  |___ |  \ 
                                                             
 '''

print(banner)


print("Exemplo de uso email: teste@gmail.com")
print("User: teste")
print("Dominio: gmail.com")

print("\n")
username = input("Digite o user: ")
domain = input("Digite o dominio: ")
print("Procurando...")



request_data = {'luser': username, 'domain': domain, 'luseropr': 1, 'domainopr': 1, 'submitform': 'em'.format(username, domain)}
url = "http://pwndb2am4tzkvold.onion"
r = requests.post(url, proxies=proxies, data=request_data)
string = r.text

start = string.find('<pre>')
finish = string.find('</pre>')
cos = string[start:finish]

print(cos)
        
# O output n ta arrumado meu pc desligou e eu perdi tudo 
# N to afim de arrumar isso agora :)
