import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

rounds = 1

while True:

    print('*' * 10)
    print('ROUND',rounds)
    print('*' * 10)

    print('computer points:',computer_wins)
    print('user points:',user_wins)


    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    rounds += 1 

    if not user_option in options:
        print('Esa opcion no es valida')
        #continue

    computer_option = random.choice(options)

    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gana!')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('computer gana!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gana!')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computer gana!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gana!')
            user_wins += 1
        else:
            print('piedra gana a tijera')    
            print('computer gana')
            computer_wins += 1

    if computer_wins == 2:
        print('computer gana la partida!')
        break

    if user_wins == 2:
        print('user gana la partida!')
        break

    #rounds += 1        
            