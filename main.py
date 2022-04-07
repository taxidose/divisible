# Finde eine 9 stellige Zahl, bestehend aus den Ziffern 1,2,3,4,5,6,7,8,9, welche ersten n-Stellen durch n teilbar sind.
# Zusatzfrage gibt es eine Zweite?
#
# Beispiel für n-Stellen durch n teilbar:     n=3:    234 : 3 = 78 , also teilbar.


from itertools import permutations

numbers_1_to_9 = list(range(1, 10))
magic_number_counter = 0

for permutation in permutations(numbers_1_to_9, len(numbers_1_to_9)):

    number = "".join(str(i) for i in permutation)

    divisible_true_list = [True] + [False] * 8

    for i in range(2, 10):

        if int(number[:i]) % i == 0:
            new_number = number[:i]
            divisible_true_list[i-1] = True

            if False not in divisible_true_list:
                magic_number_counter += 1
                if magic_number_counter == 1:
                    print(f"First number found: {new_number}")
                    print("Checking if second number exists...")
                elif magic_number_counter == 2:
                    print("Second number found o.O")
                    
        else:
            break


if magic_number_counter == 1:
    print("... no :)")
else:
    print("[ERROR] No number or too many numbers found :(")
