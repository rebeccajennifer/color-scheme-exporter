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
#   Driver for program
#_______________________________________________________________________

import argparse

from classes.color_scheme_parser import ColorSchemeParser
from classes.color_scheme_parser import ParserStrings

from classes.scheme_types.gnome_scheme import GnomeScheme
from classes.scheme_types.mintty_scheme import MinttyScheme
from classes.scheme_types.konsole_scheme import KonsoleScheme
from classes.scheme_types.vscode_term_scheme import VsCodeTermScheme
from classes.scheme_types.vscode_scheme import VsCodeScheme
from classes.scheme_types.vim_scheme import VimScheme

from utilities.color_scheme_utils import GeneralUtils as Utils

SCHEME_MAP: dict =\
{ ParserStrings.GNOME_INPUT       : GnomeScheme
, ParserStrings.KONSOLE_INPUT     : KonsoleScheme
, ParserStrings.VSCODE_TERM_INPUT : VsCodeTermScheme
, ParserStrings.VSCODE_INPUT      : VsCodeScheme
, ParserStrings.MINTTY_INPUT      : MinttyScheme
, ParserStrings.VIM_INPUT         : VimScheme
}


#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()

#_______________________________________________________________________
if __name__ == '__main__':

  new_line(2)

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  ColorSchemeParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  scheme_types: list =\
  [ GnomeScheme
  #, KonsoleScheme
  , VsCodeTermScheme
  , VsCodeScheme
  , MinttyScheme
  ]

  if (args.scheme_type != ParserStrings.ALL_INPUT):
    SchemeType = SCHEME_MAP[args.scheme_type]

  if (args.default):
    args.scheme_type = ParserStrings.ALL_INPUT

  if (args.scheme_type != ParserStrings.ALL_INPUT):
    scheme_types = [SchemeType]

  for SchemeType in scheme_types:
    # Data in file overrides all other arguments
    if(args.file):
      color_scheme = SchemeType(
        args.out_dir, Utils.read_hex_color_json(args.file))

    else:
      color_scheme =\
        SchemeType(out_dir=args.out_dir)

    color_scheme.write_file()
    color_scheme.on_completion()

  color_scheme.print_color_scheme()
