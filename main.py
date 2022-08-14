from collections import Counter as counter


def solution(A):
    final_list = []
    adition_list = []
    for data in A:
        str_num = str(data)

        addition_val = 0
        for i in range(len(str_num)):
            addition_val += int(str_num[i])
        adition_list.append(addition_val)
    count_dict = counter(adition_list)

    for key in count_dict:
        not_avail_flag = False
        if count_dict[key] > 1:
            index = [i for i, e in enumerate(adition_list) if e == key]
            ret_list = []
            for val in index:
                ret_list.append(A[val])
            final_list.append(tuple(ret_list))
        else:
            not_avail_flag = True

    if not_avail_flag:
        return -1
    else:
        return tuple(final_list)


print(method([51, 17, 42, 62]))

