def solution(S):
    array_length = len(S)
    buffer_jump_distance = 0
    for index in range(array_length):
        print("index:", index)
        jump_counter = 1
        for left_iteration in range(index, 0, -1):
            print("left_iteration:", left_iteration)
            if S[left_iteration-1] < S[left_iteration]:
                break
            else:
                jump_counter += 1

        for right_iteration in range(index, array_length-1):
            if S[right_iteration+1] < S[right_iteration]:
                break
            else:
                jump_counter += 1

        buffer_jump_distance = max(jump_counter, buffer_jump_distance)

    return buffer_jump_distance

# print(solution([2, 6, 8, 5]))
# print(solution([1, 5, 5, 2, 6]))
print(solution([1, 1]))