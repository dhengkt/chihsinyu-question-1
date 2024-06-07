def changeSequence(inputArr):
	arrIndex = len(inputArr)

	if(inputArr[0] < inputArr[1]):
		for x in range(arrIndex):
			if(inputArr[x] > inputArr[x + 1]):
				result = x
	else:
		for x in range(arrIndex):
			if(inputArr[x] < inputArr[x + 1]):
				result = x
	result = -1


if __name__ == '__main__':
	case1 = [1, 2, 4, 8, 4, 2]
	case2 = [10, 8, 6, 6, 8, 12]
	case3 = [16, 16, 16]
    changeSequence(case1)
    changeSequence(case2)
    changeSequence(case3)