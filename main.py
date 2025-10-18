import random
import time
MAX_LEN = 4

def delka(user_number:str):
    '''
    Funkce kontroluje délku uživatelem zadané sekvence
    '''
    if len(user_number) != MAX_LEN:
        return False
    return True

def jsou_cislice(user_number:str):
    '''
    Funkce kontroluje zda zadané znaky jsou číslice
    '''
    for char in user_number:
        if not char.isdigit():
            return False
        return True

def not_zero (user_number:str):
    '''
    Funkce kontorluje, že první znak není nula
    '''
    if user_number[0] == "0":
        return False
    return True

def not_same(user_number:str):
    '''
    Funkce opakuje opakování stejných číslic
    '''
    us_num_lst = list(user_number)
    for i in us_num_lst:
        if us_num_lst.count(i) != 1:
            return False
    return True

def hodnoceni_bulls(user_number:str, ran_number:str):
    '''
    Funkce určuje počet bulls
    '''
    bulls = 0
    for i in range(len(user_number)):
        if user_number[i] == ran_number[i]:
           bulls += 1
    return bulls

def hodnoceni_cows(user_number:str, ran_number:str):
    '''
    Funkce urřuje počet cows
    '''
    cows = 0
    for i in range(len(user_number)):
        if (user_number[i] in ran_number
            and user_number[i] != ran_number[i]):
            cows += 1
    return cows

def bulls_prn(bulls:int):
    '''
    Funkce pro zápis bulls
    '''
    if bulls == 1:
        blp = "bull"
    else: blp = "bulls"
    return blp

def cows_prn(cows:int):
    '''
    Funkce pro zápis cows
    '''
    if cows == 1:
        clp = "cow"
    else: clp = "cows"
    return clp

def scrt_number():
    '''
    Funkce generuje náhodné číslo bez opakovaných číslic
    '''
    while True:
        ran_num = random.sample(range(0, 9), 4)
        if ran_num[0] != 0:
            break
    ran_number = "".join(map(str, ran_num))
    return ran_number

def hodnoceni_bulls_cows(user_number: str, ran_number:str):
     '''
     Funkce určuje počet buls a cows s výpisem
     '''
     print(f">>>> {user_number}")
     bulls = hodnoceni_bulls(user_number, ran_number)
     cows = hodnoceni_cows(user_number, ran_number)
     if bulls != MAX_LEN and cows !=0:
         return print(f"{bulls}{bulls_prn(bulls)}, {cows}{cows_prn(cows)}")
     else: return False
     
def game_routine(ran_number:str):
    '''
    Funkce pro průběh jednotlivé hry
    '''
    cntr = 0
    print("Hi there!")
    print("-" * 48)
    print(f"I've generated a random {MAX_LEN} digit number for you.")
    print("Let's play a bull and cows game.")
    print("-" * 48)
    start_time = time.time()
    while True:
        user_number = input("Enter a number: ")
        print(user_number)
        cntr += 1
        if (delka(user_number) == True and jsou_cislice(user_number) == True
            and not_zero(user_number) == True and not_same(user_number) == True):
            hodnoceni_bulls_cows(user_number, ran_number)
            if hodnoceni_bulls(user_number, ran_number) == MAX_LEN:
                print(f"Correct, you've guessed the right number in {cntr} guesses!")
                print("-" * 48)
                print("That's amazing!")
                stop_time = time.time()
                duration = stop_time - start_time
                return (cntr, duration)
            elif user_number == "quit":
                return "quit"
        else: print("Zadal jsi nesprávné číslo, opakuj zadání!")

cntr_lst = []
duration_lst = []
cntr_games = 0
while True:
    ran_number = scrt_number()
    #print(ran_number)
    cntr_games += 1
    cntr_save, duration_save = game_routine(ran_number)
    if cntr_save == "quit":
        break
    else:
        cntr_lst.append(cntr_save)
        duration_lst.append(round(duration_save, 2))
    play_again = input("Do you want to play again? Y/N: ")
    if play_again == "Y" or play_again == "y":
        continue
    else: break
print("Game over!")
print (f"You played {cntr_games} with {cntr_lst} tries and durations {duration_lst}")