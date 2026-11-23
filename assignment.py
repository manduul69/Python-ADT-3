# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Enqueue() and Dequeue() - move the pointers yourself.

# Exercise 1
Queue = []
for x in range(8):
    Queue.append(-1)
HeadPointer = 0
TailPointer = -1


def IsEmpty():
    if TailPointer > -1:
        return False
    return True


def IsFull():
    if TailPointer == 4:
        return True
    return False


# Exercise 2
def Enqueue(Data):
    global Queue, HeadPointer, TailPointer
    if TailPointer == 4:
        return False
    TailPointer = TailPointer + 1
    Queue[TailPointer] = Data
    return True


# Exercise 3
def Dequeue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer == -1 or HeadPointer > TailPointer:
        return -1
    DataToReturn = Queue[HeadPointer]
    HeadPointer = HeadPointer + 1
    return DataToReturn


# Exercise 4
def Peek():
    global Queue, HeadPointer, TailPointer
    if IsEmpty() == True:
        return -1
    return Queue[HeadPointer]


def ShowQueue():
    global Queue, HeadPointer, TailPointer
    String = ""
    if IsEmpty() == True:
        return String
    for x in range(HeadPointer,TailPointer+1):
        String = String + f"{Queue[x]} "
    return String


# Exercise 5
def Canteen(Commands):
    global Queue, HeadPointer, TailPointer
    HeadPointer = 0
    TailPointer = -1
    List = []
    for x in Commands:
        if x == "serve":
            student = Dequeue()
            if student == -1:
                List.append(student)
        else:
            S = x.split(" ")
            name = S[1]
            Enqueue(name)
    return List

print(Canteen(["join Bat", "join Anu", "serve", "join Saraa", "serve", "serve"]))
print(Canteen(["serve", "join Bat"]))
