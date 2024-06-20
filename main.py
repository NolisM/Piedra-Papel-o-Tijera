import random

option= ('piedra', 'papel', 'tijera')
computer_wins = 0
user_wins = 0
round = 1
while True:
    
    print('*' * 10)
    print('round',round)
    print('*' * 10)
    
    print('-' * 10)
    print('puntaje del computer => ', computer_wins)
    print('puntaje del usuario => ', user_wins)
    print('-' * 10)
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()
    round += 1
    computer_option = random.choice(option)
    if user_option == computer_option:
        print('Empate')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('computer gano')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option== 'piedra':
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computer gano')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computer gano')
            computer_wins += 1
    else:
        print('No es una opcion valida')
        continue
    
    if ( computer_wins == 2):
        print('el ganador es el computador')
        break
    if ( user_wins == 2):
        print('el ganador es el usuario')
        break