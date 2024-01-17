def process(data):
    a = []
    b = []
    for num in data:
        str_num = str(num)
        imp = sum(1 for digit in str_num if int(digit) % 2 != 0)
        a.append(imp)
        if imp == 0:
            b.append(num)
    avg = sum(b) // len(b) if b else 0
    a.append(avg)
    return a
