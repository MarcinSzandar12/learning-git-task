import logging

action = input("Podaj działanie, posługując się odpowiednią liczbą: 1 - Dodawanie, 2 - Odejmowanie, 3 - Mnożenie, 4 - Dzielenie: ")
first_number = int(input("Podaj pierwszą liczbę: "))
second_number = int(input("Podaj drugą liczbę: "))

logging.getLogger().setLevel(logging.INFO)

if action == "1":
    logging.info(f"Dodaję {first_number} i {second_number}")
    rezults = first_number + second_number
elif action == "2":
    logging.info(f"Odejmuję {first_number} i {second_number}")
    rezults = first_number - second_number
elif action == "3":
    logging.info(f"Mnożę {first_number} i {second_number}")
    rezults = first_number * second_number
elif action == "4":
    logging.info(f"Dzielę {first_number} i {second_number}")
    rezults = first_number / second_number
    
print(rezults)
