from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


def getCompressedString(input) :
	# Write your code here.
	n = len(input)
	if n == 0:
		return ""
	startChr = 0
	endChr = 0
	output = ""
	while startChr < n:
		while endChr < n and input[endChr] == input[startChr]:
			endChr += 1
		totalChrCount = endChr - startChr
		if totalChrCount > 1:
			output += input[startChr]  + str(totalChrCount)
		else:
			output += input[startChr]
		startChr = endChr
	return output

# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)
