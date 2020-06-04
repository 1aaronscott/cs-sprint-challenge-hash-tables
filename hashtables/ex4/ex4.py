def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    b = [0]*len(a)
    cache = dict(zip(a, b))
    result = []
    for k in cache:
        if k > 0:
            #            print(k)
            try:
                if cache[k] is not None and cache[-k] is not None:
                    result.append(k)
            except:
                pass

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
