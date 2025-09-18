def tower_of_hanoi(n, source, auxiliary, target):
    """
    Solve the Tower of Hanoi puzzle and print each move.
    n: number of disks
    source: rod name (A)
    auxiliary: rod name (B)
    target: rod name (C)
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        tower_of_hanoi(n - 1, source, target, auxiliary)
        print(f"Move disk {n} from {source} to {target}")
        tower_of_hanoi(n - 1, auxiliary, source, target)

# --- Example usage ---
n_disks = int(input("Enter number of disks: "))
tower_of_hanoi(n_disks, 'A', 'B', 'C')
