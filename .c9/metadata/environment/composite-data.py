{"filter":false,"title":"composite-data.py","tooltip":"/composite-data.py","undoManager":{"mark":17,"position":17,"stack":[[{"start":{"row":3,"column":0},"end":{"row":4,"column":11},"action":"insert","lines":["import csv","import copy"],"id":1}],[{"start":{"row":4,"column":11},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":["myVehicle = {","    \"vin\" : \"<empty>\",","    \"make\" : \"<empty>\" ,","    \"model\" : \"<empty>\" ,","    \"year\" : 0,","    \"range\" : 0,","    \"topSpeed\" : 0,","    \"zeroSixty\" : 0.0,","    \"mileage\" : 0","}"],"id":3}],[{"start":{"row":15,"column":1},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":38},"action":"insert","lines":["for key, value in myVehicle.items():","    print(\"{} : {}\".format(key,value))"],"id":5}],[{"start":{"row":18,"column":38},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":20,"column":0},"action":"insert","lines":["",""]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "],"id":7}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":20},"action":"insert","lines":["myInventoryList = []"],"id":8}],[{"start":{"row":20,"column":20},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":21,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":22,"column":0},"end":{"row":42,"column":42},"action":"insert","lines":["with open('car_fleet.csv') as csvFile:","    csvReader = csv.reader(csvFile, delimiter=',')  ","    lineCount = 0  ","    for row in csvReader:","        if lineCount == 0:","            print(f'Column names are: {\", \".join(row)}')  ","            lineCount += 1  ","        else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","    print(f'Processed {lineCount} lines.')"],"id":10}],[{"start":{"row":42,"column":42},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"insert","lines":["    "]},{"start":{"row":43,"column":4},"end":{"row":44,"column":0},"action":"insert","lines":["",""]},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"remove","lines":["    "],"id":12},{"start":{"row":43,"column":4},"end":{"row":44,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":43,"column":4},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"remove","lines":["    "],"id":14}],[{"start":{"row":44,"column":0},"end":{"row":44,"column":41},"action":"insert","lines":["currentVehicle = copy.deepcopy(myVehicle)"],"id":15}],[{"start":{"row":44,"column":41},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":16}],[{"start":{"row":45,"column":0},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":17}],[{"start":{"row":46,"column":0},"end":{"row":49,"column":22},"action":"insert","lines":["for myCarProperties in myInventoryList:","    for key, value in myCarProperties.items():","        print(\"{} : {}\".format(key,value))","        print(\"-----\")"],"id":18}]]},"ace":{"folds":[],"scrolltop":526,"scrollleft":0,"selection":{"start":{"row":39,"column":15},"end":{"row":39,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1636552963891,"hash":"119a2d33826ae9b0e038acafa15207f805b33566"}