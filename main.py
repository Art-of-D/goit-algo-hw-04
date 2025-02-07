import shlex
from decorators.error_handler import input_error
from timeit import timeit
import time
from utils.generate_arr import generate_array
from utils.sorting import merge_sort, insertion_sort, timsort

def parse_input(user_input):
    """
    Parse the user's input into a command and arguments.

    Args:
        user_input (str): The user's input.

    Returns:
        tuple: A tuple of the command and arguments. If the user entered no command, returns ("commands", []).
    """
    if not user_input:
        print("Please enter a command.")
        return "commands", []

    try:
        tokens = shlex.split(user_input)
        cmd = tokens[0].strip().lower() if tokens else "commands"
        args = tokens[1:] if len(tokens) > 1 else []
        return cmd, args
    except ValueError as e:
        print(f"Error parsing input: {e}")
        return "commands", []

@input_error
def input_generator():
    inp = input("Please enter three numbers separated by spaces: length, min_value, max_value to generate an array.\n")
    cmd, args = parse_input(inp)
    try:
        a = int(cmd)
        b = int(args[0])
        c = int(args[1])
    except ValueError:
        raise ValueError("Invalid input. Please enter three numbers.")
    return generate_array(a, b, c)
@input_error
def manual_array():
    inp = input("Please enter an array of numbers separated by spaces.\n")
    try:
        m_arr = list(map(int, inp.split()))
        for i in range(len(m_arr)):
            m_arr[i] = int(m_arr[i])
    except ValueError:
        raise ValueError("Invalid input. Please enter an array of numbers.")
    
    return m_arr

def main():
    arr = []
    print("Welcome to the D&A bot!")
    print("Available commands: hello, copy, ms, is, ts, manual-gen, regen, help, commands, close OR exit")
    arr = input_generator()
    while True:

        while not arr:
            arr = input_generator()

        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        if command in ["ms", "1"]:
            execution_time = timeit(lambda: merge_sort(arr), number=1)
            print(f"Merge Sort executed in {execution_time:.6f} seconds")
        elif command in ["is", "2"]:
            execution_time = timeit(lambda: insertion_sort(arr), number=1)
            print(f"Insertion Sort executed in {execution_time:.6f} seconds")
        elif command in ["ts", "3"]:
            execution_time = timeit(lambda: timsort(arr), number=1)
            print(f"Tim Sort executed in {execution_time:.6f} seconds")
        elif command in ["diff", "4"]:
            print(f"Merge Sort: {timeit(lambda: merge_sort(arr), number=1):.6f} sec")
            print(f"Insertion Sort: {timeit(lambda: insertion_sort(arr), number=1):.6f} sec")
            print(f"Tim Sort: {timeit(lambda: timsort(arr), number=1):.6f} sec")
        elif command in ["manual-gen", "88"]:
            arr = manual_array()
            print("Your array:\n", arr)
        elif command in ["regen", "99"]:
            arr = input_generator()
            print("Generated array:\n", arr)
        elif command in ["commands", "help", "command", "0"]:
            print("Available commands: hello, copy, ms, is, ts, manual-gen, regen, help, commands, close OR exit")
        else:
            print("Invalid command. If you need help, type 'commands'.")

if __name__ == "__main__":
    main()