# Greatest_Common_Divisor

1. Naive Algorithm: a search iterating up to the smaller number, an algorithm which performs a throughout search, however, could take very long to retrive the answer, if it ever does. The time complexity is linear O(n)

2. Euclidean Algorithm: a improved way of searching for GCD based on Eclidean Algorithm. Using the sum of remainder and the product of the larger number and some q number 
-> a = a' + bq given the question GCD(a, b). The time complexity is O(Log(n)), which cuts the time complexity of the naive algorithm drastically.
