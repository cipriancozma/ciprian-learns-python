# lists
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c']
diverse = [1, 2, 'a', True]

# Data Structure
amazon_cart = ['sunglasses', 'notebooks', 'books', 'programming books', 'toys']
print(amazon_cart[1])

# List slicing
print(amazon_cart)
print(amazon_cart[0:2])
amazon_cart[0] = 'laptop'
print(amazon_cart)

new_list = amazon_cart[:] # copying the list
new_list[0] = 'gum'
print(amazon_cart)
print(new_list)

