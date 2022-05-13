# Rationale
# If we consider a circle with radius r, the radius will be half the length of the
# square's sides. If we go from the circle's midpoint to the right and to the left
# we can then go up and down to find the corner points, basically using Manhattan
# distance.

cx, cy = list(map(int, input().split()))
r = int(input())

midpoint_right = [cx + r, cy]
midpoint_left = [cx - r, cy]

upper_right = [midpoint_right[0], midpoint_right[1] + r]
lower_right = [midpoint_right[0], midpoint_right[1] - r]
upper_left = [midpoint_left[0], midpoint_left[1] + r]
lower_left = [midpoint_left[0], midpoint_left[1] - r]

print(upper_right[0], upper_right[1])
print(lower_right[0], lower_right[1])
print(lower_left[0], lower_left[1])
print(upper_left[0], upper_right[1])
