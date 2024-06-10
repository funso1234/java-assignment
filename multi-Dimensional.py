outer_list = []

for a in range(4):
    inner_list = []
    for b in range(5):
        inner_list.append(a * b)
    outer_list.append(inner_list)
    print(inner_list)

    for r in range(4):
        for t in range(5):
            print(outer_list[r][t], end='  ')
        print()

    Ist = ["shakira", 0, True, 0]
    Ist.insert()