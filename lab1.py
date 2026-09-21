#1 (ā ∨ b)(b̄ ∨ c)∧ a ∧ c̄;

arr = [
    [1, 1, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0],
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, 0]
]
# print("Task 1:\n")
# print("(ā ∨ b)(b̄ ∨ c)∧ a ∧ c̄\n")
# print("  |-ā-|  |-b̄-| ")
# print("--|   |--|   |--a--c̄--")
# print("  |-b-|  |-c-|\n ")
# print("| a | b | c | ā | b̄ | c̄ | (ā ∨ b) | (b̄ ∨ c) | a ∧ c̄ | F |")

# for i in arr:
#     a = i[0]
#     b = i[1]
#     c = i[2]
#     not_a = not a
#     not_b = not b
#     not_c = not c
#     not_a_or_b = not_a or b
#     not_b_or_c = not_b or c
#     a_and_not_c = a and not_c
#     f = not_a_or_b and not_b_or_c and a_and_not_c
#     print(
#             f"| {a:^1} | {b:^1} | {c:^1} | "
#             f"{int(not_a):^1} | {int(not_b):^1} | {int(not_c):^1} | "
#             f"{int(not_a_or_b):^7} | {int(not_b_or_c):^7} | "
#             f"{int(a_and_not_c):^5} | {int(f):^1} |"
#         )

# print("Формула є суперечністю")



# print("\n\nTask 2:\n")

# arrF = []
# for i in range(8):
#     arrF.append(int(input(f"F для рядка {arr[i]}: ")))

# ddnf_terms = []
# dknf_terms = []

# for (val_a, val_b, val_c), f in zip(arr, arrF):
#     if f == 1:
#         a = "a" if val_a == 1 else "ā"
#         b = "b" if val_b == 1 else "b̄"
#         c = "c" if val_c == 1 else "c̄"
#         ddnf_terms.append(f"({a} ∧ {b} ∧ {c})")
#     else:
#         a = "a" if val_a == 0 else "ā"
#         b = "b" if val_b == 0 else "b̄"
#         c = "c" if val_c == 0 else "c̄"
#         dknf_terms.append(f"({a} ∨ {b} ∨ {c})")

# print("\nДДНФ:")
# print(" ∨ ".join(ddnf_terms) if ddnf_terms else "Не існує (усі F = 0)")

# print("\nДКНФ:")
# print(" ∧ ".join(dknf_terms) if dknf_terms else "Не існує (усі F = 1)")

# print("\n\nTask 3:\n")
#(ā + b)(a+bc)(ā +c)+c̄

text = "(ā+b)*(a+(b*c))*(ā+c)+c̄"
print(f"{text}\n")
text = text.replace("+", " ∨ ").replace("*", " ∧ ")
print(f"Формула алгебраїчних висловлень: {text}\n\n")


print("      |---- ā ----|   |--------- a ---------|   |---- ā ----|"           )
print("      |           |   |                     |   |           |"           )
print("  |---|           |---|                     |---|           |------|"    )
print("  |   |---- b ----|   |----- b ------- c ---|   |---- c ----|      |"    )
print("--|                                                                |--"  )
print("  |                                                                |"    )
print("  |------------------------------ c̄ -------------------------------|\n\n")

print("| a | b | c | ā | b̄ | c̄ | (ā ∨ b) | (b ∧ c) | (a ∨ (b ∧ c) ) | (ā ∨ c) | F |")
for i in arr:
    a = i[0]
    b = i[1]
    c = i[2]
    not_a = not a
    not_b = not b
    not_c = not c
    not_a_or_b = not_a or b
    b_and_c = b and c
    a_or_b_and_c = a or b_and_c
    not_a_or_c = not_a or c
    f = (not_a_or_b and a_or_b_and_c and not_a_or_c) or not_c
    print(
            f"| {a:^1} | {b:^1} | {c:^1} | "
            f"{int(not_a):^1} | {int(not_b):^1} | {int(not_c):^1} | "
            f"{int(not_a_or_b):^7} | {int(b_and_c):^7} | "
            f"{int(a_or_b_and_c):^14} | {int(not_a_or_c):^7} | {int(f):^1} |"
        )

print("Формула нейтральна і виконувана\n")

print("Зведена форма: b ∨ c̄\n")
print("  |- b -|  ")
print("--|     |--")
print("  |- c̄ -|  ")