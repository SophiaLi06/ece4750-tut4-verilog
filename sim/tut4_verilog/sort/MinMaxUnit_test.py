#=========================================================================
# MinMaxUnit_test
#=========================================================================

import pytest

from copy              import deepcopy
from random            import randint

from pymtl             import *
from pclib.test        import run_test_vector_sim
from MinMaxUnit import MinMaxUnit

#-------------------------------------------------------------------------
# Syntax helpers
#-------------------------------------------------------------------------

# We define the header string here since it is so long. Then reference
# the header string and include a comment to label each of the columns.

header_str = \
  ( "in0",  "in1", "out_min*", "out_max*" )

# We define a global variable 'x' so that we can simply use the x
# character instead of '?' to indicate don't care reference outputs

x = '?'

# Use xr as shorthand for xrange to make list comprehensions more compact


#-------------------------------------------------------------------------
# test_basic
#-------------------------------------------------------------------------

def test_basic( dump_vcd, test_verilog ):
  run_test_vector_sim( MinMaxUnit(), [ header_str,
    # in  in  out     out 
    # in0 in1 out_min out_max
    [ 0,  0,  0,  0],
    [ 1,  4,  1,  4],
    [ 3,  2,  2,  3],
    [ 0,  0,  0,  0],
  ], dump_vcd, test_verilog )

