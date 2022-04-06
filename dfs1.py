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

if source is None or source not in graph:
   pass

path = []

stack = [source]

while(len(stack) != 0):

    s = stack.pop()

    if s not in path:

        path.append(s)

    if s not in graph:

        # leaf node
        continue

    for neighbor in graph[s]:

        stack.append(neighbor)         
    print(" ".join(path))
