from faker import Faker
import random
import json

fake = Faker()
dlist = []
for i in range(100):
    dictionary ={
        "Gender": random.choice(['Male','Female']),
        "HeightCm": (random.randint(110,170)),
        "WeightKg": (random.randint(25,100))
        }
    dlist.append(dictionary)

with open("data.json", "w") as outfile:
    json.dump(dlist, outfile)