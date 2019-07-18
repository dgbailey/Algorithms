#!/usr/bin/python

import argparse

#time complexity: O(n^2) solution, space complexity: O(1) ?
#recursive solution?
def find_max_profit(prices):

  current_max_profit = False #O(1)

  #start backwards
  #loop through price list
  #[100, 90, 80, 50, 20, 10]
  for i in range(len(prices) -1,-1,-1):#O(n)

      #for each price
      
      #loop backward through prices in slices without current value
      #for each loop subtract and compare with current profit, modifying if greater
      #at end return profit

    sell_price = prices[i] 

    for j in range(len(prices[:i]) -1,-1,-1):#0(n)
      
      buy_price = prices[j]
      comparison_profit = sell_price - buy_price

      if current_max_profit:#needed for very first comparison
        if comparison_profit > current_max_profit:
          current_max_profit = comparison_profit

      else:
        current_max_profit = comparison_profit


  return current_max_profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))