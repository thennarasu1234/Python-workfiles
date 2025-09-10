# try,except,finally,else

n=10
print(n/0)

try:
    n=0
    print(n/0)
except IndexError as e:
    print("ar")
except ZeroDivisionError as e:
    print("div")

else:
    print("no error")
finally:
    print("anyway i execute")


# new

n = 10

try:
    num1 = int(input("enter a number:"))
    num2 = int(input("enter a another number:"))
    result = num1/num2
    print(*"result:",result)

except ZeroDivisionError:
    print("Error : cannot divided by zero!")
except ValueError:
    print("Error: please enter only number!")
finally:
    print("execution completed")