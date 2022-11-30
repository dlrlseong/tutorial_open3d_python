
originalPCD = open("S_10_0001_1_I.pts", "r")
resultPCD = open("result.pts", "w")
while(True):
    line = originalPCD.readline()
    # print(line)
    list = line.split(" ")
    # print(list)
    for i in range (0, 6):
        resultPCD.write(list[i] + " ")
    
    resultPCD.write("\n")
    # exit()
    if not line:
        break

# print(originalPCD)
originalPCD.close()
resultPCD.close()