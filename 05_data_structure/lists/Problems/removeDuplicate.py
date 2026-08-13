items = [3, 5, 3, 2, 5, 7, 2, 8]
new_items = []
for item in items:
    if item not in new_items:
        new_items.append(item)
print(new_items)