"""Given a positive integer as input, return the output as a string in the following format:

Each digit (from left to right) multiplied by the corresponding power of 10, so that the sum equals the input number.

If the digit is zero, exclude it from the output;
For the last digit, just use the digit itself, without *1.
Examples
0     -->  ""
56    -->  "5*10+6"
60    -->  "6*10"
999   -->  "9*100+9*10+9"
10004 -->  "1*10000+4" 
"""


def simplify(number): 
    num = number
    string_num = str(num)
    list_1 = [int(d) for d in string_num]
    first_digit = list_1[0]
    if first_digit == 0:
        return ''
    if len(list_1) == 1:
        return f'{first_digit}'
    string_1 = f"{first_digit}*{10**(len(list_1)-1)}"
    for i in range(1, len(list_1)):
        digit = list_1[i]
        if digit == 0:
            pass
        else:
            multiplier = 10**(len(list_1)-1-i)
            if multiplier == 1:
                str_mult = ''
            else:
                str_mult = f'*{multiplier}'
            string_1 += f"+{digit}{str_mult}"  
    return string_1