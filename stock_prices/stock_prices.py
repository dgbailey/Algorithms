#!/usr/bin/python

import argparse

def find_max_profit(prices):

  curr_min_price = 0
  curr_max_price = 0
  min_search_list =[]

  [1050, 270, 1540, 3800, 2]

  
  
  for i in range (len(prices) -1):

    if prices[i] > curr_max_price:
      curr_max_price = prices[i]

    
    
  min_search_list = prices[:prices.index(curr_max_price)]
  print("HELLO",min_search_list)
  curr_min_price = min_search_list[0]

  

  for i in range(len(min_search_list) -1):
    if min_search_list[i] < min_search_list[i +1]:
      curr_min_price = min_search_list[i]

   




  return curr_max_price - curr_min_price



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))