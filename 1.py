import json
countries_capitals = {}
def add_data(country, capital):
    countries_capitals[country] = capital
def delete_data(country):
    if country in countries_capitals:
        del countries_capitals[country]
    else:
        print("Страна не найдена в словаре.")
def search_data(country):
    if country in countries_capitals:
        return countries_capitals[country]
    else:
        return "Страна не найдена в словаре."
def edit_data(country, new_capital):
    if country in countries_capitals:
        countries_capitals[country] = new_capital
    else:
        print("Страна не найдена в словаре.")
def save_data(file_name):
    with open(file_name, 'w') as file:
        json.dump(countries_capitals, file)
def load_data(file_name):
    global countries_capitals
    with open(file_name, 'r') as file:
        countries_capitals = json.load(file)

add_data('Россия', 'Москва')
add_data('США', 'Вашингтон')

print(search_data('Россия'))
edit_data('Россия', 'Санкт-Петербург')
print(search_data('США'))

delete_data('США')

print(search_data('США'))

save_data('countries.json')

countries_capitals = {}
load_data('countries.json')

print(search_data('Россия'))