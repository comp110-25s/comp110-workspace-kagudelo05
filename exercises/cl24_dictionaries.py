"""examples of set and dictionary syntax"""

pids: set[int] = {710000000, 712345678}
pids.add(730120710)

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluates to number of key-=value entries
print(f"{len(ice_cream)} flavors")

# add key-value entries using subscription notation
ice_cream["mint"] = 3

# access values by their key using subscription
print(ice_cream["chocolate"])

# re-assign values by their key using assignment
ice_cream["vanilla"] += 10

# check if key in dictionary
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No orders of mint")

# remove items by key using the pop method
ice_cream.pop("strawberry")

# loop through items using for-in loops
total_orders: int = 0
# the varuable (e.g., flavor) iterates over # each key one-by-one in the dictionary.
for flavor in ice_cream:
    print(f"{flavor}: {ice_cream[flavor]}")
    total_orders += ice_cream[flavor]

print(f"Total orders: {total_orders}")
