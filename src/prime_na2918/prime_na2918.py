import math

def is_prime(n):
    """
    Determines if a given number is prime

    Parameters
    ----------
    n : float
      A numerical value (should be an int based on definitions of primes, 
      but the provided code does not correctly check for this)
   
    Returns
    -------
    bool
      A True/False value representing if the input is prime or not.

    Examples
    --------
    >>> from prime_na2918 import prime_na2918
    >>> prime_na2918.is_prime(1)
    False
    >>> prime_na2918.is_prime(2)
    True
    >>> prime_na2918.is_prime(10)
    False
    >>> prime_na2918.is_prime(-1)
    False
    """

    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
