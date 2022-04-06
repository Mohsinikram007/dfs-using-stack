graph = {
    'a' : ['b','c'],
    'b' : ['d','e'],
    'c' : ['f','h'],
    'd' : [],   
    'e' : [],   
    'f' : [],   
    'h' : []
} 
source ='a'



path = []

stack = [source]

path.append(source)
stack.append(source)

while stack:
    s = stack.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in path:
        path.append(neighbour)
        stack.append(neighbour)
