# i. Using above create a dictionary of countries and its population
# ii. Write a program that asks user for three type of inputs,
#    a. print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
#    b. add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
#    c. remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
#    d. query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.


def printDict(population):
    for info in population:
        print(info,"==>",population[info])


def addDict(population):
    countryName=input("Add country name: ")
    for info in population:
        if countryName == info:
            print("Country already exists. TRY AGAIN")
            break
        else:
            populationNum=input("Add population of entered country: ")
            population[countryName]=populationNum
            for info in population:
                print(info,"==>",population[info])
            return population


def removeDict(population):
    item=input("Enter country you want to remove: ")
    population.pop(item)
    for info in population:
        print(info,"==>",population[info])

def printPopulation(population):
    item=input("Enter the country you want to see the population of : ")
    for info in population:
        if item == info:
            print(item,"==>",population[item])
            break
        else:
            print("COUNTRY DOES NOT EXIST")
            break
            
population={
    'China':143,
    'India':136,
    'USA':32,
    'Pakistan':21
}

printDict(population)
addDict(population)
removeDict(population)
printPopulation(population)
