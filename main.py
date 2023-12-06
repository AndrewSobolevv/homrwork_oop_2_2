
cook_book = {}
with open("recipes.txt", encoding="utf-8") as f:
    for line in f:
        dish = line.strip()
        count = f.readline()
        recipe = []
        for ingr in range(int(count)):
            ingr, quant, measure = f.readline().strip().split("|")
            recipe.append({"ingr_name": ingr, "quant": quant, "measure": measure})
        cook_book.setdefault(dish, recipe)
        skip = f.readline()

# print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        recipe = cook_book.get(dish)
        if recipe is not None:
            for ingredient in recipe:
                ingredient_name = ingredient['ingr_name']
                ingredient_quantity = int(ingredient['quant']) * person_count
                ingredient_measure = ingredient['measure']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': ingredient_quantity, 'measure': ingredient_measure}
                else:
                    shop_list[ingredient_name]['quantity'] += ingredient_quantity
    return shop_list


result = get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2)
for ingredient, details in result.items():
    print(f"{ingredient}: {details['measure']}, {details['quantity']}")

