cook_book = {}

with open('write.txt', 'rt', encoding = "utf-8") as file:
    for l in file:
        dish_name = l.strip()
        new_list = []
        count = file.readline()
        for i in range(int(count)):
            dish_ing = file.readline()
            ingredient_name, quantity, measure  = dish_ing.strip().split(' | ')
            new_list.append({'ingredient_name': ingredient_name, 'quantity': int(quantity),'measure': measure})
            dep = {dish_name: new_list}
        separate = file.readline()
        cook_book.update(dep)

print(f'cook_book = {cook_book}')

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingredient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
        del [new_shop_list_item['ingredient_name']]
      else:
        shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
        del [new_shop_list_item['ingredient_name']]

    return shop_list





print(get_shop_list_by_dishes(['Фахитос'], 2))

