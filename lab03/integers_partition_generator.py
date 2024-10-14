def partition_generator(n, l=None, added=""):
    if l is None:
        l = n

    if n == 0:
        yield added.strip()

    for i in range(1, min(l, n) + 1):
        yield from partition_generator(n - i, i, added + str(i) + " ") 

n = 100
with open("integers_partitions_100.txt", "w") as file:
    for partition in partition_generator(n):
        file.write(partition)
        file.write("\n")
