#!/usr/bin/env python3.7

if __name__ == '__main__':

    inventory = [
        ("pommes", 22),
        ("melons", 4),
        ("poires", 18),
        ("fraises", 76),
        ("prunes", 51),
    ]

    reverse_inventory = [(quantity, name) for name, quantity in inventory]
    print(reverse_inventory)
    reverse_inventory.sort()
    print(reverse_inventory)

    invenotry = [(quantity, name) for name, quantity in sorted(reverse_inventory, reverse=False)]
    print(invenotry)



