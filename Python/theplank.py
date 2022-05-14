# The plank
# Looking at statistics of the problem it would seem there are no time limit exceeded or atleast very few so an
# algorithm doesn't need to be super quick it seems. We can try an exhaustive recursive algoritm.
# The plank cannot be longer than 24 units. We can make an algorithm that always branches in all direction and in
# the final stage puts together solutions that are valid.

def recursive_exhaust(remaining_length):
    # Base Cases:
    if(remaining_length < 0):
        return 0
    elif(remaining_length == 0):
        return 1

    # Recursive Cases, branch in 3 directions:
    one_branch = recursive_exhaust(remaining_length - 1)
    two_branch = recursive_exhaust(remaining_length - 2)
    three_branch = recursive_exhaust(remaining_length - 3)

    return one_branch + two_branch + three_branch

total_length = int(input())
print(recursive_exhaust(total_length))
