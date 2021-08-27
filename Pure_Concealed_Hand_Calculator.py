#!/usr/bin/env python3

def sublist(a, b):
    c = b.copy()
    for item in a:
        if item in c:
            c.remove(item)
        else:
            return False
    return True


def find_quetou(hand14):
    result = []
    for i in range(10):
        if(sublist([i, i], hand14)):
            result.append(i)
    return result


def hu(h):
    huxing = []
    quetou_list = find_quetou(h)
    for quetou in quetou_list:
        huxing.append([quetou, quetou])
        hand12 = h.copy()
        hand12.remove(quetou)
        hand12.remove(quetou)
        hand12.sort()

        while(1):
            i = hand12[0]
            if(sublist([i, i, i], hand12)):
                hand12.remove(i)
                hand12.remove(i)
                hand12.remove(i)
                huxing.append([i, i, i])
            elif(sublist([i, i + 1, i + 2], hand12)):
                hand12.remove(i)
                hand12.remove(i + 1)
                hand12.remove(i + 2)
                huxing.append([i, i + 1, i + 2])
            else:
                huxing = []
                break
            if(len(hand12) == 0):
                return True, huxing
    return False, []


def ting(hand):
    result = []
    for i in range(1, 10):
        if (sublist([i, i, i, i], hand)):
            continue
        if (hu(hand + [i])[0]):
            print(f"Winning tile is {i}, melds are {hu(hand + [i])[1]}")
            result.append(i)
    if (result == []):
        print("No winning tiles!")
    return result


if __name__ == '__main__':
    print("Mahjong Calculator for Winning Tiles on Pure Concealed Hand")
    print("麻将门清清一色听牌计算器")
    print("Developed by Haofeng Jiang\n开发者：蒋浩锋\n2021/08/27\n")

    next_or_exit = ""
    while (next_or_exit != "exit"):
        h = []
        i = 0
        print("--------------------------------------------\nPlease enter the 13 tiles on your hand:")
        print("Or enter 'tx' to restart entries from Tile x if you entered wrongly")
        print("Or enter 'hand' to see what you have entered\n")
        while (i < 13):
            ele = input(f"Tile {i+1}: ")

            if (ele == ""):
                continue

            elif (ele == "hand"):
                print(h)
                continue

            elif (ele == 'tx'):
                print("Please specify which tile to restart, e.g. enter t1/t2/t3 ...")
                continue

            elif (ele[0] == 't' and ele[1:].isdigit()):
                if (int(ele[1:]) < 1 or int(ele[1:]) > i + 1):
                    print(f"You must restart from Tile 1 to Tile {i+1}, e.g. enter 't1' to restart from the beginning")
                    continue
                else:
                    i = int(ele[1:]) - 1
                    h = h[:i]
                    continue

            elif (not ele.isdigit() or ele == "" or int(ele) < 1 or int(ele) > 9):
                print("Your input must be integers from 1 to 9 inclusive, or enter 'tx' to restart from Tile x")
                continue

            elif (sublist([int(ele), int(ele), int(ele), int(ele)], h)):
                print("The same tile can only appear at most 4 times")
                continue
            h.append(int(ele))
            i += 1

        assert(len(h) == 13)
        h.sort()
        print(f"\nCurrent tiles on your hand are {h}")
        ting(h)

        next_or_exit = ""
        while (next_or_exit != "next" and next_or_exit != "exit"):
            next_or_exit = input("Enter 'next' to calculate the next problem, or enter 'exit' to exit:")

    print("\nThanks for using!")

