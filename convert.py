# This file is meant to convert plain text breast-cancer.data
# into all numerical values, follow dictionary and comments
# for conversion values

rec_events = {"recurrence-events" : 1, "no-recurrence-events" : 0}
age_groups = {"10-19" : 1, "20-29" : 2, "30-39" : 3, "40-49" : 4, "50-59" : 5, "60-69" : 6, "70-79" : 7, "80-89" : 8, "90-99" : 9}
menopause = {"premeno" : 0, "lt40" : 1, "ge40" : 2}
tumor_size = {"0-4" : 1, "5-9" : 2, "10-14" : 3, "15-19" : 4, "20-24" : 5, "25-29" : 6, "30-34" : 7, "35-39" : 8, "40-44" : 9, "45-49" : 10, "50-54" : 11, "55-59" : 12}
inv_nodes = {"0-2" : 1, "3-5" : 2, "6-8" : 3, "9-11" : 4, "12-14" : 5, "15-17" : 6, "18-20" : 7, "21-23" : 8, "24-26" : 9, "27-29" : 10, "30-32" : 11, "33-35" : 12, "36-39" : 13}
deg_malig = {"1" : 1, "2" : 2, "3" : 3}
breast_quad = {"?" : 0, "left_up" : 1, "left_low" : 2, "right_up" : 3, "right_low" : 4, "central" : 5}


# Function converts our data into numerical values for use with a neural network
def convertData(file):
    with open(file) as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    data = [x.split(",") for x in data]

    for x in data:
        # Recurrence events, no-recurrence = 0 recurrence = 1
        x[0] = rec_events[x[0]]
        # Age groups 1,2,3,4,5,6,7,8,9
        x[1] = age_groups[x[1]]
        # Menopause, premno = 0, lt40 = 1, ge40 = 2
        x[2] = menopause[x[2]]
        # Tumor-size, 1-12
        x[3] = tumor_size[x[3]]
        # Inv-nodes, 1-13
        x[4] = inv_nodes[x[4]]
        # Node-caps, yes = 1, no = 0
        if x[5] == "yes":
            x[5] = 1
        else:
            x[5] = 0
        # Deg-malig
        x[6] = deg_malig[x[6]]
        # Breast, right = 1, left = 0
        if x[7] == "right":
            x[7] = 1
        else:
            x[7] = 0
        # Breast-quad, left-up = 1, left-low = 2, right-up = 3, right-low = 4, central = 5
        x[8] = breast_quad[x[8]]
        # Irradiat, yes = 1, no = 0
        if x[9] == "yes":
            x[9] = 1
        else:
            x[9] = 0
    return data


# Writes a file with our numerical data values for use with our neural network

def writeFile(file, data):
    with open(file, "w") as f:
        for x in data:
            # f.write(str(x[0]) + "," + str(x[1]) + "," + str(x[2]) + "," + str(x[3]) + "," + str(x[4]) + "," + str(x[5])  + "," + str(x[6]) + "," + str(x[7]) + "," + str(x[8]) + "," + str(x[9]) + "\n") # Original numerical file
            f.write(str(x[0]) + "," + str(x[1]) + "," + str(x[2]) + "," + str(x[3]) + "," + str(x[4]) + "," + str(x[5]) + "," + str(x[7]) + "," + str(x[8]) + "," + str(x[9]) + "," + str(x[6]) + "\n") # Fixed numerical file (adds x[6] (deg-malig) to end of numerical lines for easier data manipulation)


numdata = convertData("breast-cancer.data") # Original breast cancer data file
#writeFile("breast-cancer-num.data", numdata) # Original numerical data
#writeFile("breast-cancer-num-fixed.data", numdata) # Fixed numerical data
