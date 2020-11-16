

animal_types = {'Dog': 2, 'Cat': 1, 'Duck': 1}

animals_count = list(animal_types.values())
max_count = animals_count.index(max(animals_count))
max_indices = [i for i, x in enumerate(animals_count) if x == animals_count[max_count]]

animals_to_consider = list(animal_types.keys())

for max_index in max_indices:
    del animals_to_consider[max_index]

print()
