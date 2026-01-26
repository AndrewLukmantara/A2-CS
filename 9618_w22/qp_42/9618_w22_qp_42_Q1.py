global Jobs
Jobs = [[0 for _ in range(2)] for _ in range(100)] # ARRAY[0:99, 0:1] OF INTEGER
global NumberOfJobs
NumberOfJobs = 0 # INTEGER


def Initialise():

    for i in range(100): # i : INTEGER
        Jobs[i][0] = -1
        Jobs[i][1] = -1


def AddJob(JobNumber, Priority):

    global NumberOfJobs

    for i in range(100):
        if Jobs[i][0] == -1:
            Jobs[i][0] = JobNumber
            Jobs[i][1] = Priority
            NumberOfJobs += 1
            print("Added")
            return

    print("Not added")

Initialise() 
AddJob(12, 10) 
AddJob(526, 9) 
AddJob(33, 8) 
AddJob(12, 9) 
AddJob(78, 1)

def InsertionSort():
    for i in range(1, NumberOfJobs):
        keyJob = Jobs[i][0] # INTEGER
        keyPriority = Jobs[i][1] # INTEGER

        j = i - 1 # j : INTEGER
        while j >= 0 and keyPriority < Jobs[j][1]:
            Jobs[j+1][0] = Jobs[j][0]
            Jobs[j+1][1] = Jobs[j][1]
            j -= 1

        Jobs[j+1][0] = keyJob
        Jobs[j+1][1] = keyPriority

def PrintArray():
    i = 0
    while Jobs[i][0] != -1 and i < 100:
        print(f"{Jobs[i][0]} priority {Jobs[i][1]}")
        i = i + 1

InsertionSort()
PrintArray()
        


