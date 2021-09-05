element = ["Metal ", "Metal ", "Water ", "Water ", "Wood ", "Wood ", "Fire ", "Fire ", "Earth ", "Earth "]
zodiac = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"]

def zodiac_element(year):
    return element[year%10] + zodiac[year%12]

