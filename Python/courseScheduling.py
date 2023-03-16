# Solution to the problem: https://open.kattis.com/problems/coursescheduling

# Made into a function so as to avoid code duplication. Simply adds a course to the map:
def addCourse(course, courseMap):
    if courseMap.__contains__(course):
        courseMap[course] += 1
    else:
        courseMap[course] = 1

# A) Input:
students = int(input())
courseMapping = {}
courseCounter = {}

# B) Write some code that enrolls students to courses:
for i in range(students):
    data = input().split()
    course = data[-1]
    student = data[0] + " " + data[1]

    # Add a course if a student is not enrolled in it:
    if not courseMapping.__contains__(student):
        courseMapping[student] = {course : True}
        addCourse(course, courseCounter)
    elif not courseMapping[student].__contains__(course):
        courseMapping[student][course] = True
        addCourse(course, courseCounter)

# C) Sort the courses based lexiographic order, no specification needed really:
courses = list(courseCounter.keys())
sortedCourses = list(sorted(courses))
for course in sortedCourses:
    print(course, courseCounter[course])
