import time
import json
import csv

column_names = ['Body Mass Index (kg/m2)','BMI Scale (kg/m2)','Health Risk']

def checkBmi():
    with open('bmidata.csv','w',newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(column_names)

        for i in data:
            bmi = i.get('WeightKg')/((i.get('HeightCm')**2)/10000)
            if (bmi < 18.4):
                bmiData = [f'{round(bmi,2)} kg/m2','18.4 and below', 'Malnutrition risk']
            elif(bmi > 18.5 and bmi < 24.9):
                # print(f'{round(bmi,2)} kg/m2, Low risk')
                bmiData = [f'{round(bmi,2)} kg/m2','18.5 - 24.9', 'Low risk']
            elif(bmi > 25 and bmi < 29.9):
                bmiData = [f'{round(bmi,2)} kg/m2','25-29.9','Enhanced risk']
            elif(bmi > 30 and bmi < 34.9):
                bmiData = [f'{round(bmi,2)} kg/m2','30-34.9','Medium risk']
            elif(bmi > 35 and bmi < 39.9):
                bmiData = [f'{round(bmi,2)} kg/m2','35-39.9','High risk']
            else:
                bmiData = [f'{round(bmi,2)} kg/m2','40 and above','Very High risk']
            csvwriter.writerow(bmiData)


with open('./data.json','r') as f:
    data = json.loads(f.read())
    f.close()


import timeit
print(f"Execution time is: {timeit.timeit(stmt = checkBmi, number = 1)}")