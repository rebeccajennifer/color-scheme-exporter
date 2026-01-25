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
def test_make_background_color_dark():

  # Cutoff is 0x5f (95 decimal) making test so that highest value is 2x
  # Multiplier should be 1/2 so each element should be 1/2
  color     : int   = RgbColor.get_rgb_from_hex(0xbe1020)
  color_bg  : dict  = RgbColor.get_rgb_from_hex(0x5f0810)
  test_color: dict  = RgbColor.make_background_color_dark(color)

  assert test_color == color_bg

  # Setting cutoff greater than largest element, should return same
  test_color: dict  =\
    RgbColor.make_background_color_dark(color, cutoff=0xff)

  assert test_color == color

#_______________________________________________________________________
def test_make_background_color_lite():

  # Cutoff is 0x5f (95 decimal) making test so that highest value is 2x
  # Multiplier should be 1/2 so each element should be 1/2
  color     : int   = RgbColor.get_rgb_from_hex(0x401020)
  color_bg  : dict  = RgbColor.get_rgb_from_hex(0xff80ff)
  test_color: dict  = RgbColor.make_background_color_lite(color, 0x80)

  assert test_color == color_bg

  # Setting cutoff greater than largest element, should return same
  test_color: dict  =\
    RgbColor.make_background_color_dark(color, cutoff=0x10)

  #assert test_color == color

#_______________________________________________________________________
def test_make_background_color_err():

  #with pytest.raises(ValueError):
  #  RgbColor.make_background_color_dark(color='hello')

  with pytest.raises(ValueError):
    c = RgbColor.make_background_color_dark(color=-1)

  #with pytest.raises(ValueError):
  #  RgbColor.make_background_color_lite(color='hello')

  #with pytest.raises(Exception):
  #  c = RgbColor.make_background_color_lite(color=-1)

#_______________________________________________________________________
def test_scale_color():

  lo_cutoff: int = 0x10
  hi_cutoff: int = 0xe0

  color       : int = 0x804020
  color_scaled: int = 0x804020

  test_color  : int = RgbColor.scale_color(color, lo_cutoff, hi_cutoff)
  assert test_color == color_scaled

  lo_cutoff   : int = 0x00
  hi_cutoff   : int = 0xe0
  color       : int = 0xff8010
  color_scaled: int = 0xe0700e
  test_color  : int = RgbColor.scale_color(color, lo_cutoff, hi_cutoff)

  assert test_color == color_scaled

#_______________________________________________________________________
def test_scale_color_err():

  with pytest.raises(ValueError):
    RgbColor.scale_color(color='hello')

  with pytest.raises(ValueError):
    c = RgbColor.scale_color(color=-1)
