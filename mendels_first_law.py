def mendel(k, m, n): # Creates function with k, m, n as parameters
    number = k + m + n # Total number of species in the population
    total = number * (number - 1) # Total number of ordered pairs

    dominant = (k*k - k) * 1.00   # FF×FF pairs, 100% dominant offspring
    dominant += (m*m - m) * 0.75  # Ff×Ff pairs, 75% dominant offspring
    dominant += (n*n - n) * 0.00  # ff×ff pairs, 0% dominant offspring
    dominant += k*m * 2 * 1.00    # FF×Ff+Ff×FF(FF×Ff×2) pairs (both orders), 100% dominant offspring
    dominant += k*n * 2 * 1.00    # FF×ff+ff×FF(FF×ff×2) pairs (both orders), 100% dominant offspring
    dominant += m*n * 2 * 0.50    # Ff×ff+ff×Ff(Ff×ff×2) pairs (both orders), 50% dominant offspring

    return round(dominant / total, 5) # Divide sum by total pairs, round to hundreed thousands place

with open("rosalind_iprb.txt") as f: # Open the input file
    k, m, n = map(int, f.read().split()) # Read file, split into 3 integers k(FF), m(Ff), n(ff)
print(mendel(k, m, n)) # Call function and print the output result
