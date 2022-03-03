import os

import pandas as pd
from termcolor import colored

file_name = "formatted.csv"
df = pd.read_csv(file_name)  # create dataframe from csv

try:
    output = pd.read_csv("locations.csv")
except:
    output = pd.DataFrame(columns=["location", "route"])

start = int(input("Start with index number: "))  # for starting in the middle of the dataframe
for index, row in df.iterrows():
    entry = {}
    if index >= start:
        print("###################")
        print("Ort: " + row["Ort"])
        print("Standort des Lagers: " + row["Standort des Lagers"])
        print("###################")
        while True:
            try:
                location = input("Enter location name: ")
                entry["location"] = location
                break
            except ValueError:
                print("Enter a valid string.")
        print("###################")
        print("Verlauf/Orte: " + row["Verlauf/Orte"])
        print("###################")
        print(colored("Enter 'n' to finish route", "red"))
        route = []
        while True:
            try:
                route_stop = input("Enter route stop: ")
                if route_stop == "n":
                    os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal after finishing entry
                    break
                else:
                    route.append(route_stop)
            except ValueError:
                print("Enter a valid string.")
        entry["route"] = route
        output = output.append(entry, ignore_index=True)
        output.to_csv("locations.csv", index=False)
    else:
        continue
