def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    num_arrays = len(arrays)  # get the array length
    cache = {}
    for lst in arrays:  # for each list in the arrays
        for elem in lst:  # for each element in list
            if elem in cache:
                cache[elem] += 1  # increase count if it exists
            else:
                cache[elem] = 1  # add to cache if it doesn't exist

    result = []
    # if the value for a key equals number of arrays, it is in all of them
    for key in cache:
        if cache[key] == num_arrays:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
