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
#   Collection of strings used in color_scheme_designer.
#_______________________________________________________________________

from classes.rgb_color import RgbConst, RgbColor
from utilities.color_scheme_utils import GeneralUtils as Utils

class ColorSchemeStrings:

  LINE: str =\
    '________________________________________________________________'

  CONTINUE: str =\
    '\nPress enter to continue.'\
    f'{LINE}'\
    '\n'

  OUTPUT_STR: str =\
    '\nThe following text will be printed to the output file: '\
    '\n'

  DEFAULT_NAME: str =\
    'color-scheme-name'


#_______________________________________________________________________
class ErrorStrings:
  ERROR_STR: str =\
    'ERROR:'

  INVALID_ENTRY: str =\
    f'{ERROR_STR} Invalid argument input.'\
    '\n'

  INVALID_DIR: str =\
    f'{ERROR_STR} Output directory does not exist. File will be '\
    'created in cwd.'\
    '\n'
