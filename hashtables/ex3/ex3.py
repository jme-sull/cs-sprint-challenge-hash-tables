def intersection(arrays):
    """
    YOUR CODE HERE
    """
    num_dic = {}
    result = []

    for i in range(len(arrays)):
        for x in arrays[i]:
            if x in num_dic:
                num_dic[x] += 1
            else:
                num_dic[x] = 1
    
    for key, value in num_dic.items():
        if value == len(arrays):
            result.append(key)
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
