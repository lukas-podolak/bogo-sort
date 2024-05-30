import random
import time
import matplotlib.pyplot as plt

# bogosort

# this function checks whether or not the array is sorted
def is_sorted(random_array):
    for i in range(1, len(random_array)):
        if random_array[i] < random_array[i - 1]:
            return False
    return True

# this function repeatedly shuffles the elements of the array until they are sorted
def bogo_sort(random_array):
    start_time = time.time()
    attempts = 0
    while not is_sorted(random_array):
        random.shuffle(random_array)
        attempts += 1
        elapsed_time = time.time() - start_time
        visualize(random_array, attempts, elapsed_time)
    return random_array

# this function generates an array with randomly chosen integer values
def generate_random_array(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]

# this function visualizes the array
def visualize(array, attempts, elapsed_time):
    plt.clf()
    plt.bar(range(len(array)), array)
    plt.title(f'BogoSort Attempts: {attempts} | Time: {elapsed_time:.2f} seconds')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.pause(0.01)

# the size, minimum value and maximum value of the randomly generated array
size = 100
min_val = 1
max_val = 1000
random_array = generate_random_array(size, min_val, max_val)
print("Unsorted array:", random_array)

# Set up the plot
plt.ion()
fig = plt.figure()

sorted_arr = bogo_sort(random_array)

# End the timer
end_time = time.time()
elapsed_time = end_time - start_time

print("Sorted array:", sorted_arr)
print(f"Time taken to sort: {elapsed_time:.6f} seconds")

# Keep the plot open
plt.ioff()
plt.show()