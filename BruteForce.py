import random
import time

target_array = list("password")
string_array = [""] * len(target_array)
i = 0
x = 0
while i < len(target_array):
    string_array[i] = chr(random.randint(32,126))
    if string_array[i] == target_array[i]:
        i += 1
    print("".join(string_array))
    time.sleep(.006)
    x += 1
print(x)