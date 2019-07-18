#!/usr/bin/python

import math
#O(n) solution time complexity, space complexity:O(1) ?
def recipe_batches(recipe, ingredients):
 
  limiting_factor = False

  for key, value in recipe.items():#loop through recipe and get key and value
    if key in ingredients:
      item_batches_possible = ingredients[key] // recipe[key]#perform floored division ingredient value //recipe value

      if limiting_factor: #compare this to current limiting factor value if LT , update limiting factor value
        if item_batches_possible < limiting_factor:
          limiting_factor = item_batches_possible

      else:
        limiting_factor = item_batches_possible

    else:
      limiting_factor = 0
      break

  return 0 if limiting_factor < 1 else limiting_factor#at end return this limiting factor value


if __name__ == '__main__':
 

  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))