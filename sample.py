import csv
import pandas as pd
import re

class ContainerShip:
    originCountry='0'
    destinationCountry='0'
    containerNumber='0'
    containerWeight='0'
    loadType='0'
    companyName='0'
    companyCountry='0'
    def gettingInfo(self,text):
        #text.replace("/", "-")
        #print(text)
        #replace("@", "-").replace(".", "-")
        #infoList=text.split("-")
        import re
        infoList=re.split("-|/|@|\.", text)
        self.originCountry=infoList[0]



def load_data():
    test = pd.read_csv("dane.csv", delimiter=';', header=None)
    all_containers = []
    for col in test.columns:
        all_containers.extend([cell for cell in test.get(col) if pd.notna(cell)])
    print(test.head(5))
    new_header = test.iloc[0]
    test = test[1:]
    test.columns = new_header
    print(f"read {len(all_containers)} containers")
    jap_containers = [con for con in all_containers if con.split('-')[1] == 'JP']
    print(f"{len(jap_containers)} containers will end up in japan")
    return test
    # import ipdb; ipdb.set_trace()
    # names = [con.split('/')[0].split('-')[2] for con in all_containers]


dataContainers=load_data()
print(dataContainers.head(5))
for col in dataContainers.columns:
    for cell in dataContainers.get(col):
        info=cell
        #print(info)
        if info is not 'nan':
            cell=ContainerShip()
            cell.gettingInfo(info)



