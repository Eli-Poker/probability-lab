import random

def check_similarity(values):
    for i in range(len(values)):
        for j in range(1+i, len(values)):
            if values[i] == values[j]:
                return True
    return False


def random_birthdays(n):
    birthdays = []
    for _ in range(n):
        birthdays.append(random.randint(0, 364))
    return birthdays


def simulate_birthday(n, trials):
    count = 0
    for _ in range(trials):
        birthdays = random_birthdays(n)
        if check_similarity(birthdays):
            count += 1
    prob = count/trials
    return prob

def prob_all_different(n):
    if n < 2:
        return 1.0
    return (365-n+1)/365 * prob_all_different(n-1)
def theoretical_proba(n):
    return 1 - prob_all_different(n)
    
def main():
    random.seed(42)
    n_values = [1, 5, 10, 20, 23, 30, 40, 50, 60, 366]
    trials = 10000
    print("For X number of people, the probability of at least two people share the same birthday.")
    for i in range(len(n_values)):
        proba = simulate_birthday(n_values[i], trials)
        tproba = theoretical_proba(n_values[i])
        print(f"{n_values[i]} people | Empirical probability:{proba:.3f}| Theoretical probability:{tproba:.3f} | difference: {abs(tproba - proba):.3f} ")
    
            


if __name__ == "__main__":
    main()