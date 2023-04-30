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

def FDaño(List,danger):
   
    Buscando = []
    LDaño = []
    LDaño = FDaño(danger)
    for i in range(len(List)):
        if any(elem in List[i]['zoneDangerous'] for elem in LDaño):
            Buscando.append(List[i])
    return Buscando

def PMascotas(List,mascota):
   
    Buscando = []
    for i in range(len(List)):
        if(List[i]['isPetFriendly'] == mascota):
            Buscando.append(List[i])
    return Buscando

def Actividad_Comercial(List, Actividad):

    matching = []
    for i in range(len(List)):
        if(Actividad in List[i]['commercialActivities']):
            matching.append(List[i])
    return matching

def precio(List, budget):
    
    Buscando = []
    for i in range(len(List)):
        if(List[i]['price']<=budget):
            Buscando.append(List[i])
    return Buscando
