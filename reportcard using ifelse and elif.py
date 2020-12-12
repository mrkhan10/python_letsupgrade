#Report card using ifelse and ELIF
marks = int(input("Enter the your marks"))

if marks >= 85 :
    print("Distinction")
elif marks>=70 and marks <85 :
    print("First class")
elif marks>=60 and marks <70 :
    print("Second class")
elif marks>=35 and marks <60:
    print("Pass")
elif marks>=0 and marks <35:
    print("Fail")
else:
    print("Invalid input")