

weight = int(input("Enter your weight: "))
unit= input("(L)bs or (K)g:").upper()

if unit == 'L':
    conversion= weight * .45
    print("Your weight in KG is: " + str(conversion))
else:
    conversion= weight / .45
    print(f"Your weight in LBS is: {conversion}")