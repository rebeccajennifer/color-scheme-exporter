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

#_______________________________________________________________________
# Tests for utility functions.
#_______________________________________________________________________

import pytest

from utilities.color_scheme_utils import GeneralUtils as Utils

#_______________________________________________________________________
class TestConst:
  """
  Contains constants used in tests.
  """

  ALL_CAPS_2_CHAR_WITH_0X: str = '0XFF'
  MIX_CAPS_2_CHAR_WITH_0X: str = '0xFf'
  ALL_CAPS_6_CHAR_WITH_0X: str = '0XFFFFFF'
  MIX_CAPS_6_CHAR_WITH_0X: str = '0xFfFFff'

  ALL_CAPS_2_CHAR_NO_PRFX: str = 'FF'
  MIX_CAPS_2_CHAR_NO_PRFX: str = 'fF'
  ALL_CAPS_6_CHAR_NO_PRFX: str = 'FFFFFF'
  MIX_CAPS_6_CHAR_NO_PRFX: str = 'fFfFFf'

  ERR_VAL_WITH_0X: str = '0x5g'

  INT_2_CHAR: int = 255
  INT_6_CHAR: int = 16777215

  ERR_VAL: int = -1

#_______________________________________________________________________
def test_str_hex2int_all_caps_with_0x():
  assert(
    Utils.str_hex_to_int(TestConst.ALL_CAPS_2_CHAR_WITH_0X) ==\
    TestConst.INT_2_CHAR
  )
  assert(
    Utils.str_hex_to_int(TestConst.ALL_CAPS_6_CHAR_WITH_0X) ==\
    TestConst.INT_6_CHAR
  )

def test_str_hex2int_mix_caps_with_0x():
  assert(
    Utils.str_hex_to_int(TestConst.MIX_CAPS_2_CHAR_WITH_0X) ==\
    TestConst.INT_2_CHAR
  )
  assert(
    Utils.str_hex_to_int(TestConst.MIX_CAPS_6_CHAR_WITH_0X) ==\
    TestConst.INT_6_CHAR
  )

def test_str_hex2int_all_caps_no_prfx():
  assert(
    Utils.str_hex_to_int(TestConst.ALL_CAPS_2_CHAR_NO_PRFX) ==\
    TestConst.INT_2_CHAR
  )
  assert(
    Utils.str_hex_to_int(TestConst.ALL_CAPS_6_CHAR_NO_PRFX) ==\
    TestConst.INT_6_CHAR
  )

def test_str_hex2int_mix_caps_no_prfx():
  assert(
    Utils.str_hex_to_int(TestConst.MIX_CAPS_2_CHAR_NO_PRFX) ==\
    TestConst.INT_2_CHAR
  )
  assert(
    Utils.str_hex_to_int(TestConst.MIX_CAPS_6_CHAR_NO_PRFX) ==\
    TestConst.INT_6_CHAR
  )

#_______________________________________________________________________
def test_str_hex2int_err():
  with pytest.raises(Exception):
    Utils.str_hex_to_int(TestConst.ERR_VAL_WITH_0X)

#def test_str_hex2int_err_output():
#  Utils.str_hex_to_int(TestConst.ERR_VAL_WITH_0X)