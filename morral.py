
# Recursive function
def bag(size, weight, values, n):
    #There are no more elements or the bag is full
    if n == 0 or size == 0:
        return 0
    print('check if the bag has space')
    print(n, size)

    # n -1 allows me to check the next value recursively
    if weight[n - 1] > size:
        return bag(size, weight, values, n - 1)
    print('')
    print('Check if the bag size is less than the weight')
    print(size, weight, values, n - 1)

    print('')
    print('The max value that the bag can handle')
    return max(values[n - 1] + bag(size - weight[n - 1], weight, values, n - 1), bag(size, weight, values, n - 1))


# Entry point 
if __name__ == '__main__':
    values = [60, 100, 120]
    weight = [10, 20, 30]
    size = 60
    n = len(values)

    result = bag(size, weight, values, n)
    print(result)