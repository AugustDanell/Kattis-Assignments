while True:
    instructions = int (input())
    if(instructions == 0):
        break

    else:
        bit_string = list("?"*32)
        offset = 31

        for i in range(instructions):
           # print("".join(bit_string))
            instruction = input().split()
            if(instruction[0] == "SET"):
                bit_string[offset-int(instruction[1])] = "1"

            elif(instruction[0] == "CLEAR"):
                bit_string[offset - int(instruction[1])] = "0"

            # Or case:
            elif(instruction[0] == "OR"):
                a_bit = offset - int(instruction[1])
                b_bit = offset - int(instruction[2])
                a = bit_string[a_bit]
                b = bit_string[b_bit]

                if(a == "1" or b == "1"):
                    bit_string[a_bit] = "1"

                elif(a == "0" and b == "0"):
                    bit_string[a_bit] = "0"
                else:
                    bit_string[a_bit] = "?"

            elif(instruction[0] == "AND"):
                a_bit = offset - int(instruction[1])
                b_bit = offset - int(instruction[2])
                a = bit_string[a_bit]
                b = bit_string[b_bit]

                if(a == "1" and b == "1"):
                    bit_string[a_bit] = "1"
                elif(a == "0" or b == "0"):
                    bit_string[a_bit] = "0"
                else:
                    bit_string[a_bit] = "?"

        print("".join(bit_string))
