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
#   Argument parser file
#_______________________________________________________________________

import argparse
from os import getcwd

from classes.color_scheme_strings import ColorSchemeStrings
from classes.rgb_color import RgbColor, RgbConst

from utilities.color_scheme_utils import GeneralUtils


#_______________________________________________________________________
class ParserStrings:

  PROGRAM_NAME: str =\
    'Color Scheme Creator'

  PROGRAM_DESC: str =\
    'This program creates color scheme files in the format of several '\
    'terminal programs.'

  PROGRAM_EPI:  str =\
    'This is the epilog to the help menu.'

  SCHEME_TYPE_HELP_DESC: str =\
    'Type of profile, e.g. Gnome, Konsole'

  GNOME_INPUT       : str = 'gnome'
  KONSOLE_INPUT     : str = 'konsole'
  VSCODE_TERM_INPUT : str = 'vscode-term'
  MINTTY_INPUT      : str = 'mintty'
  ALL_INPUT         : str = 'all'

  SCHEME_TYPES: list =\
    [ GNOME_INPUT
    , KONSOLE_INPUT
    , VSCODE_TERM_INPUT
    , MINTTY_INPUT
    , ALL_INPUT
    ]

  CMD_LINE_ENTRY_GROUP_TITLE: str =\
    'Command Line Color Entry'

  CMD_LINE_ENTRY_GROUP_DESC: str =\
    'Argument group for command line entry.'

  BACKGND_HELP_DESC: str =\
    'Background color.'

  FOREGND_HELP_DESC: str =\
    'Foreground color.'

  RGB_LIST_HELP_DESC: str =\
    'List of 16 RGB values corresponding to color indices 0 - 15.'

  OUT_FILE_HELP_DESC: str =\
    'Base name of ouput file. Do not include extension.'

  OUT_DIR_HELP_DESC: str =\
    'Directory path of output file.'

  COLOR_JSON_HELP_DESC: str =\
    'Path to json file containing the foreground, background, '\
    'and palette. Overrides '\
    f'{CMD_LINE_ENTRY_GROUP_TITLE} argument group.'\
    '\nExample:'\
    '\n  {   "intense-bold"              : "false"'\
    '\n    , "background-color"          : "0x282828"'\
    '\n    , "background-color-intense"  : "0x1c1c1c"'\
    '\n    , "foreground-color"          : "0xDF5f87"'\
    '\n    , "foreground-color-intense"  : "0xFF5f87"'\
    '\n    , "palette":["0x5f0000"'\
    '\n    , "0xFF5f00"'\
    '\n    , "0x5fFF00"'\
    '\n    , "0xFFFF5f"'\
    '\n    , "0x5f00FF"'\
    '\n    , "0xFF5fFF"'\
    '\n    , "0x5fFFFF"'\
    '\n    , "0xFFFFFF"'\
    '\n    , "0x5f0000"'\
    '\n    , "0xFF5f00"'\
    '\n    , "0x5fFF00"'\
    '\n    , "0xFFFF5f"'\
    '\n    , "0x5f00FF"'\
    '\n    , "0xFF5fFF"'\
    '\n    , "0x5fFFFF"'\
    '\n    , "0xFFFFFF"'\
    '\n  ]'\
    '\n}'\

  DEFAULT_DESC: str =\
    'Select to use default color profile:'\
    f'{RgbColor.int_list_hex_str(RgbConst.DEFAULT_RGB_INT_LIST)}'

  COLOR_RANGE: str = '{0x000000-0xFFFFFF}'

  DEFAULT_NAME: str = ColorSchemeStrings.DEFAULT_NAME


#_______________________________________________________________________
class ColorSchemeParser:

  #_______________________________________________________________________
  def init_parser(parser: argparse.ArgumentParser) -> None:
    """
    Initializes the argument parser.
    """
    parser.prog = ParserStrings.PROGRAM_NAME
    parser.epilog = ParserStrings.PROGRAM_EPI
    parser.description = ParserStrings.PROGRAM_DESC

    parser.add_argument( '--scheme_type'
      , '-s'
      , help=ParserStrings.SCHEME_TYPE_HELP_DESC
      , action='store'
      , type=str
      , required=False
      , default=ParserStrings.ALL_INPUT
      , choices=ParserStrings.SCHEME_TYPES
    )

    # Add type, move strings to class
    cmd_line_group = parser.add_argument_group(\
      ParserStrings.CMD_LINE_ENTRY_GROUP_TITLE
       , ParserStrings.CMD_LINE_ENTRY_GROUP_DESC)

    cmd_line_group.add_argument('--background_color'
      , '-bg'
      , help=ParserStrings.BACKGND_HELP_DESC
      , action='store'
      , type=GeneralUtils.str_hex_to_int
      , required=False
      , default=RgbConst.DEFAULT_BACKGROUND
      , choices=range(0, GeneralUtils.MAX_COLOR + 1)
      , metavar=ParserStrings.COLOR_RANGE
    )

    cmd_line_group.add_argument('--foreground_color'
      , '-fg'
      , help=ParserStrings.FOREGND_HELP_DESC
      , action='store'
      , type=GeneralUtils.str_hex_to_int
      , required=False
      , default=RgbConst.DEFAULT_FOREGROUND
      , choices=range(0, GeneralUtils.MAX_COLOR + 1)
      , metavar=ParserStrings.COLOR_RANGE
    )

    cmd_line_group.add_argument('--rgb_list'
      , '-rgb'
      , help=ParserStrings.RGB_LIST_HELP_DESC
      , action='store'
      , type=str
      , required=False
      , default=RgbConst.DEFAULT_RGB_STR_LIST
    )

    parser.add_argument('--name'
      , '-n'
      , help=ParserStrings.OUT_FILE_HELP_DESC
      , action='store'
      , type=str
      , required=False
      , default=ParserStrings.DEFAULT_NAME
    )

    parser.add_argument('--out_dir'
      , '-o'
      , help=ParserStrings.OUT_DIR_HELP_DESC
      , action='store'
      , type=str
      , default=getcwd()
    )

    parser.add_argument('--file'
      , '-f'
      , help=ParserStrings.COLOR_JSON_HELP_DESC
      , action='store'
      , type=str
      , required=False
    )

    parser.add_argument('--default'
      , '-d'
      , help=ParserStrings.DEFAULT_DESC
      , action='store_true'
      , required=False
    )

    return


