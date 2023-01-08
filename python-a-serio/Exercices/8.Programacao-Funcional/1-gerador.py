def my_generator():
    yield 1
    yield 2
    yield 'a'

generator = my_generator()

# Restrict memory for use 128MB

# ulimit -v 131072

# Teste one

a = list(range(10000000))

# Teste two

for value in range(10000000):
    if value == 50000:
        print('Found it')
        break