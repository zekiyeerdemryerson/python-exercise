#Based on Canada's government labour market indicators in August 2020, the unemployment population in Toronto decreased to 
# approximately 518 thousand in August of 2020 with a month-to-month change rate of -2.5 percent.

# Create four variables: cityName as String (Toronto), augPopulation as Integer (518), changeRate as 
# Floating-point number (-2.5%), and decreasing as Boolean (True).


#Print every literal and type of the variables in Q1.a in a separate new line.

cityName="Toronto"
augPopulation=518
changeRate=-2.5/100
decreasing=True

print(cityName,augPopulation,changeRate,decreasing,sep="\n") 
# If the unemployment rate stays the same in September, find how many people would still be unemployed? Round off the answer to the nearest whole number.

#Unemployment Population in September is 505 thousand
septPopulation=round(augPopulation+changeRate*augPopulation) 
print(f"Unemployment Population in September is {septPopulation} thousand") 

#Find the difference between the unemployment population of August and that of September.
#Unemployment Population difference between August to September is 13 thousand less
diffPop = augPopulation-septPopulation
print(f"Unemployment Population difference between August to September is {diffPop} thousand less")
#Convert the variable augPopulation to a floating-point number then print the new literal and type
newAugPop=float(augPopulation)
print(type(newAugPop))
#Given that var1 is the sepPopulation variable rounded to
# the nearest whole number, and var2 is the changeRate variable rounded to two decimal places. 
var1=round(septPopulation)
var2=round(changeRate,2)
# Print the following statement: The unemployment populaton might be var1 thousand in September 2020, which is a var2 month-to-month change rate.
print(f"The unemployment populaton might be {var1} thousand in September 2020, which is a {var2} month-to-month change rate.")

#Q2 Create a list of numbers called nmbrs starting at 0 and ending at 21, using the following code:
nmbrs = list(range(22))
print(nmbrs, end="\n")

 #Print the nmbrs list in reverse order using a simple for loop. 
for rnmbrs in range(len(nmbrs)-1,-1,-1):
    print(rnmbrs,end=" ") 

# Print the numbers that are divisible by 7 in the nmbrs list.