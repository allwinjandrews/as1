def prime(n):
    """
    To check if a number is prime or not
    :param n: number
    :return: number
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def factor(n):
    """
    To return factors of a number
    :param n: number
    :return: list of factors
    """
    f_list = []
    for i in range(1, n+1, 1):
        if n % i == 0:
            f_list.append(i)
    return f_list


def prime_fact(n):
    """
    To return prime factors of a number
    :param n: number
    :return: list of prime factors
    """
    prime_f = []
    fact = factor(n)
    for i in fact:
        if prime(i) == 1:
            prime_f.append(i)
    return prime_f


if __name__ == '__main__':
    num = int(input('enter the number to be checked:'))

    if num < 2:
        print('Neither prime nor composite')
    elif prime(num) is False:
        print('Not Prime')
    else:
        print("Prime")

    if not prime_fact(num):
        print('no prime factors')
    else:
        print('The prime factors are:\n', prime_fact(num))

    print('The factors are:\n', factor(num))
