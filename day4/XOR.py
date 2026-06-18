def get_prefix_xor(x):
    remainder = x % 4
    if remainder == 0:
        return x
    elif remainder == 1:
        return 1
    elif remainder == 2:
        return x + 1
    else:  # remainder == 3
        return 0
s, e = map(int, input().split())

val = get_prefix_xor(e) ^ get_prefix_xor(s - 1)

print(val)
