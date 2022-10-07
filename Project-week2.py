import csv

with open("owid-covid-data.csv", "r") as csv_file:
    data = csv.reader(csv_file, delimiter=",")
    data_spain = []
    data_argentina = []
    data_europe = []
    data_north_america = []
    for x in data:
        if "Spain" in x:
            data_spain.append(x)
#            print(data_spain)
        elif "Argentina" in x:
            data_argentina.append(x)
#            print(data_argentina)
        elif "Europe" in x:
            data_europe.append(x)
 #           print(data_europe)
        elif "North America" in x:
            data_north_america.append(x)
 #           print(data_north_america)

#print(data_spain[ :2])

data_spain_dictionary = { data_spain: }
data_argentina_dictionary = { data_argentina: }
data_europe_dictionary = { data_europe: }
data_north_america_dictionary = { data_north_america: }