friend_a={"Python","Cooking","Hiking","Movies"}
friend_b={"Hiking","Gaming","Photography","Python"}
i=(friend_a & friend_b)
u=(friend_a | friend_b)
d=(friend_a - friend_b)
print(f'Shared:{i}')
print(f'All:{u}')
print(f'Unique Interests:{d}')