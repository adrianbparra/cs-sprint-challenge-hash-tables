def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # weights is an array

    # length is the length of weights

    # limit is the total limit to get

    # if lenth of one return None
    if length > 1 :
        
        
        weightsDict = {j:i for i,j in enumerate(weights)}
        # loop over weights
        # print(weightsDict)

        for i in range(len(weights)):
            remainder = limit - weights[i]

            if remainder in weightsDict:
                
                index = [i,weightsDict[remainder]]
                index.sort(reverse = True)
                return index
            # print(remainder)

            
        # check if curr index - weight is in the weights dic
            # return the index
    else:
        return None