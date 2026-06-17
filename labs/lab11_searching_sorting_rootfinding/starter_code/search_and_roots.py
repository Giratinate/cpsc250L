def linear_search(values, target):
    comparisons = 0
    for i in values:
        if i == target:
            comparisons += 1
            return values.index(i), comparisons
        else:
            comparisons += 1


def binary_search(values, target, counter, computations):
    answer = 0
    if target == values[len(values)//2]:
        computations += 1
        answer = len(values)//2 + counter
    elif target < values[len(values)//2]:
        computations += 1
        answer, computations = binary_search(values[0:len(values)//2], target, counter, computations)
    elif target > values[len(values)//2]:
        computations += 1
        counter += len(values)//2
        answer, computations = binary_search(values[len(values)//2:], target, counter, computations)
    return answer, computations


def f(x):
    return x * x - 2


def bisection_root(function, left, right, tolerance):
    if abs(right - left) < tolerance:
        return left
    else:
        middle = (left + right) / 2
        if function(middle) * function(left) < 0:
            return bisection_root(f, left, middle, tolerance)
        else:
            return bisection_root(f, middle, right, tolerance)


def main():
    import random
    values = random.sample(range(0, 1000), 500)
    values.sort()

    # Find the 500th value in the list
    search_value = values[249]

    print("Search Tests")
    print("------------")
    print("Linear search for ", search_value," --> (index,comps) = ", linear_search(values, search_value))
    print("Binary search for ", search_value," --> (index,comps) = ", binary_search(values, search_value, 0, 0))

    print()
    print("Root Finding")
    print("------------")
    root = bisection_root(f, 1, 2, 0.0001)
    print("Approximate root of x^2 - 2:", root)

main()
