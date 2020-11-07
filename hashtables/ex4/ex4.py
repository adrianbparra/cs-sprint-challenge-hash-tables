def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # make a dictonary with the keys for only negatives
    dictSearch = {v:0 for k,v in enumerate(a) if v < 0}

    pos = [v for v in a if v > 0]
    result = []

    # loop over values 
    for val in pos:
        if -val in dictSearch:
            result.append(val)



    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
