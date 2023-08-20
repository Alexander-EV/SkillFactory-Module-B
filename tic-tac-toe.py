cell = list(range(1, 10))
print("Добро пожаловать в игру Крестики-нолики!")
print("Перед вами поле 3x3. Каждый игрок по очереди ставит X или O в ячейку с определенной цифрой.")


def show_field(cell):
    print("-" * 13)
    for i in range(3):
        print("|", cell[0 + i * 3], "|", cell[1 + i * 3], "|", cell[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_token):
    while True:
        player_answer = input("Куда поставить " + player_token + "? ")
        if not (player_answer.isdigit()):
            print("Введите число")
            continue
        player_answer = int(player_answer)
        if 1 > player_answer > 9:
            print("Введите число от 1 до 9.")
            continue
        if str(cell[player_answer - 1]) not in "XO":
            cell[player_answer - 1] = player_token
        else:
            print("Эта клетка уже занята!")
            continue
        break
    return player_token


def check_win(cell):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if cell[each[0]] == cell[each[1]] == cell[each[2]]:
            return cell[each[0]]
    return False


def main(cell):
    counter = 0
    while True:
        show_field(cell)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1

        if check_win(cell):
            print("Поздравляю!", check_win(cell), "выиграл!")
            break
        if counter == 9:
            print("Ничья!")
            break
    show_field(cell)


main(cell)

