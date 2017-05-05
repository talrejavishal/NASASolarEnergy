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

"""

csv_file = "dataset_solar2.csv"
text_file = open("temp.txt","w")

df = pd.read_csv(csv_file)
date_col = df['TIME']
date_col = date_col.values
print date_col.size
temp = pd.Series(range(1,date_col.size))
df['TempDate'] = temp
#df.to_csv("Temp.csv")
rowIdx = 1
val = 1000000676
idx = 0
print df.iloc[[0]]['RADIATION']
cur = "00:00:08"
print type(cur)
radiation = 0
pressure = 0
humidity = 0
temperature = 0
wind_dir_deg = 0
wind_speed = 0
startIdx = 0
endIdx = -1
for i in range(0,date_col.size):
    val = str(df.iloc[i]['TIME'])
    #print val,cur
    if val[:2] == cur[:2]:
        radiation += df.iloc[i]['RADIATION']
        pressure += df.iloc[i]['PRESSURE']
        humidity += df.iloc[i]['HUMIDITY']
        temperature += df.iloc[i]['TEMPERATURE']
        wind_dir_deg += df.iloc[i]['WIND_DIRECTION_DEGREES']
        wind_speed += df.iloc[i]['WIND_SPEED']
        #print radiation
    else:
        #print radiation
        endIdx = i-1
        num = endIdx-startIdx+1
        radiation /= num
        pressure /= num
        humidity /= num
        temperature /= num
        wind_dir_deg /= num
        wind_speed /= num
        date = str(df.iloc[endIdx]['DATE'])
        finalTime = val[:2]
        nxtHour = int(finalTime)
        begHour = int(cur[:2])
        diff = nxtHour - begHour
        if diff != 1:
            if begHour == 23:
                nxtHour = 0
            else:
                nxtHour = begHour + 1

        finalTime = str(nxtHour)
        if finalTime == "00":
            finalTime = "24"
        text_file.write(str(date)+","+finalTime+","+str(radiation)+","+str(pressure)+","+str(humidity)+","+str(temperature)+","+str(wind_dir_deg)+","+str(wind_speed)+"\n")
        #print "T:",startIdx,endIdx
        startIdx = i
        radiation = df.iloc[i]['RADIATION']
        pressure = df.iloc[i]['RADIATION']
        humidity = df.iloc[i]['RADIATION']
        temperature = df.iloc[i]['RADIATION']
        wind_dir_deg = df.iloc[i]['RADIATION']
        wind_speed = df.iloc[i]['RADIATION']
        cur = val

text_file.close()


"""

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
