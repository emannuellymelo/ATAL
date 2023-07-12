def stop_position(d, i):
    final_node = 1    
    for _ in range(1, d):
        if (i % 2 != 0):
            final_node *= 2
            i = (i + 1) // 2
        else:
            final_node = final_node * 2 + 1
            i = i//2
    return final_node

while(True):
    lines = int(input())
    if(lines < 0): break
    for p in range(lines):
        test_case = input().split(" ")
        d = int(test_case[0])
        i = int(test_case[1])
        print(stop_position(d,i))