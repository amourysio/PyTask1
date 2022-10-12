##                     Fizz Buzz Game
print("-----    Fizz Buzz Game  -----")
## User Input:
userNumber = int(input("Please Enter Number :"))

## Logic
for i in range(userNumber + 1):

  if (i % 5 == 0 and i % 3 == 0):
    print("Number ", i, " : ", "FizzBuzz")
  else:
    if (i % 3 == 0):
      print("Number ", i, " : ", "Fizz")
    elif (i % 5 == 0):
      print("Number ", i, " : ", "Buzz")
    else:
      print("Number ", i, " : ", "An Indivisible Number!")


##              The 5th number of prime number
print("-----    The 5th number of prime number      -----")

## User Input:
fromValue = int(input("Please, Enter the Lowest Range Value: "))
toValue = int(input("Please, Enter the Upper Range Value: "))
count = 0


## Logic
for number in range(fromValue, toValue + 1):
    if(number > 1):
        for i in range(2,number):
            if(number % i) == 0:
                break
        else:
            count += 1
            if(count == 5):
                  print("The 5th number of prime number is :",number)

