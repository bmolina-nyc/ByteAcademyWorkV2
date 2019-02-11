## The Generator Version of range()

    Create your own implementation of `range()`. It should support the `range(max)`, `range(min,max)`, and `range(min,max,step)` modes of invoking the function.

## Words, one line at a time

    Create a generator that takes a path to a textfile as its argument. `linewords(path)` and yields a list of words for each line of the file (use .split()).

    NOTE: `with open` doesn't play too nice with yield (the file is no longer open after the first yield) You'll need to open a file and then manually close it after all lines have been yielded.

## Math problems for the mathy:

### Prime Factors.

    There are two kinds of positive numbers: prime numbers and composite numbers. A composite number is the product of a sequence of prime numbers. You can write a simple function to factor numbers and yield each prime factor of the number.

    Your factor function can accept a number, n, for factoring. The function will test values, f, between 2 and the square root of n to see if the expression n % f == 0 is true. If this is true. then the factor, f, divides n with no remainder; f is a factor.

    Don't use a simple-looking for -loop; the prime factor of 128 is 2, repeated 7 times.

### The Sieve of Eratosthones

    Look up the Sieve of Eratosthenes. We created a list or a set of candidate prime numbers. This exercise has three parts: initialization, generating the list (or set) or prime numbers, then reporting. In the list version, we had to filter the sequence of boolean values to determine the primes. In the set version, the set contained the primes.

    Within the Generate step, there is a point where we know that the value of p is prime. At this point, we can yield p. If yield each value as we discover it, we eliminate the entire "report" step from the function.
