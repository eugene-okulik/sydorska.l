num_1, num_2 = 0, 1
num = num_1 + num_2
fibonacci = [0, 1]
while len(fibonacci) < 100001:
    fibonacci.append(num)
    num = fibonacci[-1] + fibonacci[-2]

print(fibonacci[4], fibonacci[199], fibonacci[999], fibonacci[99999])
