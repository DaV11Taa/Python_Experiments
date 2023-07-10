class Animal:
    def __init__(self, name, foodCosts):
        self.name = name
        self.foodCosts = foodCosts

    def getName(self):
        return self.name

    def getFoodCosts(self):
        return self.foodCosts

    def toString(self):
        return f"(name: {self.name}, foodCosts: {self.foodCosts})"


class Vivarium:
    def __init__(self, inhabitants, area, constructionYear):
        self.inhabitants = inhabitants
        self.area = area
        self.constructionYear = constructionYear

    def getCost(self):
        return 900 + self.area ** 2 * 100 + self.area ** 2 * (2021 - self.constructionYear) * 5

    def toSting(self):
        # "[area: 34, constructionYear: 1965, animals: (name: Pingu, foodCosts: 231), (name: Pinguina, foodCosts: 270)]"
        result = "[area: " + str(self.area) + ", constructionYear: " + str(self.constructionYear) + ", animals: "
        for animal in self.inhabitants:
            if self.inhabitants[len(self.inhabitants) - 1] == animal:
                result = result + animal.toString() + "]"
            else:
                result = result + animal.toString() + ", "
        return result


class Zoo:
    def __init__(self, vivaria):
        self.vivaria = vivaria

    def getCost(self):
        result = 0
        for vivarium in self.vivaria:
            result = result + vivarium.getCost()
        return result

    def toString(self):
        result = "{"
        for vivarium in self.vivaria:
            if self.vivaria[len(self.vivaria) - 1] == vivarium:
                result = result + vivarium.toSting() + "}"
            else:
                result = result + vivarium.toSting() + ", "
        return result


vivarias = []
AnimalList = []
first = Animal("Lion", 235)
second = Animal("Wolf", 500)
third = Animal("Pingu", 450)
AnimalList.append(first)
AnimalList.append(second)
AnimalList.append(third)
AnimalList2 = []
First = Animal("giorgi", 900)
Second = Animal("deme", 800)
Third = Animal("shalva", 100)
AnimalList2.append(First)
AnimalList2.append(Second)
AnimalList2.append(Third)
vivaria = Vivarium(AnimalList, 9, 1998)
vivaria2 = Vivarium(AnimalList2, 12, 2000)
vivarias.append(vivaria)
vivarias.append(vivaria2)
zoo = Zoo(vivarias)
print(zoo.toString())
print(zoo.getCost())
