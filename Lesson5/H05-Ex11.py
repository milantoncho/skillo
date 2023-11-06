# #TODO: 11. Given two sets, write a function that determines if one set is a subset of the other.

set_europe = {"Norway", "Italy", "Romania","Spain","Austria"}
set_eu = {"Italy", "Romania","BG"}

def is_subset(set_small, set_big):
    return set_small.issubset(set_big)

if is_subset(set_eu,set_europe) is True:
    print("set_eu is a subset of set_europe")
    print(f"i.e. {set_eu} is a subset of {set_europe}")
else:
    print("set_eu is NOT a subset of set_europe")
    print(f"i.e. {set_eu} is a subset of {set_europe}")




#TODO:  Why are the {} reordered?
