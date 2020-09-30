def is_power_of_two(n: int) -> bool:
    return n!=0 and (n & (n - 1)==0)


def is_proth_number(n: int) -> bool:
    """
    Function to check if a number is a 
    proth prime numer or not
    Formula: n = k * (2^n) + 1
    """
    # step 1: subtract 1 from n

    n -= 1

    # step 2: loop through ood numbers from k=1 to n//k
    # and check for divisibility of n by k

    k = 1

    while (k < n//k):
        if n%k==0:
            # if n is divisible by k, check if result is power of two 
            if is_power_of_two(n//k):
                return True
        
        # set k to the next odd number
        k += 2
    # base return value
    return False


if __name__ == "__main__":
    from sys import argv, exit
    
    if len(argv) < 2:
        print("Number not provided. Run file with number as argument e.g\npython3 proth_number.py 11")
        exit()

    number = argv[1]
    try:
        number = int(number)
        print("%i is%sa Proth Number"%(number, ' ' if is_proth_number(number) else ' not '))
    except ValueError:
        print("Provided number not an integer")

