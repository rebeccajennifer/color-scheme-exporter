#_______________________________________________________________________
#_______________________________________________________________________
#        _   __   _   _ _   _   _   _         _
#   |   |_| | _  | | | V | | | | / |_/ |_| | /
#   |__ | | |__| |_| |   | |_| | \ |   | | | \_
#    _  _         _ ___  _       _ ___   _                    / /
#   /  | | |\ |  \   |  | / | | /   |   \                    (^^)
#   \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
#_______________________________________________________________________
#
#-----------------------------------------------------------------------
#   Copyright 2025, Rebecca Rashkin
#   -------------------------------
#   This code may be copied, redistributed, transformed, or built
#   upon in any format for educational, non-commercial purposes.
#
#   Please give me appropriate credit should you choose to modify this
#   code. Thank you :)
#-----------------------------------------------------------------------
#
#_______________________________________________________________________
#   //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\
#_______________________________________________________________________
#_______________________________________________________________________
#   DESCRIPTION
#   Tests for RGB color related functions.
#_______________________________________________________________________

import pytest

from classes.rgb_color import RgbColor
from classes.rgb_color import RgbConst
from classes.ansi256_colors import Ansi256Colors

#_______________________________________________________________________
class TestConst:
  """
  Contains constants used in tests.
  """

  COLOR_INT: int = 0x80FF10
  RED_VAL: int = 128
  GRN_VAL: int = 255
  BLU_VAL: int =  16

  ERR_VAL: int = -1

#_______________________________________________________________________
def test_get_rgb_from_hex():
  rgb_dict = RgbColor.get_rgb_from_hex(TestConst.COLOR_INT)

  assert rgb_dict[RgbConst.RED_STR] == TestConst.RED_VAL
  assert rgb_dict[RgbConst.GRN_STR] == TestConst.GRN_VAL
  assert rgb_dict[RgbConst.BLU_STR] == TestConst.BLU_VAL

#_______________________________________________________________________
def test_ansii_256_from_rgb():

  for i in range(16, len(Ansi256Colors.rgb_list)):
    rgb_val = Ansi256Colors.rgb_list[i]
    ansi_256_val = RgbColor.ansi_256_from_rgb(rgb_val)
    assert ansi_256_val == i

#_______________________________________________________________________
def test_rgb_from_ansi_256():

  for i in range(16, len(Ansi256Colors.rgb_list)):
    ansi_256_val = i
    rgb_val = RgbColor.rgb_from_ansi_256(ansi_256_val)
    expected_rgb_val = Ansi256Colors.rgb_list[i]
    assert rgb_val == expected_rgb_val

#_______________________________________________________________________
def test_make_background_color():

  with pytest.raises(ValueError):
    RgbColor.make_background_color(color='hello')