for number in range(0,101):
    if number%3 == 0 and number%5 == 0:
        print("Dedezinha Querida")
    elif number%3 == 0:
        print("Dedezinha")
    elif number%5 == 0:
        print("Querida")
    else:
        print(f"{number}")