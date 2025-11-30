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
#   Contains operations related to RGB colors
#_______________________________________________________________________

from math import floor
from utilities.color_scheme_utils import GeneralUtils as Utils

#_______________________________________________________________________
class RgbConst:

  RED_STR: str = 'RED'
  GRN_STR: str = 'GRN'
  BLU_STR: str = 'BLU'

  RED_MASK: str = 0xFF0000
  GRN_MASK: str = 0x00FF00
  BLU_MASK: str = 0x0000FF

  RED_RIGHT_SHIFT: int = 16
  GRN_RIGHT_SHIFT: int = 8
  BLU_RIGHT_SHIFT: int = 0

  DEFAULT_CURSOR_COL: int = 0x808080
  DEFAULT_BACKGROUND: int = 0x1c1c1c
  DEFAULT_FOREGROUND: int = 0xeeeeee

  DEFAULT_RGB_STR_LIST: str = str(
    ' 0x202020'
    ' 0x870000'
    ' 0x008700'
    ' 0x878700'
    ' 0x000087'
    ' 0x870087'
    ' 0x008787'
    ' 0x878787'
    ' 0x000000'
    ' 0xd75f5f'
    ' 0x5fd75f'
    ' 0xd7d75f'
    ' 0x5f5fd7'
    ' 0xd75fd7'
    ' 0x5fd7d7'
    ' 0xd7d7d7'
  )

  DEFAULT_RGB_INT_LIST: list[int] =\
    Utils.str_list_to_hex_list(DEFAULT_RGB_STR_LIST.split())

  ANSI_256_DARK_GREYS: list =\
  [ 0x000000
  , 0x080808
  , 0x121212
  , 0x1c1c1c
  , 0x262626
  , 0x303030
  , 0x3a3a3a
  , 0x444444
  , 0x4e4e4e
  , 0x585858
  , 0x5f5f5f
  , 0x626262
  , 0x6c6c6c
  , 0x767676
  ]

  ANSI_256_LITE_GREYS: list =\
  [ 0x878787
  , 0x8a8a8a
  , 0x949494
  , 0x9e9e9e
  , 0xa8a8a8
  , 0xafafaf
  , 0xb2b2b2
  , 0xbcbcbc
  , 0xc6c6c6
  , 0xd0d0d0
  , 0xdadada
  , 0xd7d7d7
  , 0xe4e4e4
  , 0xeeeeee
  , 0xffffff
  ]


#_______________________________________________________________________
class RgbColor:

  #_____________________________________________________________________
  def get_rgb_from_hex(rgb_color: int) -> dict:
    """
    Creates map of red, green, and blue values from a single number.

    E.g.
    input:  0xFFFF00
    output: {'red': 255, 'grn': 255, blu: 0}
    """

    rgb_map: dict = {}

    red: int = (rgb_color & RgbConst.RED_MASK) >> RgbConst.RED_RIGHT_SHIFT
    grn: int = (rgb_color & RgbConst.GRN_MASK) >> RgbConst.GRN_RIGHT_SHIFT
    blu: int = (rgb_color & RgbConst.BLU_MASK) >> RgbConst.BLU_RIGHT_SHIFT

    rgb_map[RgbConst.RED_STR] = red
    rgb_map[RgbConst.GRN_STR] = grn
    rgb_map[RgbConst.BLU_STR] = blu

    return rgb_map

  #_____________________________________________________________________
  def int_list_hex_str(l: list[int]) -> str:
    """
    Prints list of integers as 6 digit hex string.
    """

    out_str: str = ''


    for i in range (len(l)):
      out_str = f'{out_str}\nColor {i:02}: 0x{l[i]:06x}'

    return out_str

  #_____________________________________________________________________
  def construct_color_print_str(text: str
    , fg: int = 0
    , bg: int = -1
  ) -> None:
    """
    Calls utility function to print colored text.

    Parameters
    text - text to print
    fg   - foreground color range[0x000000-0xFFFFFF]
    bg   - background color range[0x000000-0xFFFFFF]
    """

    # Convert rgb ints to dicts
    fg= RgbColor.get_rgb_from_hex(fg)
    bg= RgbColor.get_rgb_from_hex(bg)

    fg_red: int = fg[RgbConst.RED_STR]
    fg_grn: int = fg[RgbConst.GRN_STR]
    fg_blu: int = fg[RgbConst.BLU_STR]
    bg_red: int = bg[RgbConst.RED_STR]
    bg_grn: int = bg[RgbConst.GRN_STR]
    bg_blu: int = bg[RgbConst.BLU_STR]


    # Used in print color utility function
    # -1 indicates to print no background color
    if (bg == -1):
      bg_red: int = -1
      bg_grn: int = -1
      bg_blu: int = -1

    return Utils.construct_color_print_str(text=text
    , fg_red=fg_red
    , fg_grn=fg_grn
    , fg_blu=fg_blu
    , bg_red=bg_red
    , bg_grn=bg_grn
    , bg_blu=bg_blu
    )

  #_____________________________________________________________________
  def ansi_256_from_rgb(rgb_color: int) -> int:
    """
    Converts 24 bit RGB color to nearest ANSI 256 color.

    Parameters
    rgb_color - 24 bit RGB color as integer

    Returns
    Nearest ANSI 256 color as integer
    """

    valid_rgb_values: list[int] =\
    [0x00, 0x5f, 0x87, 0xaf, 0xd7, 0xff]

    # Get RGB components
    rgb_map: dict = RgbColor.get_rgb_from_hex(rgb_color)

    red: int = rgb_map[RgbConst.RED_STR]
    grn: int = rgb_map[RgbConst.GRN_STR]
    blu: int = rgb_map[RgbConst.BLU_STR]

    # If greyscale, handle separately
    if (red == blu and red == grn and red not in valid_rgb_values):

      valid_greyscale_values: list[int] =\
      [ 0x08, 0x12, 0x1c, 0x26, 0x30, 0x3a
      , 0x44, 0x4e, 0x58, 0x62, 0x6c, 0x76
      , 0x80, 0x8a, 0x94, 0x9e, 0xa8, 0xb2
      , 0xbc, 0xc6, 0xd0, 0xda, 0xe4, 0xee
      ]

      grey_near: int = min(valid_greyscale_values
        , key=lambda x: abs(x - red))

      ansi_index = 232 + ((grey_near - 8) // 10)

    else:
      # Find nearest valid value for each component
      red_near: int = min(valid_rgb_values
        , key=lambda x: abs(x - red))
      grn_near: int = min(valid_rgb_values
        , key=lambda x: abs(x - grn))
      blu_near: int = min(valid_rgb_values
        , key=lambda x: abs(x - blu))

      r_scaled = floor((red_near / 256.0) * 6)
      g_scaled = floor((grn_near / 256.0) * 6)
      b_scaled = floor((blu_near / 256.0) * 6)

      # Compute ANSI 256 color value
      ansi_index = 16 + (r_scaled * 36) + (g_scaled * 6) + b_scaled

    return ansi_index