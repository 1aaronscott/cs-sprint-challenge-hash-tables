def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    # make the keys the weights and the values the indices
    for i in range(len(weights)):
        cache[weights[i]] = i
#    print(cache)
    # for each weight find the difference and if it matches, return the indices
    for i in range(len(weights)):
        lw = limit-weights[i]
        if lw in cache:
            return (max(i, cache[lw]), min(i, cache[lw]))
    return None


if __name__ == "__main__":
    weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    print(get_indices_of_item_weights(weights_4, 9, 7))
