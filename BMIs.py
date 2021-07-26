# Lists to store data of the text file
names = []
heights = []
weights = []

# Opening text file in read mode
File = open("data.txt", 'r')
# Reading all lines of the text file into a list
allLines = File.readlines()

# Loop to iterate in the range from 1 to length of allLines
for i in range(1, len(allLines)):
	# Getting the line at index i of the list allLines
	line = allLines[i]
	# Stripping the line to eliminate extra space at both ends
	line = line.strip()
	# Splitting the line into list of strings
	line = line.split('\t')
	# Adding name to the names list
	names.append(line[0])
	# Adding height to the heights list
	heights.append(float(line[1]))
	# Adding weigth to the weigths list
	weights.append(float(line[2]))
# Closing the text file after reading
File.close()

# List to store BMIs
BMIs = []

# Loop to iterate in the range from 0 to length of names list
for i in range(len(names)):
	# Calculating bmi
	bmi = weights[i] / heights[i] ** 2
	# Rounding the bmi to 2 decimal places
	bmi = round(bmi, 2)
	# Adding the bmi to BMIs list
	BMIs.append(bmi)

# Calculating maximums
max_height = max(heights)
max_weight = max(weights)
max_bmi = max(BMIs)

# Calculating minimums
min_height = min(heights)
min_weight = min(weights)
min_bmi = min(BMIs)

# Calculating averages
avg_height = sum(heights) / len(heights)
avg_weight = sum(weights) / len(weights)
avg_bmi = sum(BMIs) / len(BMIs)

# Printing columns in tabular format
print("{:<12s}{:<12s}{:<12s}{:<12s}".format('Name','Height(m)','Weight(kg)','BMI'))
for i in range(len(names)):
	print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(names[i],heights[i],weights[i],BMIs[i]))

print("\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Average',avg_height,avg_weight,avg_bmi))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Max',max_height,max_weight,max_bmi))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Min',min_height,min_weight,min_bmi))


# Opening text file in write mode
File = open('Modified_data.txt', 'w')
# Writing columns into the text file
File.write("Name\tHeight(m)\tWeight(kg)\tBMI\n")
for i in range(len(names)):
	File.write("{}\t{:.2f}\t{:.2f}\t{:.2f}\n".format(names[i],heights[i],weights[i],BMIs[i]))
# Closing the text file after writing
File.close()

