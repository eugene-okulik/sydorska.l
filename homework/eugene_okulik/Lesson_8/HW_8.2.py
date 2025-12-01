def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b


gen = fibonacci()
counter = 0
position = [4, 199, 999, 99999]
for num in gen:
    if counter in position:
       print(num)

    if counter == max(position):
        break

    counter += 1
