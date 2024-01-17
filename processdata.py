def process(data):
    odd_counts = []
    no_odd_nums = []
    for num in data:
        str_num = str(num)
        odd_count = sum(1 for digit in str_num if int(digit) % 2 != 0)
        odd_counts.append(odd_count)
        if odd_count == 0:
            no_odd_nums.append(num)
    avg = sum(no_odd_nums) // len(no_odd_nums) if no_odd_nums else 0
    odd_counts.append(avg)
    return odd_counts
