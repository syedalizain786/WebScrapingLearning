#File Handling in Python

#Reading data from file
def readingFile(filename):
    try:
        file=open(filename,'r')

        text=file.read()

        #Using Print to print all content of file
        print(text)

        #Using for loop
        for l in file:
            print(l)

        file.close()

        #Using with
        with open('sample.txt', 'r') as withFile:
            data=withFile.read()


        print(data)
        withFile.close()

        #Using with
        with open('sample.txt', 'r') as linesRead:
            data=linesRead.readlines()
            #Read lines and split them when space is encountered or give split argument you want
            for line in data:
                word=line.split()
                print(word)

            linesRead.close()
    except Exception as e:
        print(e)

readingFile("writingFile.txt")


#Writing in a txt file

def writingFile(filename):
    try:
        file=open(filename,'w')

        #w mode write in file and override the previous content
        file.write("This is writing modeee\n")
        file.write("I'm writing inside file and overriding")
        file.close()


        #With use of with statement our file automaticaaly closes no need to call f.close()
        with open(filename,'w') as file:
            file.write("\n Writing with with mode")

    except Exception as e:
        print("Error: "+e)

writingFile("writingFile.txt")


#Append in a text File
def appendFile(filename):
    try:
        with open(filename,'a') as f:
            f.write("\n I'm in append mode")
    except Exception as e:
        print("Error"+e)

appendFile("sample.txt")

def fileFuncstions(filename):
    with open(filename) as file:

        #Seek function will go to that byte and reject the previous bytes
        file.seek(10)

        #Tell func tells where are we in file or for seeking to a relevant position with in file
        print(file.tell())
        #Giving no to read will read just that no of bytes
        data=file.read(5)
        print(data)
fileFuncstions("sample.txt")


