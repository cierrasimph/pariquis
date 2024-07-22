def my_generator():
    yield [12, 15, 0.002746942550584391]

# Create an iterator from the generator function
my_iterator = my_generator()

# Iterate over the values produced by the iterator
for value in my_iterator:
    print(value)
