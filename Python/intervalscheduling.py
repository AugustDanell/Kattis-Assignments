if __name__ == "__main__":
    courses = int(input())
    course_list = []
    for _ in range(courses):
        course_list.append(list(map(int,input().split())))

    course_list = sorted(course_list, key = lambda x: x[1])
    time = 0
    possible_courses = 0
    for course in course_list:
        if time <= course[0]:
            possible_courses += 1
            time = course[1]
            
    print(possible_courses)
