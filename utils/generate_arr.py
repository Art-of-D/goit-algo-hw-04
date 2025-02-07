import random

def generate_array(length=100, min_value=0, max_value=1000000):
  return [random.randint(min_value, max_value) for _ in range(length)]