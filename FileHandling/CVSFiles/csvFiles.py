import csv

#Reading CSV File

def reading_file(filename):
    fields=[]
    rows=[]
    with open(filename,'r') as csvfile:
        #Creating a csv reader object
        csvreader=csv.reader(csvfile,delimiter=',')

        # extracting field names through first row
        fields = next(csvreader)
        print(fields)

        for row in csvreader:
            rows.append(row)

        print(fields)
        for row in rows:
            for col in row:
                print("%3s" % col, end=" "),
            print('\n')

# reading_file("AAPL.csv")

def writing_file(filename):
    with open(filename,'a',newline='') as csvfile:
        writer=csv.writer(csvfile,delimiter=",")

        # writer.writerow(["2014-11-30",116.849998,119.750000,116.620003,118.930000,112.124863,181873900])

        data=[["2014-11-25",116.849998,119.75,116.620003,118.93,112.124863,181873900],
            ["2014-11-26",116.849998,119.75,116.620003,118.93,112.124863,181873900],
            ["2014-11-27",116.849998,119.75,116.620003,118.93,112.124863,181873900],
            ["2014-11-28",116.849998,119.75,116.620003,118.93,112.124863,181873900]]
        #Write Multiple Rows
        writer.writerows(data)
writing_file("AAPL.csv")

reading_file("AAPL.csv")