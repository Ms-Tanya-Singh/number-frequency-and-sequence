lst = input("Take a list of integers: ")
lst = lst.replace('[', '').replace(']', '').replace(',', '')
lst = lst.split()

if not lst:
    print("The list is empty.")
    exit()

try:
    lst = [int(num) for num in lst]
except ValueError:
    print("Please enter only integers.")
    exit()

# Most frequent number
freqdct = {}
for num in lst:
    if num in freqdct:
        freqdct[num] += 1
    else:
        freqdct[num] = 1

freqnum = next(iter(freqdct))
for num in freqdct:
    if freqdct[num] > freqdct[freqnum]:
        freqnum = num
    elif freqdct[num] == freqdct[freqnum] and num < freqnum:
        freqnum = num

# Longest same-number sequence
max_len = 1
current_len = 1
streak_num = lst[0]

for i in range(1, len(lst)):
    if lst[i] == lst[i - 1]:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
            streak_num = lst[i]
    else:
        current_len = 1

print(f"The smallest frequently occurring number is {freqnum} and its frequency is {freqdct[freqnum]}")
print(f"The longest same-number sequence is of number {streak_num} and its length is {max_len}")
