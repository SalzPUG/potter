#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *

from potter import potter, potter_level


def test_potter_level_1():
  assert_equals( potter_level([1,2], 1), 8 * 2 )
  assert_equals( potter_level([1,1], 1), 8 * 2 )
  assert_equals( potter_level([1,5], 1), 8 * 2 )

def test_potter_level_2():
  assert_equals( potter_level([1,2], 2), 8 * 2 * 0.95 )
  assert_equals( potter_level([1,1], 2), 8 * 2 )
  assert_equals( potter_level([1,5], 2), 8 * 2 * 0.95 )


def test_potter_level_3():
  assert_equals( potter_level([1,2,3], 3), 8 * 3 * 0.9 )
  assert_equals( potter_level([1,1,1], 3), 8 * 3 )
  assert_equals( potter_level([1,1,3], 3), 8 * 2 * .95 + 8 )

def test_potter_level4():
  assert_equals( potter_level([1,2,3,4], 4),  8 * 4 * .8)
  assert_equals( potter_level([1,1,1,1], 4),  8 * 4)
  assert_equals( potter_level([1,1,3,4], 4),  8 * 3 * .9 +8 )

def test_potter_level45():
    assert_equals( potter_level([1,2,3,4,5], 4), 8 * 4 * .8 + 8 )

def test_zero_potter():
  assert_equals( potter([]), 0  )
  
  
def test_one_potter():
  for i in range(1,6):
    assert_equals( potter([i]),   8 )
    
def test_two_potters():
    assert_equals(potter([1,2]), 15.20)

def test_two_other_potters():
    assert_equals(potter([3,4]), 15.20)

def test_three_potters():
  assert_equals( potter([1,2,3]), 8*3*.9 )

def test_four_potters():
    assert_equals(potter([1,2,3,4]), 8*4*.8)
  
def test_all_the_potters():
  assert_equals( potter([1,2,3,4,5]), 30 )

  
def test_maybe_some_potter():
  assert_equals( potter([1,2,3,3]), 3*8*0.9+8 )
