# Быки и Коровы
import random


def calculate_bulls_and_cows(player_n, secret_n):
    bulls = 0
    cows = 0
    for index in range(len(player_n)):
        if player_n[index] == secret_n[index]:
            bulls += 1
    for index in range(len(player_n)):
        for j in range(len(secret_n)):
            if index != j and player_n[index] == secret_n[j]:
                cows += 1
    return bulls, cows


def check_player_num(player_n):
    is_player_num_correct = True
    if len(player_n) != 4:
        print("Only 4 digits allowed.")
        is_player_num_correct = False
    digits = 0
    for i in player_n:
        if i.isnumeric():
            digits += 1
    if digits != 4:
        print("Only digits allowed.")
        is_player_num_correct = False
    if len(set(player_n)) != 4:
        print("Repeating numbers are not allowed.")
        is_player_num_correct = False
    return is_player_num_correct


def start_game():
    num_list = list()

    while len(num_list) < 4:
        start_num = 0
        if len(num_list) == 0:
            start_num = 1

        s = str(random.randint(start_num, 9))
        if s not in num_list:
            num_list.append(s)

    secret_num = "".join(num_list)
    print(secret_num)

    rules = """Let's play a game!
    Try to guess a four digit number.
    All four digits should be different and can not start with 0.
    'Cows' is total number of digits you guessed right.
    'Bulls' shows how many of those that exists were placed at the
     right spot."""
    print(rules)

    player_num = input("Type your variant here:")
    while player_num != secret_num:
        if not check_player_num(player_num):
            player_num = input("Please try again:")

        bulls, cows = calculate_bulls_and_cows(player_num, secret_num)
        print(f"Bulls:{bulls}, Cows:{cows}")

        player_num = input("Try again:")
    else:
        print("You win this one, my friend.")

# start_game()


# Строки с заданным символом
def string_decorator(fn):
    def string_processing(str):
        result = []
        for i in str:
            if i != '#':
                result.append(i)
                # print("Added", result)

            if i == "#":
                if len(result) > 0:
                    result.pop()
                    # print("Removed", result)
        fn(str)

        print("Output:", ''.join(result))
        return ''.join(result)

    return string_processing


@string_decorator
def str_process(a: str):
    return str(a)


# myfunc("a#bc#d")
# myfunc("abc#d##c")
# myfunc("abc##d######")
# myfunc("#######")


# Использование marks
# Параметризация
# Использование fixture

