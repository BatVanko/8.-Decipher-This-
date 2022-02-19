input_line = input().split(" ")

for word in input_line:
    first_part = []
    second_part = []
    for l in word:
        if l.isdigit():
            first_part.append(l)
        else:
            second_part.append(l)
    first_part = chr(int("".join(first_part)))
    swap = second_part[0]
    second_part[0] = second_part[-1]
    second_part[-1] = swap
    second_part = "".join(second_part)

    print(first_part + second_part, end=" ")
