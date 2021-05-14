import os

num = int(input("Numero de telefono: "))

#Comentar este comando en caso de tener instalado curl
#os.system('apt-get install curl')

os.system('clear')

os.system(f'curl "http://apilayer.net/api/validate?access_key=9bbe084951ab3183978a8ade88f90532&number={num}&country_code=&format=1" | sed -e "s/^.//" -e "s/.$//" > {num}.txt')
os.system(f'chmod 777 {num}.txt')
os.system('clear')
os.system(f'cat -T {num}.txt')


print('\n\n')
input('Preisona una tecla para continuar...')

os.system('clear')


