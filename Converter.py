class Converter:
    def __init__(self, usd, eur, pln):
        self.usd = usd
        self.eur = eur
        self.pln = pln

    def hryvnia_to_usd(self, amount):
        return amount / self.usd

    def hryvnia_to_eur(self, amount):
        return amount / self.eur

    def hryvnia_to_pln(self, amount):
        return amount / self.pln

    def usd_to_hryvnia(self, amount):
        return amount * self.usd

    def eur_to_hryvnia(self, amount):
        return amount * self.eur

    def pln_to_hryvnia(self, amount):
        return amount * self.pln

# Створюємо екземпляр класу Converter з курсами валют
converter = Converter(usd=28.5, eur=33.0, pln=7.5)

# Конвертація з гривні в інші валюти
amount_hryvnia = 1000
usd_amount = converter.hryvnia_to_usd(amount_hryvnia)
eur_amount = converter.hryvnia_to_eur(amount_hryvnia)
pln_amount = converter.hryvnia_to_pln(amount_hryvnia)

print(f"{amount_hryvnia} гривень = {usd_amount:.2f} USD")
print(f"{amount_hryvnia} гривень = {eur_amount:.2f} EUR")
print(f"{amount_hryvnia} гривень = {pln_amount:.2f} PLN")

# Конвертація з інших валют в гривню
usd_amount = 100
eur_amount = 50
pln_amount = 200

hryvnia_usd = converter.usd_to_hryvnia(usd_amount)
hryvnia_eur = converter.eur_to_hryvnia(eur_amount)
hryvnia_pln = converter.pln_to_hryvnia(pln_amount)

print(f"{usd_amount} USD = {hryvnia_usd:.2f} гривень")
print(f"{eur_amount} EUR = {hryvnia_eur:.2f} гривень")
print(f"{pln_amount} PLN = {hryvnia_pln:.2f} гривень")
