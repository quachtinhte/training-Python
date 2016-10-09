def fibo1(n):
    if n < 2:
        return n
    else:
        return fibo1(n - 1) + fibo1(n - 2)


def fibo2(n):
    temp1 = 1
    temp2 = 0
    for i in range(1, n):
        result = temp1 + temp2
        temp2 = temp1
        temp1 = result
    return result


def main():
    print(fibo1(10))
    print(fibo2(10))

if __name__ == "__main__":
    main()
