s1 = "Hana98Hajari98!"

total_sum = 0
count = 0

for character in s1:
    if character.isdigit():
        total_sum += int(character)
        count += 1