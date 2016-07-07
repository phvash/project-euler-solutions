def fetchRows():
	tableObj = open('numbers','r')
	spacedTable = tableObj.readlines()

	#eliminate '\n'
	count = 1
	row = {}
	for line in spacedTable:
		#remove '\n at the end of the line'
		strippedLine =  line.strip('\n')
		#save the numbers in the row as a list
 		ListofNum = strippedLine.split(' ')
 		#add the list of nums on the line to the row dict
 		row[count] = ListofNum
 		count += 1

 	return row

def getColumns(row):
	col = {}
	for colNum in xrange(1,len(row)+1):
		column = []
	 	for rowNum in xrange(1,len(row)+1):
			value = (row[rowNum])[colNum-1]
			column.append(value)
		col[colNum] = column
	return col

def product(list):
	return int(list[0])*int(list[1])*int(list[2])*int(list[3])

def rowPOF(row):
	'''product of fours in each row'''
	rowsMaxPofs = []
	for rowNum in xrange(1,len(row)+1):
		pofs = []

		#get all products of fours in a row
		for rowNumIndex in xrange(0,len(row[rowNum])-3):
			pofs.append(product((row[rowNum])[rowNumIndex:rowNumIndex+4]))
		
		rowsMaxPofs.append(max(pofs))
	
	return max(rowsMaxPofs)

def colPOF(col):
	'''product of fours in each col'''
	colsMaxPofs = []
	for colNum in xrange(1,len(col)+1):
		pofs = []

		#get all products of fours in a row
		for colNumIndex in xrange(0,len(col[colNum])-3):
			pofs.append(product((col[colNum])[colNumIndex:colNumIndex+4]))
		#get the max product for each line
		colsMaxPofs.append(max(pofs))
	
	return max(colsMaxPofs)
def rowPOFLeft(row):
	'''product of fours in each row'''
	rowsMaxPofs = []
	for rowNum in xrange(1,len(row)+1):
		pofs = []

		#get all products of fours in a row
		for rowNumIndex in xrange(0,len(row[rowNum])-3):
			pofs.append(product(((row[rowNum])[::-1])[rowNumIndex:rowNumIndex+4]))
		
		rowsMaxPofs.append(max(pofs))
	
	return max(rowsMaxPofs)

def colPOF2Up(col):
	'''product of fours in each col'''
	colsMaxPofs = []
	for colNum in xrange(1,len(col)+1):
		pofs = []

		#get all products of fours in a row
		for colNumIndex in xrange(0,len(col[colNum])-3):
			pofs.append(product(((col[colNum])[::-1])[colNumIndex:colNumIndex+4]))
		#get the max product for each line
		colsMaxPofs.append(max(pofs))
	
	return max(colsMaxPofs)

def getDiagonal(row,col):
	#get upper diagonnal
	count = 1
	for colNum in xrange(1,len(col)+1)
		diagonnal = []
		for index in xrange(1,len(col)+1):
			value = (row[index])[index]
			diagonal.append(value)

def main():
	row = fetchRows()
	col = getColumns(row)
	maxPofsRight = rowPOF(row)
	maxPofsDown = colPOF(col)
	maxPofsLeft = rowPOFLeft(row)
	maxPofsUp = colPOF2Up(col)
	print (maxPofsRight)
	print (maxPofsDown)
	print (maxPofsLeft)
	print (maxPofsUp)


if __name__ == '__main__':
	main()