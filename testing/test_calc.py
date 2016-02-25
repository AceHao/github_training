import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import calc

def test_add():
    assert calc.add(1, 2) == 3
    assert calc.div(4, 2) == 2
    assert calc.subtract( 100, -1) == 101
