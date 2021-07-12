# Taken from my own Git/Datastructures/Stack:
class stack:
    def __init__(self):
        self.Internal_List = []
        self.size = 0

    def peek(self):
        return self.Internal_List[self.size-1]

    def is_empty(self):
        return self.size == 0

    def pop(self):
        element = self.Internal_List.pop(self.size-1)
        self.size -= 1

        return element

    def push(self, element):
        self.Internal_List.append(element)
        self.size += 1

    def __len__(self):
        return self.size

aux = stack()
pairs = int(input())
sock_pile = list(map(int,input().split()))

for sock in sock_pile:
    if(not aux.is_empty() and aux.peek() == sock):
        aux.pop()
    else:
        aux.push(sock)

#print(aux.Internal_List, aux.size)

if(aux.is_empty()):
    print(2 * pairs)
else:
    print("impossible")
