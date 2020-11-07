def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    first = arrays[:1]
    last = arrays[1:]

    # create dict of values in last array into 

    for i in range(len(last)):
        # print(last[i])

        last[i] = {v:0 for k,v in enumerate(last[i])}

    # join list with values as keys and add 

    # loop over val in first array

    # check each dict to see if value exist
    result = []

    for val in first:

        time_found = 0

        for term in last:

            if val in term:
                
                time_found += 1
        

        if time_found >= len(last) - 1:

            result.append(val)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
