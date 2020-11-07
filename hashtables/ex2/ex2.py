#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    ticketsDict = {}

    for ticket in tickets:
        # make the tickets to a dict 
        ticketsDict[ticket.source] = ticket.destination

    # Your code here

    # start the location as none
    location = "NONE"

    route = []
    
    # loop over the length of tickets
    for i in range(length):

        # add route destination with the source
        route.append(ticketsDict[location])

        # update the source
        location = ticketsDict[location]


    return route
