class Card:
    def __init__(self, first_name, last_name, company_name, job_position, email):
       self.first_name = first_name
       self.last_name = last_name
       self.company_name = company_name
       self.job_position = job_position
       self.email = email

       self._first_name_lengh = len(first_name)
       self._last_name_lengh = len(last_name)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    def contact(self):
        return f'Kontaktuję się z {self.first_name} {self.last_name} {self.job_position} {self.email}'

    @property
    def name_lengh(self):
        return f'{self._first_name_lengh} {self._last_name_lengh}'

class BaseContact(Card):
   def __init__(self, phone_number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.phone_number = phone_number

    def contact(self):
        return f'Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}'

    @property
    def name_lengh(self):
        return f'{self._first_name_lengh} {self._last_name_lengh}'

class BaseContact(Card):
   def __init__(self, business_phone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.business_phone = business_phone

    def contact(self):
        return f'Wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name}'

    @property
    def name_lengh(self):
        return f'{self._first_name_lengh} {self._last_name_lengh}'

card_1 = Card(first_name = "Karol", last_name = "Nowak", phone_number = "+48 409 054 993", business_phone = "+48 384 092 012", company_name = "Parklane Hosiery", job_position = "Ticket taker", email = "KarolNowak@rhyta.com")
card_2 = Card(first_name = "Sławomira", last_name = "Zając", phone_number = "+48 395 237 012", business_phone = "+48 976 391 104", company_name = "Gold Touch", job_position = "Financial aid director", email = "SlawomiraZajac@dayrep.com")
card_3 = Card(first_name = "Bartosz", last_name = "Rutkowski", phone_number = "+48 192 374 019", business_phone = "+48 377 919 555", company_name = "Service Merchandise", job_position = "Land surveyor", email = "BartoszRutkowski@dayrep.com")
card_4 = Card(first_name = "Oliwia", last_name = "Czarnecka", phone_number = "+48 142 576 978", business_phone = "+48 519 945 920", company_name = "Greenwich IGA", job_position = "Pipelayer", email = "OliwiaCzarnecka@armyspy.com")
card_5 = Card(first_name = "Kunegunda", last_name = "Kwiatkowska", phone_number = "+48 135 246 357", business_phone = "+48 111 232 909", company_name = "Weingarten's", job_position = "Power transformer repairer", email = "KunegundaKwiatkowska@rhyta.com")

cards = [card_1, card_2, card_3, card_4, card_5]

by_first_name = sorted(cards, key=lambda card: card.first_name)
by_last_name = sorted(cards, key=lambda card: card.last_name)
by_email = sorted(cards, key=lambda card: card.email)

