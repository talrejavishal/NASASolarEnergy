import pandas as pd
import csv

def transferToCsv(data,fileName):

    """
    :param data:string
    :param fileName:string
    :param season:string
    :return:none

    This function takes the listoflists (data) and adds the corresponding matches for a particular seasons
    into the variable data. After that, the data variable is written line by line into the Scoreboard_all.csv file
    """

    with open(fileName, "r") as ins:
        for line in ins:
            val = str(line)
            val = val.rstrip('\n')
            x = val.split(",")
            print x
            data.append(x)



csv_file = "dataset_solar2.csv"
#text_file = open("temp.txt","w")

df = pd.read_csv(csv_file)
date_col = df['TIME']
date_col = date_col.values
#print date_col.size
temp = pd.Series(range(1,date_col.size))
#df.to_csv("Temp.csv")
rowIdx = 1
val = 1000000676
idx = 0
#print df.iloc[[0]]['RADIATION']
cur = "00"
#print type(cur)

startIdx = 0
endIdx = -1
for i in range(0,date_col.size):
    val = str(df.iloc[i]['TIME'])
    print val[:2,],cur[:2]
    if val[:2] == cur[:2]:
        #print radiation
    else:
        #print radiation
        endIdx = i-1
        num = endIdx-startIdx+1
        date = str(df.iloc[endIdx]['DATE'])
        finalTime = val[:2]
        if finalTime == "00":
            finalTime = "24"
        #text_file.write(str(date)+","+finalTime+","+str(radiation)+","+str(pressure)+","+str(humidity)+","+str(temperature)+","+str(wind_dir_deg)+","+str(wind_speed)+"\n")
        print "T:",startIdx,endIdx
        startIdx = i
        cur = val

#text_file.close()


data = []

# Initializing a blank .csv file
with open("FinalData.csv", "wb") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in data:
        writer.writerow(line)


# Appending the Column data for the .csv file
data.append("DATE,TIME,RADIATION,PRESSURE,HUMIDITY,TEMPERATURE,WIND_DIRECTION_DEGREES,WIND_SPEED".split(","))
transferToCsv(data,"temp.txt")

with open("FinalData.csv", "ab") as csv_file:  # Opens the .csv file in append binary mode.
    writer = csv.writer(csv_file, delimiter=',')
    for line in data:
        writer.writerow(line)


csv_file.close()
