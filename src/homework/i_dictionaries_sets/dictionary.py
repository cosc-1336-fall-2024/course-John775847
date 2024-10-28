
def get_p_distance(list1, list2):
    p_distance = 0

    if (len(list1) == len(list2)):
        for i in range(len(list1)):
            if (list1[i] != list2[i]):
                p_distance += 1 # Cannot use 0.1 because if you add it together 3 times you get 0.30000000000000004
    else:
        print("DNA does not match")
        return "Error"

    p_distance = p_distance / 10 # p_distance * 0.1 will also cause the above error

    return p_distance

def get_p_distance_matrix(list1):
    out_matrix = []

    for index1 in range(len(list1)):
        temp_list = []
        for index2 in range(len(list1)):
            temp_list.append(float(get_p_distance(list1[index1], list1[index2])))
        out_matrix.append(temp_list)

    return out_matrix
