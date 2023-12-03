# Part 1

# Read in the bag pulls
bag_pull = open('/Users/byronbootspmbp/GitHub_Projects/adventofcode2023/Day2/input2.txt', 'r')

sum1 = 0

for pull in bag_pull:
    # start off assuming bag pull is valid
    valid = True
    # split to get the bag id
    bag_id, pull = pull.split(':')
    # Get each individual pull
    for cubes in pull.split(';'):
        # Get the set of cubes from each individual pull
        for options in cubes.split(','):
            # Get our number and color values in individual variables
            number, color = options.split()
            if int(number) > 14:
                valid = False
            elif int(number) > 12 and color == 'red':
                valid = False
            elif int(number) > 13 and color == 'green':
                valid = False
    # if our pull was valid, add our bag id 
    if valid:
        sum1 += int(bag_id[5:])
                        
print(sum1)


# Part 2

bag_pull = open('/Users/byronbootspmbp/GitHub_Projects/adventofcode2023/Day2/input2.txt', 'r')

sum2 = 0

for pull in bag_pull:
    # initialize variables to keep track of each color's max
    red_max = 0
    green_max = 0
    blue_max = 0
    # split to get the bag id
    bag_id, pull = pull.split(':')
    # Get each individual pull
    for cubes in pull.split(';'):
        # Get the set of cubes from each individual pull
        for options in cubes.split(','):
            # Get our number and color values in individual variables
            number, color = options.split()
            # check if we have a new max for each color
            if color == 'red' and int(number) > red_max:
                red_max = int(number)
            elif color == 'green' and int(number) > green_max:
                green_max= int(number)
            elif color == 'blue' and int(number) > blue_max:
                blue_max = int(number)
    # multiply our maxes and add the power to our sum
    power = red_max * green_max * blue_max
    sum2 += power
                        
print(sum2)