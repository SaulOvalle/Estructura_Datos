import json 

def ReadJsonFile():
    data = []
    with open (r'C:\Users\Saul\Downloads\input_challenge_lab_2.jsonl') as JsonFile:
        for line in JsonFile:
            data.append(json.loads(line))
    return data

def construccion (input1, typeBuilder):
    
    construc = []
    Fconstruc = []
    for i in range(len(input1)):
        for j in input1[i]['builds'].keys():
            if(j == typeBuilder):
                construc.append(input1[i]['builds'][j])

    for i in construc:
        for j in i:
            Fconstruc.append(j)
    return Fconstruc

def PeligroCliente(peligro):
   
    outputList = []
    match peligro:
        case "Red":
            outputList = ["Red"]
        case "Orange":
            outputList = ["Red","Orange"]
        case "Yellow":
            outputList = ["Red","Orange","Yellow"]
        case "Green":
            outputList = ["Red","Orange","Yellow","Green"]
    return outputList

def FDaño(CurrentList,danger):
    #Se devuelven los lugares cuyo nivel de peligro 
    #admitido se encuentra en la lista de dangerList
    matching = []
    LDaño = []
    LDaño = FDaño(danger)
    for i in range(len(CurrentList)):
        if any(elem in CurrentList[i]['zoneDangerous'] for elem in LDaño):
            matching.append(CurrentList[i])
    return matching