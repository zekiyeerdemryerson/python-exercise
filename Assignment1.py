# Based on Canada's government labour market indicators in August 2020, the unemployment population in Toronto decreased to
# approximately 518 thousand in August of 2020 with a month-to-month change rate of -2.5 percent.


cityName = "Toronto"
augPopulation = 518
changeRate = -0.025
decreasing = True


# Print every literal and type of the variables in Q1.a in a separate new line.
# help(print)


print(cityName, augPopulation, changeRate, decreasing, sep="\n")


# print(type(changeRate))

# If the unemployment rate stays the same in September, find how many people would still be unemployed? Round off the answer to the nearest whole number.

sepPopulation = round(augPopulation + (changeRate * augPopulation))
txt = "Unemployment Population in September is {} thousand"
print(txt.format(sepPopulation))

# Find the difference between the unemployment population of August and that of September.

diff_Pop = augPopulation - sepPopulation
txt2 = (
    "Unemployment Population difference between August to September is {} thousand less"
)
print(txt2.format(diff_Pop))

# Convert the variable augPopulation to a floating-point number then print the new literal and type
sepPopulation = float(sepPopulation)
print(sepPopulation, type(sepPopulation))

# Given that var1 is the sepPopulation variable rounded to
# the nearest whole number, and var2 is the changeRate variable rounded to two decimal places.
# Print the following statement: The unemployment populaton might be var1 thousand in September 2020, which is a var2 month-to-month change rate.
txt3 = " The unemployment populaton might be {} thousand in September 2020, which is a {} month-to-month change rate"
print(txt3.format(round(sepPopulation), round(changeRate, 2)))

# Q2 Create a list of numbers called nmbrs starting at 0 and ending at 21, using the following code:

nmbrs = list(range(22))
print(nmbrs, end=" ")
# Print the nmbrs list in reverse order using a simple for loop.

for rnm in range(len(nmbrs) - 1, -1, -1):
    print(rnm, end=" ")

# Print the numbers that are divisible by 7 in the nmbrs list.
