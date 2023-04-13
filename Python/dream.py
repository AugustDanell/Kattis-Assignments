# A solution to the problem: https://open.kattis.com/problems/dream

'''
General Solution - A Stack with two Counters:
When we process scenarios we save the events into a stack as potential dreams. There are two non-trivial cases. The first is when we say that a scenario contains an
event E and E has happened. In that case we need the events leading up to E to have happened so we save a counter growing in that direction. Another non-trivial scenario
is when an Event E is said not to have happened, but it has happened. In that case we have to negate it by finding it in the stack. This counter grows in the other 
direction, telling us how many dreams we have to pop from the stack. If the two counters go past each other the solution is inconsistent, as this tells us that we need
some dreams but they also need to be popped from the stack.
'''


if __name__ == "__main__":
  
    # 1. Initiate datastructures and take in input:
    n = int(input())
    stack = []
    event_map = {}
    stack_index = {}
    
    # 2. Iterate over n commands. Depending on the command execute different actions:
    for _ in range(n):
        data = input().split()
        
        # 3. If the command is an Event, add the event, index it in the stack, and set it as True:
        if data[0] == "E":
            stack_index[data[1]] = len(stack)
            stack.append(data[1])
            event_map[data[1]] = True
        
        # 4. If the command is a dream, pop events from the stack and mark them as undone:
        elif data[0] == "D":
            dreams_to_undo = int(data[1])
            for i in range(dreams_to_undo):
                event_map[stack.pop()] = False

        # 5. Process the events of a scenario:
        elif data[0] == "S":
            
            # A): Initiate counters and assume that the scenario is consistent:
            m = int(data[1])
            remove_dreams = 0
            goodScenario = True
            need_dreams = -1
            
            # B) Iterate over each event in the scenario:
            for i in range(m):
                event = data[2+i]

                # C) If the input suggests so, negate the current event:
                negated = event[0] == "!"
                if negated:
                    event = event[1:]

                # D) Handling the event where E is asked and it can be found to have happened:
                if not negated and event in event_map and event_map[event]:
                    need_dreams = max(1+stack_index[event], need_dreams)
                    
                    # D1: We have a counter called need dreams. If an event is said to be happened we need i..need_dreams to have happened:
                    if need_dreams > len(stack) - remove_dreams:
                        goodScenario = False
                        break
                    else:
                        continue

                # E) Handling the trivial ok event where !E is asked and E has not happened:
                elif negated and (not (event in event_map) or not event_map[event]):
                    continue


                # F) Handling the inconsistent event where E is asked but E is not found:
                elif not negated and (not (event in event_map) or not event_map[event]):
                    goodScenario = False
                    break

                # G) Handling the event where !E is asked but E is found and has to be dreamt away. This event works the other way in the stack:
                elif negated and (event in event_map and event_map[event]):
                    index = 0
                    local_counter = len(stack) - stack_index[event]
                    remove_dreams = max(remove_dreams, local_counter)

                    if need_dreams > len(stack) - remove_dreams and not need_dreams == -1:
                        goodScenario = False
                        break

            # All necessary events are processed, output the scenario:
            if goodScenario and remove_dreams == 0:
                print("Yes")
            elif not goodScenario:
                print("Plot Error")
            else:
                print(remove_dreams, "Just A Dream")
