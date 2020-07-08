# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

def fizzbuzz(num):
    if int(num) % 3 == 0 and int(num) % 5 == 0:
        return "FizzBuzz"
    elif int(num) % 3 == 0 and int(num) % 5 != 0:
        return "Fizz"
    elif int(num) % 3 != 0 and int(num) % 5 == 0:
        return "Buzz"
    else:
        return num
