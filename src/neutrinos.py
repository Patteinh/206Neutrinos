import math

def update_stats(n, a, h, sd, new_value):
    n += 1
    a_new = a + (new_value - a) / n
    sd_new = math.sqrt(((n - 1) * sd ** 2 + (new_value - a) * (new_value - a_new)) / n)
    h_new = n / ((n - 1) / h + 1 / new_value)
    rms_squared = ((n - 1) * (a ** 2 + sd ** 2) + new_value ** 2) / n
    rms_new = math.sqrt(rms_squared)
    return n, a_new, h_new, sd_new, rms_new

def neutrinos(args):
    n = int(args[1])
    a = float(args[2])
    h = float(args[3])
    sd = float(args[4])
    while True:
        next_value = input("Enter next value: ")
        if next_value == "END":
            break
        next_value = float(next_value)
        n, a, h, sd, rms = update_stats(n, a, h, sd, next_value)
        print(f"\tNumber of values: {n}")
        print(f"\tStandard deviation: {sd:.2f}")
        print(f"\tArithmetic mean: {a:.2f}")
        print(f"\tRoot mean square: {rms:.2f}")
        print(f"\tHarmonic mean: {h:.2f}\n")
