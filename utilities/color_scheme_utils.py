#_______________________________________________________________________
# This file contains general utilities. The classes and functions in
# this file should be independent of the programs that consume it.
#_______________________________________________________________________

import json

from flux_bunny_utils.error_utils import ErrorUtils
from flux_bunny_utils.string_utils import StringUtils


#_______________________________________________________________________
class UtilErrors:

  LINE: str =\
    '\n________________________________________________________________'

  ERROR: str =\
    f'{LINE}'\
    '\nUH OH! The program has encountered an error!'\
    f'{LINE}'

  ERROR_TYPE: str =\
    f'{ERROR}'\
    '\nTYPE:        '

  DESC: str =\
    '\nDESCRIPTION: '

  CONVERSION_ERROR: str =\
    f'Invalid conversion'

#_______________________________________________________________________
class GeneralUtils:

  MAX_COLOR: int = 0xFFFFFF

  #_____________________________________________________________________
  def str_list_to_hex_list(l: list[str]) -> list[int]:
    """
    Converts a list of strings representing hexadecimal numbers to a
    list of ints.

    Parameters
    l - list of strings representing hex numbers
      E.g. ["0xFF","0x5F","0x87"]

    Returns
    List of ints corresponding with the hex representation of the
    argument.
      E.g. [255, 95, 135]
    """

    list_length: int = len(l)
    int_list: list[int] = [0] * list_length

    for i in range(list_length):
      int_list[i] = StringUtils.str_hex_to_int(l[i])

    return int_list

  #_____________________________________________________________________
  def rgb_str_to_int_list(rgb_str_list: str) -> list[int]:
    """
    Generates a list of RGB values from a white space separated list
    of 24-bit ints.

    Parameters
    rgb_str_list - string with a list of hex values,
      '0x000000 0xff0000 0x00ff00'

    Returns
    List of ints corresponding to input argument
    """

    #_____________________________________________________________________
    # Parse color inputs to list of strings
    #_____________________________________________________________________
    color_str_list: list = rgb_str_list.split()

    # Initialize int color list
    return GeneralUtils.str_list_to_hex_list(color_str_list)

  #_____________________________________________________________________
  def read_hex_color_json(file_path: str) -> dict:
    """
    Reads json file in the format
    ________________________________
    { "intense-bold"  : "true"
    , "background"    : "0x282828"
    , "foreground"    : "0xDF5f87"
    , "color-list"    :
        [ "0x5f0000"
        ...
        , "0xFFFFFF"
        ]
    }
    ________________________________

    Parameters
    file_path - path to json file

    Returns
    Dictionary with key value pairs from json file
    """

    # Open and read the JSON file
    with open(file_path, 'r') as file:
      file_dict: dict = json.load(file)
      return file_dict

  #_____________________________________________________________________
  def bool_to_str(flag: bool, capitalize: bool = False) -> str:
    """
    Prints Boolean string.

    Parameters
    flag        - Boolean to print
    capitalize  - Capitalize first letter
    """

    out_str: str = ''

    if (flag):
      out_str = 'true'
    else:
      out_str = 'false'

    if (capitalize):
      out_str = f'{out_str[0].upper()}{out_str[1:len(out_str)]}'

    return out_str

  #_____________________________________________________________________
  def str_to_bool(s: str) -> bool:
    """
    Returns boolean corresponding with input string. Will return true
    if string is any capitalization of the word 'true'.

    Parameters
    s - any string, assumption s = {'true', 'True', 'false', 'False'}

    Returns
    bool
    """

    lowercase: str = s.lower()

    return lowercase == 'true' or lowercase == 't'

  #_____________________________________________________________________
  def construct_color_print_str(text: str
    , fg_red: int
    , fg_grn: int
    , fg_blu: int
    , bg_red: int = -1
    , bg_grn: int = -1
    , bg_blu: int = -1
  ) -> None:
    """
    Prints text to screen with defined foreground color.

    Parameters
    text - text to print
    fg_red  - foreground red value in RGB range[0-255]
    fg_grn  - foreground grn value in RGB range[0-255]
    fg_blu  - foreground blu value in RGB range[0-255]

    bg_red  - background red value in RGB range[0-255]
              -1 indicates no background color
    bg_grn  - background grn value in RGB range[0-255]
              -1 indicates no background color
    bg_blu  - background blu value in RGB range[0-255]
              -1 indicates no background color
    """

    # Background color
    set_bg_str: str = ''

    if (bg_red > -1 and bg_grn > -1 and bg_blu > -1):

      # 48: Bash parameter code for foreground
      set_bg_str = f'\033[48;2;{bg_red};{bg_grn};{bg_blu}m'

    # Print text in background and foreground color as indicated in arg
    # 38: Bash parameter code for foreground
    colored_str: str =\
      f'\033[38;2;{fg_red};{fg_grn};{fg_blu}m{set_bg_str}{text}\033[0m'

    return colored_str