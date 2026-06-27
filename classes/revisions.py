def is_prime(n: int) -> bool:
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def traverse_list(items: list) -> None:
    """Traverse a list and print each element with its index."""
    for index, value in enumerate(items):
        print(f"Index {index}: {value}")


def check_number(n: int) -> str:
    """Use if-else to determine whether a number is positive, negative, or zero."""
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"


def sum_numbers(n: int) -> int:
    """Use a for loop to compute the sum of numbers from 1 to n."""
    total = 0
    for value in range(1, n + 1):
        total += value
    return total


def find_max_in_list(numbers: list) -> int | None:
    """Find the maximum value in a list using simple comparisons."""
    if not numbers:
        return None
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum


print("Prime check for 17:", is_prime(17))
print("Prime check for 18:", is_prime(18))

sample_list = [5, 12, 7, 3]
print("Traversing sample list:")
traverse_list(sample_list)

print("Check number 10:", check_number(10))
print("Check number -5:", check_number(-5))
print("Check number 0:", check_number(0))

print("Sum from 1 to 5:", sum_numbers(5))

print("Max in sample list:", find_max_in_list(sample_list))
