N = int(input())
ratings = list(map(int, input().split()))
normal_colors = set()
free_color_users = 0
for r in ratings:
    if 1 <= r <= 399:
        normal_colors.add("gray")
    elif 400 <= r <= 799:
        normal_colors.add("brown")
    elif 800 <= r <= 1199:
        normal_colors.add("green")
    elif 1200 <= r <= 1599:
        normal_colors.add("cyan")
    elif 1600 <= r <= 1999:
        normal_colors.add("blue")
    elif 2000 <= r <= 2399:
        normal_colors.add("yellow")
    elif 2400 <= r <= 2799:
        normal_colors.add("orange")
    elif 2800 <= r <= 3199:
        normal_colors.add("red")
    else:
        free_color_users += 1
fixed_count = len(normal_colors)
if fixed_count == 0 and free > 0:
    min_ans = 1
else:
    min_ans = fixed_count
max_ans = fixed_count + free
print(min_ans, max_ans)
