#TODO: 15. Write a program that generates a set of prime numbers less than 100 using list comprehensions and sets. Hint: Write a function that checks if a number is prime or not.

def prime_n(some_input):
    list = [2,3,5]
    my_set = set()
    prime = 0
    for i in list:
        if some_input%i == 0 and some_input != 2 and some_input != 3 and some_input != 5:
            prime = 0
            break
        else:
            prime = prime+1
    if prime>0:
        return True
    else:
        return False


set_of_primes = {j for j in range(2, 10) if prime_n(j)}
#AVD reminder: loop j through a range and for every j-value, check if the function is true or false. return the true values.
print(set_of_primes)
