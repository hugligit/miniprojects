*************
Prime Numbers
*************


.. tags:: tiny, math, scrolling



A prime number is a number that is evenly divisible only by one and itself.
Prime numbers have a variety of practical applications, but no algorithm can
predict them; we must calculate them one at a time. However, we do know that
there is an infinite number of prime numbers to be discovered.

This program finds prime numbers through brute-force calculation. Its code is
similar to Project 24, “Factor Finder.” (Another way to describe a prime number
is that one and the number itself are its only factors.) You can find out more
about prime numbers from https://en.wikipedia.org/wiki/Prime_number.

The `isPrime()` function accepts an integer and returns True if it is a prime
number. Otherwise, it returns False. Project 24 is worth studying if you’re
trying to understand this program. The isPrime() function essentially looks for
any factors in the given number and returns False if it finds any.

The algorithm in this program can quickly find large prime numbers. The number
one trillion has a mere 10 digits. But to find prime numbers that are as big as
a googol (a one followed by 100 zeros), you need to use an advanced algorithm
such as the Rabin-Miller primality test. Chapter 22 of my book Cracking Codes
with Python (No Starch Press, 2018) has a Python implementation of this
algorithm.


.. collapse:: prime_numbers.py

   .. literalinclude:: prime_numbers.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project56.html
