course = "Python's Course for Beginners"
course = 'Python for "Beginners"'

print("The first character: " + course[0])
print("The last character: " + course[-1])
print("The range of 0 to 6 first character (The last index is exclusive): " + course[0:6])
print("The range with default values: " + course[6:])
print("Using func upper: " + course.upper())
print("Using func lower: " + course.lower())
print("Find the first 'Be' index in the course variable: " + str(course.find("B")))
print("Replace Python to Java: " + course.replace("Python", "Java"))
print("Find if word 'Python' is exist in the course string: " + str('Python' in course))
print("The length of the course variable is: " + str(len(course)))



course = '''Hi Gavin

Thank you for your support.
This is multiple line print

'''
print(course)
print("The title of the course variable is: " + course.title())