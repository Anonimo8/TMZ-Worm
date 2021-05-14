import os

num = int(input("Numero de telefono: "))

#os.system('apt-get install curl')

os.system('clear')

os.system(f'curl "http://apilayer.net/api/validate?access_key=9bbe084951ab3183978a8ade88f90532&number={num}&country_code=&format=1" ')

print('\n\n')
input('Preisona una tecla para continuar...')
os.system('clear')

#curl -H "" | json_ppasd
