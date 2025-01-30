def print_sequence(n):
    if n == 1:
        print(f'The current value in the sequence is {n}! End of sequence')
        return

    print(f'The current value in the sequence is {n}')

    if n % 2 == 0:
        print_sequence(n / 2)
    else:
        print_sequence(3 * n + 1)

def recursive_double_list(input_list, new_list):
    if len(input_list) == 0:
        return new_list

    first_item = input_list[0]
    new_list.append(first_item * 2)
    left_over_list = input_list[1:]
    return recursive_double_list(left_over_list, new_list)
