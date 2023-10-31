from prime_na2918 import prime_na2918 as primes

def test_is_prime_param():
    '''
        Test the primes.is_prime function for a list of examples, 
including
        negative numbers, 0, and 1
    '''
    examples = [
        (2, True),
        (7, True),
        (8, False),
        (9, False),
        (-1, False),
        (-4, False),
        (0, False),
        (1, False),
    ]

    for example, expected in examples:
        result = primes.is_prime(example)
        assert result == expected

