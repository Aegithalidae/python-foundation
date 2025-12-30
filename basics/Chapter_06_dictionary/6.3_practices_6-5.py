river_crossing = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    'mississippi': 'usa',
    'danube': 'germany',
}

for river, country in river_crossing.items():
    print(f"The {river.title()} runs through {country.title()}.")
    print(f"{river.title()}")
    print(f"{country.title()}\n")