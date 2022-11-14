#!/usr/bin/env python3

def main():
    while True:
        user_input = int(input("How many (0-100)? "))
        if(user_input <= 100):
            # range(stop)
            # range(start, stop, step)
            for num in range(user_input, 0, -1):
                print(f"{num} bottles of beer on the wall! \n{num} bottles of beer on the wall! {num} bottles of beer! You take one down, pass it around.")
            break
        else:
            print('invalid input')

if __name__ == "__main__":
    main()
