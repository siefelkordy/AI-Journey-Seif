lucky_numbers = [42  , 8, 15, 16, 23, 42]
friends = ["Chandler", "Monica", "Ross", "Rachel", "Joey", "Phoebe"]
friends.extend(lucky_numbers)
friends.append("Gunther")
friends.insert(1, "Janice")
friends.remove("Ross")
friends.pop()
friends.pop(3)
print(friends.index("Monica"))
print(friends.count("Chandler"))
friends.sort()
lucky_numbers.sort()
friends1 = friends.copy()
print(friends)
