def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create empty list and join with "a" to make a dict
    b = [0]*len(a)
    cache = dict(zip(a, b))
    result = []
    for k in cache:
        if k > 0:  # for every positive key
            #            print(k)
            try:  # check to see if it's negative also exists
                if cache[k] is not None and cache[-k] is not None:
                    result.append(k)
            except:
                pass

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
