def prime_def():
    prime_set = set(range(1, 1001))
    for i in range(2, 101):
        if i in prime_set:
            prime_set -= set(range(2 * i, 1001, i))
    return prime_set


def is_prime_num(num):
    global PRIME_SET
    if not PRIME_SET:
        PRIME_SET = prime_def()
    return num in PRIME_SET


def dividers_num(num):
    result = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result.append(i)
    print(result)
    return result+[num]


def prepare_prime_set(num):
    global PRIME_SET
    if not PRIME_SET:
        PRIME_SET = prime_def()
    prime_list = sorted(list(PRIME_SET))
    prime_list = [i for i in prime_list if i <= num]
    return prime_list


def biggest_simple_divider(num):
    prime_list = prepare_prime_set(num)
    for i in reversed(prime_list):
        if num % i == 0:
            return i


def list_simple_divider(num):
    prime_list = prepare_prime_set(num)
    result = []
    for i in reversed(prime_list):
        while num % i == 0:
            num //= i
            result.append(i)
        if num == 1:
            break
    return result


def max_divider(num):
    result = dividers_num(num)
    return result[-2]


PRIME_SET = set()


def test_is_prime_num():
    assert is_prime_num(97)


def test_is_prime_num1():
    assert is_prime_num('234')


def test_is_prime_num2():
    assert is_prime_num([234, 456])


def test_biggers():
    assert biggest_simple_divider(30) == 15


def test_biggers1():
    assert biggest_simple_divider(30) == 5


def test_list_prime():
    assert list_simple_divider(30) == [1, 2, 4]


def test_list_prime1():
    assert list_simple_divider(30) == [2, 3, 5]


# тест грязные функции
def test_div_list():
    assert dividers_num(30) == []


def test_max_div():
    assert max_divider(30) == 15