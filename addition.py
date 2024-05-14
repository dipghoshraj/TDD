
import re

def add(numbers):
    if not numbers:
        return 0
    

    delimiter = ','
    if numbers.startswith("//"):
        delimiter, numbers = re.match(r"//(.*)\n(.*)", numbers).groups()
    
    numbers = re.split(rf"{delimiter}|\n", numbers)
    negatives = [int(num) for num in numbers if int(num) < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")
    
    return sum(int(num) for num in numbers if int(num) <= 1000)