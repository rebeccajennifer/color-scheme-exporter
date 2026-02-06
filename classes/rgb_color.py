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

from classes.ansi256_colors import Ansi256Colors
from utilities.color_scheme_utils import GeneralUtils as Utils

from flux_bunny_utils.dict_utils import DictUtils
from flux_bunny_utils.error_utils import ErrorUtils
from flux_bunny_utils.string_utils import StringUtils

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

  DEF_CRSR_BG: int = 0x808080
  DEF_BG_NORM: int = 0x262626
  DEF_FG_NORM: int = 0xc6c6c6
  DEF_BG_BOLD: int = 0x1c1c1c
  DEF_FG_BOLD: int = 0xbcbcbc

  DEF_ACCENT0: int = 0x00afaf
  DEF_ACCENT1: int = 0xaf5faf
  DEF_ACCENT2: int = 0x00afd7

  MIN_COLOR_VALUE: int = 0x00
  MAX_COLOR_VALUE: int = 0xff
  MAX_CUTOFF_DARK: int = 0x5f
  MIN_CUTOFF_DARK: int = 0x00
  MIN_CUTOFF_LITE: int = 0x5f
  MAX_CUTOFF_LITE: int = 0xd7

  DEFAULT_RGB_STR_LIST: str = str(
    ' 0x202020'
    ' 0xaf5f5f'
    ' 0x5faf5f'
    ' 0xafaf5f'
    ' 0x5f5faf'
    ' 0xaf5faf'
    ' 0x5fafaf'
    ' 0xafafaf'
    ' 0x878787'
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

    if (not isinstance(rgb_color, int)):
      desc: str =\
        f'{ErrorUtils.WRONG_TYPE} type(color) = {str(type(rgb_color))}'
      ErrorUtils.raise_exception_with_desc(err=TypeError(), desc=desc)

    if (rgb_color < 0 or rgb_color > 0xFFFFFF):
      desc: str =\
        f'{ErrorUtils.INVALID_VALUE} {rgb_color}'
      ErrorUtils.raise_exception_with_desc(err=ValueError(), desc=desc)

    rgb_map: dict = {}

    red: int = (rgb_color & RgbConst.RED_MASK) >> RgbConst.RED_RIGHT_SHIFT
    grn: int = (rgb_color & RgbConst.GRN_MASK) >> RgbConst.GRN_RIGHT_SHIFT
    blu: int = (rgb_color & RgbConst.BLU_MASK) >> RgbConst.BLU_RIGHT_SHIFT

    rgb_map[RgbConst.RED_STR] = red
    rgb_map[RgbConst.GRN_STR] = grn
    rgb_map[RgbConst.BLU_STR] = blu

    return rgb_map

  #_____________________________________________________________________
  def get_int_from_rgb_dict(rgb_dict: dict) -> str:
    """
    Creates integer from rgb dictionary.

    Parameters
      rgb_dict : Dictionary with 'red', 'grn', and 'blu' keys
                 E.g. {'red': 255, 'grn': 255, blu: 0}

    Returns
      Integer representing RGB color.

    E.g.
    input:  {'red': 255, 'grn': 255, blu: 0}
    output: 0xFFFF00
    """

    red: int = int(round(rgb_dict[RgbConst.RED_STR]))
    grn: int = int(round(rgb_dict[RgbConst.GRN_STR]))
    blu: int = int(round(rgb_dict[RgbConst.BLU_STR]))

    hex_val: int =\
      (red << RgbConst.RED_RIGHT_SHIFT) |\
      (grn << RgbConst.GRN_RIGHT_SHIFT) |\
      (blu << RgbConst.BLU_RIGHT_SHIFT)

    return hex_val

  #_____________________________________________________________________
  def get_hex_str_from_rgb_dict(rgb_dict: dict) -> str:
    """
    Creates hex string from rgb dictionary.

    Parameters
      rgb_dict : Dictionary with 'red', 'grn', and 'blu' keys
                 E.g. {'red': 255, 'grn': 255, blu: 0}

    Returns
      Hex string representing RGB color.

    E.g.
    input:  {'red': 255, 'grn': 255, blu: 0}
    output: 0xFFFF00
    """

    int_val: int = RgbColor.get_int_from_rgb_dict(rgb_dict)
    hex_str: str = StringUtils.int_to_hex6(int_val)

    return hex_str

  #_____________________________________________________________________
  def int_list_hex_str(l: list[int]) -> str:
    """
    Prints list of integers as 6 digit hex string.
    """

    out_str: str = ''


    for i in range (len(l)):
      out_str = f'{out_str}\nColor {i:<2}: 0x{l[i]:06x}'

    return out_str

  #_____________________________________________________________________
  def construct_color_print_str(text: str
    , fg: int = 0
    , bg: int = 0xffffff
  ) -> None:
    """
    Calls utility function to print colored text.

    Parameters
      text : text to print
      fg   : foreground color range[0x000000-0xFFFFFF]
      bg   : background color range[0x000000-0xFFFFFF]
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

    return Utils.construct_color_print_str(text=text
    , fg_red=fg_red
    , fg_grn=fg_grn
    , fg_blu=fg_blu
    , bg_red=bg_red
    , bg_grn=bg_grn
    , bg_blu=bg_blu
    )

  #_____________________________________________________________________
  def rgb_to_ansi256(rgb_color: int) -> int:
    """
    Converts 24 bit RGB color to nearest ANSI 256 color.

    Parameters
      rgb_color - 24 bit RGB color as integer

    Returns
      Nearest ANSI 256 color index as integer
    """

    if (isinstance(rgb_color, str)):
      rgb_color = StringUtils.str_hex_to_int(rgb_color)

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

      r_scaled = floor((red_near / 255.0) * 5)
      g_scaled = floor((grn_near / 255.0) * 5)
      b_scaled = floor((blu_near / 255.0) * 5)

      # Compute ANSI 256 color value
      ansi_index = 16 + (r_scaled * 36) + (g_scaled * 6) + b_scaled

    return ansi_index

  #_____________________________________________________________________
  def rgb_from_ansi_256(ansi_256_index: int) -> int:
    """
    Converts ANSI 256 color index to 24 bit RGB color.

    Parameters
      ansi_256_index - ANSI 256 color index as integer

    Returns
      24 bit RGB color as integer
    """

    return Ansi256Colors.rgb_list[ansi_256_index]

  #_____________________________________________________________________
  def make_background_color_dark\
    ( color
    , cutoff: int = RgbConst.MAX_CUTOFF_DARK
    ) -> dict:
    """
    Creates a darkened background color from the input color to ensure
    that light foreground text remains readable against it.

    Parameters
      color : RGB input color as int or dictionary
      cutoff: Maximum allowed channel value used to clamp brightness

    Returns
      A dictionary representing the darkened RGB background color
    """

    input_type: type = type(color)

    if (isinstance(color, str)):
      color: dict = StringUtils.str_hex_to_int(color)

    if (isinstance(color, int)):
      color: dict = RgbColor.get_rgb_from_hex(color)

    #___________________________________________________________________
    # Exception handling
    #___________________________________________________________________
    elif (not isinstance(color, dict)):

      desc: str =\
        f'{ErrorUtils.WRONG_TYPE} type(color) = {str(type(color))}'
      ErrorUtils.raise_exception_with_desc(err=TypeError(), desc=desc)

    max_pair: tuple = DictUtils.get_max_tuple(color)

    max_val: int = max_pair[1]

    if (max_val <= cutoff):
      return color

    multiplier: float = cutoff / max_val

    for key in color.keys():
      color[key] = int(color[key] * multiplier)

    if (input_type == int):
      return RgbColor.get_int_from_rgb_dict(color)

    return color

  #_____________________________________________________________________
  def scale_color\
    ( color
    , lo_cutoff: int = RgbConst.MIN_COLOR_VALUE
    , hi_cutoff: int = RgbConst.MAX_COLOR_VALUE
    ) -> dict:
    """
    Scales a color to be within the specified brightness range.

    Parameters
      color     : RGB input color as int or dictionary
      lo_cutoff : Minimum allowed channel value used to clamp brightness
      hi_cutoff : Maximum allowed channel value used to clamp brightness

    Returns
      A dictionary or int representing the scaled RGB color
    """

    color_in = color

    input_type: type = type(color)

    if (isinstance(color, str)):
      color: dict = StringUtils.str_hex_to_int(color)

    if (isinstance(color, int)):
      color: dict = RgbColor.get_rgb_from_hex(color)

    #___________________________________________________________________
    # Exception handling
    #___________________________________________________________________
    elif (not isinstance(color, dict)):

      desc: str =\
        f'{ErrorUtils.WRONG_TYPE} type(color) = {str(type(color))}'
      ErrorUtils.raise_exception_with_desc(desc=desc)

    #___________________________________________________________________
    # Determine highest and lowest channel values
    #___________________________________________________________________
    min_pair: tuple = DictUtils.get_min_tuple(color)
    max_pair: tuple = DictUtils.get_max_tuple(color)

    min_val: int = min_pair[1]
    max_val: int = max_pair[1]

    # If color is in range return without modification
    if (min_val >= lo_cutoff and max_val <= hi_cutoff):
      return color_in

    # Range of allowed values
    cutoff_range      : int = hi_cutoff - lo_cutoff

    # Normalize color channels
    for key in color.keys():
      clamped = max(0, color[key] - lo_cutoff)
      color[key] = (clamped) / max_val

    # Scale color channels
    for key in color.keys():
      color[key] = color[key] * cutoff_range + lo_cutoff

    # Return int type if input was int
    if (input_type == int):
      return RgbColor.get_int_from_rgb_dict(color)

    return color

  #_____________________________________________________________________
  def make_color_dark(color):
    """
    Creates a darkened color from the input color. Suitable for dark
    background.

    Parameters
      color : RGB input color as int or dictionary

    Returns
      A dictionary or int representing the darkened RGB color
    """

    return RgbColor.scale_color(color
      , lo_cutoff=RgbConst.MIN_CUTOFF_DARK
      , hi_cutoff=RgbConst.MAX_CUTOFF_DARK)

  #_____________________________________________________________________
  def make_color_lite(color):
    """
    Creates a lightened color from the input color. Suitable for light
    background.

    Parameters
      color : RGB input color as int or dictionary

    Returns
      A dictionary or int representing the lightened RGB color
    """

    return RgbColor.scale_color(color
      , lo_cutoff=RgbConst.MIN_CUTOFF_LITE
      , hi_cutoff=RgbConst.MAX_CUTOFF_LITE)

  #_____________________________________________________________________
  def make_background_color(color, is_dark: bool = True) -> dict:
    """
    Creates a background color from the input color to ensure that
    foreground text remains readable against it.

    Parameters
      color   : RGB input color as int or dictionary
      cutoff  : Channel value used to clamp brightness
      is_dark : If true, makes background dark. If false, makes lite.

    Returns
      A dictionary representing the lightened or darkened RGB
      background color
    """

    if (is_dark):
      return RgbColor.make_color_dark(color)

    else:
      return RgbColor.make_color_lite(color)

  #_____________________________________________________________________
  def make_foreground_color(color, is_dark: bool = True):
    """
    Creates a foreground color from the input color to ensure that
    foreground text remains readable against it.

    Parameters
      color   : RGB input color as int or dictionary
      cutoff  : Channel value used to clamp brightness
      is_dark : If true, makes foreground light. If false, makes dark.

    Returns
      A dictionary representing the lightened or darkened RGB
      foreground color
    """

    if (is_dark):
      return RgbColor.make_color_lite(color)

    else:
      return RgbColor.make_color_dark(color)
