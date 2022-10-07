import csv
import statistics
from typing import List, Any
spain_deaths = []   #totale morti in spagna per covid 19
argentina_deaths = [] #totali morti in argentina per covid 19
argentina_total_case = [] #totali casi positivi in argentina
spain_total_case = [] #totali casi positivi in spagna


data_europe_total_case = [] #totali casi in europa
data_north_america_total_case = [] #totali casi in Nord America
europe_tot_vacc = [] #numero di vaccinati totali in Europa
north_america_tot_vacc = [] #numero di vaccinati totali in Nord America


with open("owid-covid-data.csv", newline="") as csv_file:
    data = csv.reader(csv_file, delimiter=",")

    for row in data:
        if row[2] == "Spain" and row[8] != "":
            spain_deaths.append(float(row[8]))
        if row[2] == "Argentina" and row[8] != "":
            argentina_deaths.append(float(row[8]))
        if row[2] == "Spain" and row[4] != "":
            spain_total_case.append(float(row[4]))
        if row[2] == "Argentina" and row[4] != "":
            argentina_total_case.append(float(row[4]))
        if row[1] == "Europe" and row[34] != "":
            europe_tot_vacc.append(float(row[34]))
        if row[1] == "North America" and row[34] != "":
            north_america_tot_vacc.append((row[34]))
        if row[1] == "Europe" and row[4] != "":
            data_europe_total_case.append(float(row[4]))
        if row[1] == "North America" and row[4] != "":
            data_north_america_total_case.append(float(row[4]))


""" Confronto medie tra le morti e i casi totali registrati riferite ai paesi Spagna e Argentina nel periodo 2020 - 2022
Dai risultati si evince come in media i morti in spagna e argentina si discostino di 16 punti di media; mentre la media 
dei casi giornalieri in argentina è piu alta che in Spagna. """

print(statistics.mean(spain_deaths))
print(statistics.mean(argentina_deaths))
print(statistics.mean(argentina_total_case))
print(statistics.mean(spain_total_case))

""" Confronto medie tra i casi totali registrati in Europa e in Nord America nel periodo 2020 - 2022. 
Le medie sui casi totali giornalieri distribuiti sono più alti in Europa che in Nord America"""

print(statistics.mean(data_europe_total_case))
print(statistics.mean(data_north_america_total_case))


#Confronto mediana tra casi totali vaccinati in Europa e in Nord America nel periodo 2020 - 2022
north_america_tot_vacc.sort()
europe_tot_vacc.sort()

print(statistics.median(north_america_tot_vacc))
print(statistics.median(europe_tot_vacc))










