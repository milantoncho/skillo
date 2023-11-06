#TODO: 10. Create two sets with some common elements and find their intersection.

set_europe = {"Norway", "Italy", "Romania"}
set_eu = {"Italy", "France", "Romania"}
for i in set_eu:
    for j in set_europe:
        if j == i:
            print(j)

print("Intersecting set: ", set_europe & set_eu)
print("Intersecting set: ", set_europe.intersection(set_eu))