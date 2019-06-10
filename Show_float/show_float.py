#!/usr/bin/env python3.7

def format_float(num):
    if '.' in num:
        whole, decimal = num.split('.')
        return ','.join([whole, decimal[:3]])
    else:
        return num

if __name__ == '__main__':
    while True:
        try:
            num = input('give me a float')
            float(num)
        except ValueError:
            print("Value is not a number")
            continue
        output = format_float(num)
        print(output)