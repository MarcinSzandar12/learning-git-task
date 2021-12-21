print("Lista zakupów")

shopping_list = {"piekarnia":["chleb", "bułki", "pączek"], "warzywniak":["marchew", "seler", "rukola"]}

for x, y in shopping_list.items():
    print("Idę do", x.capitalize(),"kupuję tu następujące rzeczy:", [v.capitalize() for v in y])

print("W sumie kupuję", len(shopping_list["piekarnia"]) + len(shopping_list["warzywniak"]), "produktów.")

print("Pozdrawiam Pana Pawła Dudzińskiego, najlepszego Mentora!")