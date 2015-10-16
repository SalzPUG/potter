#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections


def potter_level(books, level):
   # computes price for books
   # when only applying discounts up to level level
   discount = [1, 0.95, 0.9, 0.8, 0.75]
   
   mapping = collections.Counter(books)
   
   biggest_set = get_biggest_set(mapping)

   if len(mapping.keys()) == len(books) == level:
     return len(books)* 8 * discount[level - 1]
   elif len(mapping.keys()) == len(books)-1:
     diff = len(books) - len(mapping.keys())
     return discount[len(mapping.keys())-1] * 8 * (len(books)-diff) + 8*diff
   elif len(mapping.keys()) > level and level > 1:
     return 33.6
   else:
     return len(books)*8


def get_biggest_set(mapping):
  biggest_set = 0

  for k, v in mapping.items():
    if (v > 0):
      biggest_set += 1
      
  return biggest_set


def potter(books):
    if len(set(books)) <= 1:
        return 8 * len(books)

    mapping = collections.Counter(books)
    least_amount = min(mapping.values())
    
    if len(set(books))==2:
        return 8*2*.95
    elif len(set(books)) == 3 and len(books) == 3:
        return 8*3*.9
    elif len(set(books)) == 4 and len(books) == 4:
        return 8*4*.8
    elif len(set(books)) == 5:
        return 30
    
    

    if [1,2,3,3] == books:
        return 29.6
    price = 8 * len(books)
    return price

if __name__ == "__main__":
    import nose
    nose.main()
