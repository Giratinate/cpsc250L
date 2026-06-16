import time

from matplotlib import pyplot as plt


def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        t1 = 0
        t2 = 1
        for i in range(2, n+1):
            t3 = t1 + t2
            t1 = t2
            t2 = t3
        return t3


def time_function(function, n):
    # TODO: write this function - google the python time module to figure out how it works
    # TODO: start a timer, call the appropriate function, then stop the timer
    start = time.perf_counter()
    function(n)
    end = time.perf_counter()
    # TODO: return the elapsed time
    return end - start

def main():
    values = [5, 10, 20, 25, 30, 35, 40]
    rec = []
    ite = []
    print("Fibonacci Timing")
    print("----------------")
    print("n    recursive_time    iterative_time")

    for n in values:
        recursive_time = time_function(fib_recursive, n)
        iterative_time = time_function(fib_iterative, n)
        if iterative_time != 0:
            speed = recursive_time/iterative_time
        else:
            speed = float("inf")
        print(f"{n:<5} {recursive_time:.8f} seconds    {iterative_time:.8f} seconds     {speed:.1f}")
        rec.append(recursive_time)
        ite.append(iterative_time)
    plt.title("Fibonacci Timing")
    plt.ylabel("recursive time (s)")
    plt.xlabel("iterative time (s)")
    plt.plot(values, rec, label="recursive time")
    plt.plot(values, ite, label="iterative time")
    plt.legend()
    plt.yscale("log")
    plt.show()
    # TODO: create a plot which shows both recursive time and iterative time as a function of n
    # TODO: label the x-axis, y-axis, and provide a title
    # TODO: display a legend that will indicate which dataset is which
    # TODO: make the y-axis logarithmic

main()
