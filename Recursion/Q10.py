def hanoi(n, source, auxillary, target):
    if n == 0:
        return
    else:
        hanoi(n-1, source, target, auxillary)
        print(f"Disk {n} have been moved from {source} to {target}")
        hanoi(n-1, auxillary, source, target)


hanoi(3, 'A', 'B', 'C')

