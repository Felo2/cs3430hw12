#!/usr/bin/python

###################################
# module: linprog.py
# Krista Gurney
# A01671888
###################################

from line_eq import line_eq
from maker import make_line_eq
from maker import make_var, make_const, make_prod
from maker import make_pwr, make_plus
from maker import make_point2d
from const import const
from var import var
from prod import prod
from pwr import pwr
# from poly12 import is_pwr_1
from plus import plus
from tof import tof
from consts import is_const_line
import sys



### sample line equations
lneq1 = make_line_eq(make_var('y'),
                     make_const(2))
lneq2 = make_line_eq(make_var('y'),
                     make_var('x'))
lneq3 = make_line_eq(make_var('y'),
                     make_var('y'))
lneq4 = make_line_eq(make_var('y'),
                     make_prod(make_const(2.0),
                               make_pwr('x', 1.0)))
lneq5 = make_line_eq(make_var('y'),
                     make_prod(make_const(5.0),
                               make_pwr('y', 1.0)))
lneq6 = make_line_eq(make_var('y'),
                     make_plus(make_prod(make_const(5.0),
                                         make_pwr('x', 1.0)),
                               make_const(4.0)))
lneq7 = make_line_eq(make_var('y'),
                     make_plus(make_prod(make_const(5.0),
                                         make_pwr('y', 1.0)),
                               make_const(4.0)))
lneq8 = make_line_eq(make_var('y'),
                     make_plus(make_prod(make_const(3.0),
                                         make_pwr('x', 1.0)),
                               make_const(-4.0)))


def line_intersection(lneq1, lneq2):
    # Case 1: 2 const lines
    if is_const_line(lneq1):
        if is_const_line(lneq2):
            if lneq1.get_lhs().get_name() == 'x':
                x = lneq1.get_rhs().get_val()
                y = lneq2.get_rhs().get_val()
            elif lneq1.get_lhs().get_name() == 'y':
                y = lneq1.get_rhs().get_val()
                x = lneq2.get_rhs().get_val()
            else:
                raise Exception('line_intersection: ' + str(lneq1))
        else:
            y = lneq1.get_rhs().get_val()
            x = tof(lneq2.get_rhs())(y)
    elif is_const_line(lneq2):
        #Case 2: 1 const line y = 1 ;y = x -1
        y = lneq2.get_rhs().get_val()
        x = tof(lneq1.get_rhs())(y)
    elif isinstance(lneq1.get_rhs(), pwr):#y = 1x; y = -1x +6
        eq1_coeff = get_line_coeffs(lneq1)
        eq2_coeff = get_line_coeffs(lneq2)
        if isinstance(lneq2.get_rhs(), plus):
            if isinstance(lneq2.get_rhs().get_elt2(), const):
                eq2_const = lneq2.get_rhs().get_elt2().get_val()
                x = eq2_const/(eq1_coeff - eq2_coeff)
                y = tof(lneq1.get_rhs())(x)

    else:
        raise Exception('line_intersection: ' + 'unknown equations')

    return make_point2d(x, y)

def get_line_coeffs(lneq):
    if isinstance(lneq.get_rhs(), prod):
        if isinstance(lneq.get_rhs().get_mult1(), const):
            return lneq.get_rhs().get_mult1().get_val()
        else:
            raise Exception("Unknown product")
    elif isinstance(lneq.get_rhs(), pwr):
        return 1.0
    elif isinstance(lneq.get_rhs(), plus):
        if isinstance(lneq.get_rhs().get_elt1(), prod):
            if isinstance(lneq.get_rhs().get_elt1().get_mult1(), const):
                return lneq.get_rhs().get_elt1().get_mult1().get_val()
            else:
                raise Exception('Unknown mult1')
        else:
            raise Exception('Unknown prod')
    else:
        raise Exception('Unknown line equation')



def maximize_obj_fun(f, corner_points):
  ## your code here
  pass

def minimize_obj_fun(f, corner_points):
  ## your code here
  pass


## write your answer to problem 1a as x, y, mv
def opt_prob_1a():
  ## your code here
  pass

## write your answer to problem 1b as x, y, mv
def opt_prob_1b():
  ## your code here
  pass

## write your answer to problem 1c as x, y, mv
def opt_prob_1c():
  ## your code here
  pass
  


  
  


