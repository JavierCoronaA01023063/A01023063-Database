import csv

population_2010 = [ ]
population_co2 = [ ]
value_errors = ["--", "NA"]
country_exceptions = ["World", "Country", "Asia & Oceania", "Africa", "Europe", "Central & South America", "North America", "Eurasia", "Middle East" ]

with open("populationbycountry19802010millions.csv") as csvFile:
    reader = csv.reader(csvFile)

    for row in reader:
        if row[-1] not in value_errors and row[0] not in country_exceptions:
            population_2010.append([float(row[-1]), row[0]])

population_2010.sort(reverse=True)
print("Countries with highest population in 2010: ")
print(population_2010[:5])


population_co2 = [ ]
country_exceptions2 = ["World", "Country", "Asia & Oceania", "Africa", "Europe", "Central & South America", "North America", "Eurasia", "Middle East", "European Union" ]
year = ["2010"]
data = ["greenhouse_gas_ghgs_emissions_including_indirect_co2_without_lulucf_in_kilotonne_co2_equivalent"]

with open("greenhouse_gas_inventory_data_data.csv") as csvFile:
    reader = csv.reader(csvFile)

    for column in reader:
        if column[0] not in country_exceptions2 and column[2] not in value_errors and column[1] in year and column[3] in data:
            population_co2.append([int(column[1]), float(column[2]), column[0]])

population_co2.sort(reverse=True)
print("And countries with highest Greenhouse in 2010: ")
print(population_co2[:5])

print("La relación es que Estado Unidos se encuentra en ambas listas por su gran población y sus emisiones de greenhouse")
print("Los otros paises no estan de gran población de la primera pregunta no salen como respuesta en la segunda porque no hay datos de estos paises en la base de datos.")
print("Es curioso que no se encuentren. Lo más probable es que hubieran salido nuevamente.")