## Part 1

# Open our input list and read into our variable
calibration_values = open('/Users/byronbootspmbp/GitHub_Projects/adventofcode2023/Day1/input1.txt', 'r')

# set a sum variable to keep track of total calculated sum from the calibration values
sum1 = 0
# iterate through each line of calibration_values taking each line as its own value
for value in calibration_values:
    # initialize empty array to store found digits
    digits = []
    # iterate through the full string line to find the first and last digits
    for number, digit in enumerate(value):
        # if the character we're on isnumeric, if it is add it to our digits array
        if digit.isdigit():
            digits.append(digit)
    # concatenate and then sum our first and last 
    sum1 += int(digits[0]+digits[-1])
        
print(sum1)



## Part 2

# Open our input list and read into our variable
calibration_values = open('/Users/byronbootspmbp/GitHub_Projects/adventofcode2023/Day1/input1.txt', 'r')

# set a sum variable to keep track of total calculated sum from the calibration values
sum2 = 0
# iterate through each line of calibrationvalues taking each line as its own value
for value in calibration_values:
    # initialize empty array to store found digits
    digits = []
    # iterate through the full string line to find the first and last digits
    for number, digit1 in enumerate(value):
        # if the character we're on isnumeric, if it is add it to our digits array
        if digit1.isdigit():
            digits.append(digit1)
        # if we found the word representation of a digit add the numeric digit as a string to our digits array
        for string, digit2 in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            if value[number:].startswith(digit2):
                digits.append(str(string+1))
    # concatenate and then sum our first and last digits
    sum2 += int(digits[0]+digits[-1])
    
print(sum2)