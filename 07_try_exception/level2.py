try:
    x = int("hello")
    print("A")
except ValueError:
    print("B")
except Exception:
    print("C")
    #will print B as it is value error 
try:
    x = 10 / 0
    print("A")
except ValueError:
    print("B")
except ZeroDivisionError:
    print("C")
except Exception:
    print("D")
    #c will be printed as we have divided by zero error

try:
    numbers = [10, 20]
    print(numbers[5])
except Exception:
    print("A")
except IndexError:
    print("B")
#A as it is exception it will stop program here and we will never reach to B

def safe_divide(a, b):
    try:
      divide = a/b
      return divide
    except ZeroDivisionError:
        print('canot be divided by zero')
    except TypeError:
        print('Enter proper number')
        
safe_divide(10, 0)
safe_divide("10", 2)
try:
    age = int(input("Age: "))

except Exception:
    print("Something went wrong.")

except ValueError:
    print("Age must be a number.")
# Why is the order problematic?becz exception is first we will not know actual error
# Which except should come first?ValueError
# Which should come last?Exception