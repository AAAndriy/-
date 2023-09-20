class Address:
    def __init__(self, index, country, city, street, house, apartment):
        self._index = index
        self._country = country
        self._city = city
        self._street = street
        self._house = house
        self._apartment = apartment

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, value):
        self._house = value

    @property
    def apartment(self):
        return self._apartment

    @apartment.setter
    def apartment(self, value):
        self._apartment = value

# Створюємо екземпляр класу Address і заповнюємо його поля
address = Address(index="12345", country="Україна", city="Київ", street="Вулиця Київська", house="12А", apartment="34")

# Виводимо на екран значення полів адреси
print("Індекс:", address.index)
print("Країна:", address.country)
print("Місто:", address.city)
print("Вулиця:", address.street)
print("Будинок:", address.house)
print("Квартира:", address.apartment)
