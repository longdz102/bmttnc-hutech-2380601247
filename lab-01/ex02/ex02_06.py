input_str = input("Nhap X, Y: ")
dismensions=[int(x) for x in input_str.split(',')]
rowNum=dismensions[0]
colNum=dismensions[1]
multilish = [[0 for col in range(colNum)] for now in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilish[row][col]= row*col
print (multilish)