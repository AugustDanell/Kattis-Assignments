# A solution to the problem: https://open.kattis.com/problems/calculator

import sys
def parse_numbers(tokens):
    digit_list = []
    index = 0
    while index < len(tokens):
        if tokens[index] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            digit = tokens.pop(index)
            digit_list.append(digit)
        else:
            if not digit_list == []:
                tokens.insert(index, float("".join(digit_list)))
                digit_list = []
            index += 1

    if not digit_list == []:
        tokens.append(float("".join(digit_list)))

    return tokens
def find_max_depth(tokens):
    depth = 0
    max_depth = 0
    for token in tokens:
        if token == "(":
            depth += 1
            if depth > max_depth:
                max_depth = depth
        elif token == ")":
            depth -= 1
    return max_depth
def remove_empty_groups_and_whitespaces(tokens):
    index = 0
    while index < len(tokens)-1:
        current = tokens[index]
        next = tokens[index+1]
        if current == "(" and next == ")":
            tokens.pop(index)
            tokens.pop(index)
            index -= 1
        elif current == " " or current == "\n":
            tokens.pop(index)
        else:
            index += 1
def remove_encasing_parenthesis(tokens):
    index = 1
    while index < len(tokens) -1:
        prev = tokens[index -1]
        current = tokens[index]
        next = tokens[index +1]
        if prev == "(" and next == ")" and type(current) is float:
            tokens.pop(index-1)
            tokens.pop(index)
            index -= 1
        else:
            index += 1
    return tokens
def evaluate_group(tokens):
    index = 1
    while index < len(tokens)-1:
        if tokens[index] == "*":
            negation_coeff = False
            while tokens[index+1] == "-":
                negation_coeff = not negation_coeff
                tokens.pop(index+1)

            factor = tokens[index-1]*tokens[index+1]
            if negation_coeff:
                factor = -factor

            tokens[index-1] = factor
            tokens.pop(index)
            tokens.pop(index)
        elif tokens[index] == "/":
            negative_coeff = False
            while tokens[index + 1] == "-":
                negative_coeff = not negative_coeff
                tokens.pop(index + 1)
            quotient = tokens[index-1]/tokens[index+1]
            tokens[index-1] = quotient
            if negative_coeff:
                tokens[index-1] = -quotient

            tokens.pop(index)
            tokens.pop(index)
        else:
            index += 1

    negation_flag = False
    s = 0
    for token in tokens:
        if token == "-":
            negation_flag = not negation_flag
        elif type(token) == float:
            if negation_flag:
                s -= token
                negation_flag = False
            else:
                s+= token
    return s

def replace_paranthesis_of_specific_depth(remove_depth, tokens):
    depth = 0
    index = 0
    l = []
    while index < len(tokens):
        if tokens[index] == "(":
            depth += 1
            index += 1

        elif depth == remove_depth:
            if tokens[index] == ")":
                tokens.insert(index, evaluate_group(l))
                l = []
                index += 1
                depth -= 1
            else:
                l.append(tokens.pop(index))

        elif tokens[index] == ")":
            depth-=1
            index += 1
        else:
            index += 1
    return tokens

def run_tests():
    assert (parse_numbers(list("100+200+300"))) == [100, "+", 200, "+", 300]
    assert (remove_encasing_parenthesis(["(", "(", 100.0, ")", ")"])) == [100.0]
    assert (evaluate_group([1.0, "*", 2.0, "*", 3.0])) == 6.0
    assert (evaluate_group([1.0, "+", 2.0, "+", 3.0])) == 6.0
    assert (evaluate_group(["-", 1.0])) == -1.0
    assert (evaluate_group(["-", "-", 1.0])) == 1.0
    assert (evaluate_group(["-", 1.0, "*", 5.0, "+", 2.0])) == -3.0
    l = (replace_paranthesis_of_specific_depth(3, ["(", "(", "(", 10.0, "+", 20.0, ")", ")", ")"]))
    assert remove_encasing_parenthesis(l) == [30.0]

def evaluate_entire_expr(s):
    tokens = list(s)
    remove_empty_groups_and_whitespaces(tokens)
    tokens = parse_numbers(tokens)
    while True:
        max_depth = find_max_depth(tokens)
        #print(max_depth, len(tokens), tokens)

        if max_depth == 0:
            break
        replace_paranthesis_of_specific_depth(max_depth, tokens)
        remove_encasing_parenthesis(tokens)

    return evaluate_group(tokens)

for line in sys.stdin:
    print("{:.2f}".format(evaluate_entire_expr(line)))
