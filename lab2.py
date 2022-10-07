n = int(input("How many numbers do you want to use today?:"))
if n>0:

    firstValue = int(input("Enter the first number:"))

    largest = firstValue
    smallest = firstValue
    total = firstValue

    counter = 0
    while counter < (n-1):
        current = int(input("enter the next number:"))
        total = total+current
        counter = counter+1
        if current<smallest:
            smallest = current
        elif current>largest:
            largest = current

    print("the average of the value is:",total/n)
    print("the smallest of the value is {}".format(smallest))
    print("the largest of the value is {}".format(largest))
    print("the range of the value is {}".format(largest-smallest))

else:
    print("you did not want to use any numbers today.")


