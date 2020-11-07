# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = set()

    for query in queries:


        for f in files:

            if query in f:

                result.add(query)


    result = list(result)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
