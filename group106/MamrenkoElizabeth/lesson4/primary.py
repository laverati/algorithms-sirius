def is_prime_sqr(n):
    if n == 1:
        return False
    i = 2
    while i * i <=n:
        if n % i == 0:
            return False
        i = i + 1
    return True

def test(result, awaiting_result):
    if result == awaiting_result:
        print('Ok')
    else:
        print('Ошибка', result, '!=', awaiting_result)

test(is_prime_sqr(5), True)
test(is_prime_sqr(4), False)
test(is_prime_sqr(104683), True)
test(is_prime_sqr(100000), False)

test(is_prime_sqr(5), True)
test(is_prime_sqr(4), False)
test(is_prime_sqr(104683), True)
test(is_prime_sqr(100000), False)
