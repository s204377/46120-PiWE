# Exercise 1:
def greet(name):
    print("Hello, " + name + "!")

greet("world") # "Hello, world!"


# Exercise 2:
def goldilocks(bed_size):
    if bed_size < 140:
        print("Too small!")
    elif bed_size > 150:
        print("Too large!")
    else:
        print("Just right. :)")


# Exercise 3:
def square_list(lst):
    return [x**2 for x in lst]

def square_list2(lst):
    output = [None]*len(lst)
    for i in range(len(lst)):
        output[i] = lst[i]**2
    return output

example_list = [1, 2, 3, 4, 5]

# Exercise 4:
def fibonacci_stop(stop):
    fib = [1, 1]
    while fib[-1] + fib[-2] <= stop:
        fib.append(fib[-1]+fib[-2])
    return fib

# Exercise 5:
def clean_pitch(x,status):
    output = []
    for index, pitch in enumerate(x):
        if status[index] and  (pitch > 90 or pitch < 0): # if status error while pitch not in range
            output.append(-999)
        else:
            output.append(pitch)
    return output

x = [-1, 2, 6, 95]  # "raw" pitch angle at four time steps
status = [1,0,0,0] # status signal

print(clean_pitch(x,status))
