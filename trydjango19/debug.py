n = 0

if n % 2 != 0:
    print('Not wierd')
else:
    if n % 2 == 0 and n > 20:
        print('Not weird')
    else:
        if n % 2 == 0 and n in range(6,20):
            print('Weird')
        elif n % 2 == 0 and n in range(2,5):
            print('Not weird')










if __name__ == '__main__':
    n = int(input())