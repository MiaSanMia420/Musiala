def read(filename):
    results = []
    with open(filename, 'r') as file:
        for line in file:
            nums = list(map(int, line.split()))
            result = process(nums)
            results.append(result)
    return results
