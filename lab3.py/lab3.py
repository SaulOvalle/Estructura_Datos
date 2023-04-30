import json
def readJsonFile(fileRoot):
    data = [] 
    with open(fileRoot) as jsonFile:
        for line in jsonFile:
            data.append(json.loads(line))
    return data

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   #Funcion de insertar
   def insert(self, data):
      if self.data['dpi']:
         if data['dpi'] < self.data['dpi']:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data['dpi'] > self.data['dpi']:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data

#Funcion de busqueda modificada para los dpis
def search(root, search):
    currentNode = root
    while(currentNode.data['dpi'] != search):
        if(search > currentNode.data['dpi']):
            currentNode = currentNode.right
        if(search < currentNode.data['dpi']):
            currentNode = currentNode.left
        if(search == currentNode.data['dpi']):
            return currentNode.data
        elif(currentNode.left == None and currentNode.right == None):
            return None