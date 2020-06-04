def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    num_arrays = len(arrays)
    cache = {}
    for lst in arrays:
        for elem in lst:
            if elem in cache:
                cache[elem] += 1
            else:
                cache[elem] = 1

    result = []
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
