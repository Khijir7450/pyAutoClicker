from clicker import clicky


print("Enter how many position you want to click: ")
noOfPosition = int(input())

print("Enter time difference between two click(sec): ")
sleepTime = int(input())

clicky(sleepTime, noOfPosition)