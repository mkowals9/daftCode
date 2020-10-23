import csv
import pandas as pd
import re
from collections import defaultdict

class ContainerShip:
    originCountry = '0'
    destinationCountry = '0'
    containerNumber = '0'
    containerWeight = '0'
    loadType = '0'
    companyName = '0'
    companyCountry = '0'
    def __rep__(self):
        return "Hello"

    def getting_info (self,text) :
        info_list = []
        info_list = re.split("-|/|@|\.", text)
        self.originCountry = info_list[0]
        self.destinationCountry = info_list[1]
        self.containerNumber = info_list[2]
        self.containerWeight = info_list[3]
        self.loadType = info_list[4]
        self.companyName = info_list[5]
        self.companyCountry = info_list[6]




def load_data() :
    test = pd.read_csv("dane.csv", delimiter=';', header=None)
    all_containers = []
    for col in test.columns:
        all_containers.extend([cell for cell in test.get(col) if pd.notna(cell)])
    print(test.head(5))
    new_header = test.iloc[0]
    test = test[1:]
    test.columns = new_header
    ships_and_containers = {}
    for col in test.columns:
        containers = []
        containers.extend([cell for cell in test.get(col) if pd.notna(cell)])
        ships_and_containers[col] = containers
    print(f"read {len(all_containers)} containers")
    jap_containers = [con for con in all_containers if con.split('-')[1] == 'JP']
    print(f"{len(jap_containers)} containers will end up in japan")
    return ships_and_containers
    # import ipdb; ipdb.set_trace()
    # names = [con.split('/')[0].split('-')[2] for con in all_containers]


dataContainers = load_data()
#print(dataContainers)
ship_name_to_container_list = defaultdict(list)
for ship, containers_str in dataContainers.items():
    for container_str in containers_str:
        container = ContainerShip()
        container.getting_info(container_str)
        ship_name_to_container_list[ship].append(container)

print(dict(ship_name_to_container_list))








