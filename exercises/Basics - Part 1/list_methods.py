# List methods
basket = [1, 2, 3, 4, 5]

print(len(basket))

# adding
basket.append(7)
new_list = basket
print(basket)
print(new_list)

basket.insert(5, 200)
print(basket)

basket.extend([120, 140])
print(basket)

# removing
basket.pop()
print(basket)

basket.remove(1)
print(basket)

basket.clear()
print(basket)

