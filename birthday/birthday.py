import random

def check_similarity(list):
    for i in range(len(list)):
        for j in range(1+i, len(list)):
            if list[i] == list[j]:
                return True
    return False


def main():
    n = 5
    birthdays = []
    for i in range(n):
         birthdays.append(random.randint(0, 364))
    if check_similarity(birthdays) == True:
        print("Match")
    else:
        print("No Match")

if __name__ == "__main__":
    main()