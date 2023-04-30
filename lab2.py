import json as jreader

def ReadJsonFile():
    data = []
    with open (r'C:\Users\Saul\Downloads\input_challenge_lab_2.jsonl') as JsonFile:
        for line in jsonFile:
            data.append(json.loads(line))
    return data

#Leemos la informacion y aplicamos el filtro por cada espacio
data = jreader.ReadJsonFile()
for i in range(len(data)):
    pp.filterMatchPlaces(data[i]['input1'],data[i]['input2'])
