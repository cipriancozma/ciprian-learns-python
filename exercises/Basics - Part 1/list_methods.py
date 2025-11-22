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

basket.extend([400, 120, 90])
print(basket)

# removing
basket.pop()
print(basket)

basket.remove(1)
print(basket)

#basket.clear()
#print(basket)

# index
print(basket.index(2))
print(4 in basket)

# count
print(basket.count(2))

# sort
# basket.sort()
new_basket = sorted(basket)
print(new_basket)

basket.reverse()
print(basket)

numbers_list = list(range(1, 100))
print(numbers_list)

# join
sentence = ' '
new_sentence = sentence.join(["Hi", "my name is"])
print(new_sentence)

# list unpacking
a, b, c, *all = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)
print(all)
