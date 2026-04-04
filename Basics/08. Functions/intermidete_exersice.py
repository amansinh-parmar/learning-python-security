# ==> Exersice 1: Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
import math
from collections import Counter

def calculate_mean(data):
    if len(data) == 0:
        return None
    return sum(data) / len(data)


def calculate_median(data):
    if len(data) == 0:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def calculated_mode(data):
    if len(data) == 0:
        return None
    counts = Counter(data)
    max_freq = max(counts.values())
    modes = [key for key, val in counts.items() if val == max_freq]
    return modes        # can return multiple modes

def calculate_range(data):
    if len(data)== 0:
        return None
    return max(data) - min(data)

def calculate_variance(data):
    if len(data) == 0:
        return None
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_std(data):
    variance = calculate_variance(data)
    if variance is None:
        return None
    return math.sqrt(variance)

nums = [1,2,2,3,4,5]

print("Mean: ", calculate_mean(nums))
print("Median: ", calculate_median(nums))
print("Mode: ", calculated_mode(nums))
print("Range: ", calculate_range(nums))
print("Variance: ", calculate_variance(nums))
print("Standard Deviation: ", calculate_std(nums))


# ==> Exersice 2: Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
        
    return True

print(is_prime(5))
print(is_prime(9))
print(is_prime(4), '\n')

# ==> Exersice 3: Write a functions which checks if all items are unique in the list.
def all_unique(lst):
    seen = []
    for item in lst:
        if item in seen:
            return False
        seen.append(item)
    return True

print(all_unique([1, 2, 3, 4, 4]))     # True
print(all_unique([1, 2, 22, 37,95 ]), '\n')  # False

# ==> Exersice 4: Write a function which checks if all the items of the list are of the same data type.
def same_type(lst):
    if len(lst) == 0:
        return True
    
    first_type = type(lst[0])

    for item in lst:
        if type(item) != first_type:
            return 'Oops, something went wrong data-types are not matched'

    return 'All items data-types are same.'

print(f'Same Data Type: {same_type([1,2,4])}')   # True
print(f'Non-same Data Type: {same_type([1,'2',4])}', '\n') # False

# ==> Exersice 5: Write a function which check if provided variable is a valid python variable
import keyword

def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)

print('\n',is_valid_variable("x"))        # True
print(is_valid_variable("my_var"))   # True
print(is_valid_variable("2var"))     # False
print(is_valid_variable("for"), '\n')      # False (keyword)

# ==> Exersice 6: Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
from countries_data import countries
def most_spoken_languages(countries, top=10):
    language_count = {}

    for country in countries:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:  
                language_count[language] = 1

    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_languages[:top]

# print(most_spoken_languages(countries, 10), '\n')
# print(most_spoken_languages(countries, 20))

# ==> Exersice 7: Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
from countries_data import countries

def most_populated_countries(countries, top=10):
    """
    Returns the `top` most populated countries in descending order.
    """
    # Sort countries by population in descending order
    sorted_countries = sorted(countries, key=lambda c: c['population'], reverse=True)

    # Return a list of tuples (country_name, population)
    return [(country['name'], country['population']) for country in sorted_countries[:top]]


# Example usage:
print(f'Top 10: {most_populated_countries(countries, 10)}', '\n')      # Top 10
print(f'Top 20: {most_populated_countries(countries, 20)}', '\n')      # Top 20