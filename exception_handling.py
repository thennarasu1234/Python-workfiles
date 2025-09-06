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