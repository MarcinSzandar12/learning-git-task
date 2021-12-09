print("Lista zakupów")

shopping_list = {"piekarnia":["chleb", "bułki", "pączek"], "warzywniak":["marchew", "seler", "rukola"]}

#shopping_list = [product.capitalize() for product in shopping_list.values()]

for x, y in shopping_list.items():
    print("Idę do", x.capitalize(),"kupuję tu następujące rzeczy:", y)

print("W sumie kupuję", len(shopping_list["piekarnia"]) + len(shopping_list["warzywniak"]), "produktów.")

print("Aktualizacja repozytorium lokalnego.")
