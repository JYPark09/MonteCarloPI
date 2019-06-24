import random

SIMULATION = 100000000

def check_inside(x, y):
    return (x ** 2 + y ** 2) <= 1

def main():
    count = 0

    for _ in range(SIMULATION):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if check_inside(x, y):
            count += 1
    
    print(f'Total simulation: {SIMULATION}')
    print(f'hits: {count}')

    PI = 4 * count / SIMULATION
    print(f'Estimated PI: {PI}')

if __name__ == '__main__':
    main()
