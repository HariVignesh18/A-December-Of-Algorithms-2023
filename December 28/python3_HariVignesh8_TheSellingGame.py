def max_gadgets_sold(x, z, items, clients):
    items.sort(key=lambda item: (item['m'], -item['n']), reverse=True)
    clients.sort(key=lambda client: client['k'])

    gadgets_sold = 0
    sold_items = set()

    for client in clients:
        for i, item in enumerate(items):
            if i not in sold_items and item['m'] > client['k'] and item['n'] <= client['r']:
                gadgets_sold += 1
                sold_items.add(i)
                break

    return gadgets_sold

# Example usage:
x = 3
z = 3
items = [
    {'k': 10, 'r': 100, 'm': 5, 'n': 110},  # Item 0
    {'k': 9, 'r': 200, 'm': 2, 'n': 200},    # Item 1
    {'k': 20, 'r': 300, 'm': 30, 'n': 300}   # Item 2
]

clients = [
    {'k': 5, 'r': 110},    # Client 0
    {'k': 9, 'r': 500},    # Client 1
    {'k': 20, 'r': 400},   # Client 2
]

result = max_gadgets_sold(x, z, items, clients)
print(result)
