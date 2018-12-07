# SQL 1:
# SELECT customers.gender, avg(duration) FROM (SELECT caller_id, duration FROM calls UNION SELECT callee_id, duration FROM calls) as call
# JOIN customers ON (call.caller_id = customers.id) GROUP BY gender
# SQL 2:
# O(n*m) where n is the number of records in the parents table and m is the number of
# records in the children table. First it runs through the parents table, finds all the records
# which match the criteria, and then does the same with the children table.
# A count variable should be kept up-to-date while going through the children table.
# Concatenation is a constant time process, so there should be no considerable difference between
# the two queries

def main():
    board = [[1, 5, 7, 10], [3, 13, 14, 15], [6, 16, 19, 25]]
    print(collect_numbers(board))


# Coding problem
def collect_numbers(board):
    sum = 0
    # collect 0,0
    sum += board[0][0]
    # step 1 right
    sum += board[0][1]

    # go all the way down
    y = 1
    while y < len(board):
        sum += board[y][1]
        y += 1

    # go all the way to the right
    x = 2
    y = len(board) - 1
    while x <= len(board):
        sum += board[y][x]
        x += 1

    return sum


# Coding review problem
# in worst case, O(n) runtime
def _find(data, key):
    counter = 0
    for i in data:
        if i == key:
            return counter
            # wrong variable returned, counter may not always be equal to the number we are looking for
            # should return i
        else:
            counter += 1
    return -1
    # should return None, the dataset may contain negative numbers, returning -1 is confusing
    # if the key is not found, it still returns a value that can be a valid result


threshold = 10
# threshold is only used in the second function, should be a local variable there

# with a dataset larger than 10, it has a time complexity of approximately O(log n)
# otherwise O(n), but the effective runtime in this case is marginal
def find(data, key):
    half = len(data) / 2
    # should be wrapped in a int() function, as this division returns float
    # which is not a valid slice index

    data_frst = data[0:half]  # typo
    data_second = data[half:]

    if len(data) <= threshold:
        return find(data, key)
        # wrong function called, always ends up in a recursion error, should call
        # _find(data,key)
    elif key < data[half]:
        return find(data_first, key)
        # error because of the type above
    else:
        return find(data_second, key)


if __name__ == "__main__":
    main()

