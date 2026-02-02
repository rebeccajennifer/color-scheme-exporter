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
#   Visual Studio Code color scheme
#_______________________________________________________________________

from classes.scheme_types.base_scheme import ColorScheme
from classes.rgb_color import RgbColor

from flux_bunny_utils.string_utils import StringUtils


#_______________________________________________________________________
class VimScheme(ColorScheme):

  OUT_EXT: str = 'vim'

  COMPLETION_TEXT: str =str (
    '\nFollow instructions here for instructions on how to implement'
    ' a custom color scheme in Vim:'
    '\nhttps://rebeccajennifer.com/reference/color-scheme__reference/vim-color.html'
    '\n'
  )

  #_____________________________________________________________________
  # Mapping of input key names to color label names in template
  #_____________________________________________________________________
  TEMPLATE_PATH: str = 'templates/vim/flux-bunny-template.vim'

  #_____________________________________________________________________
  def populate_replacement_map(self) -> str:
    """
    Populate map of color labels in template with values from
    color scheme. Added additional CLI colors.

    Side Effects:
      Modifies self.str_replace_map to include CLI color mappings.
    """

    Rgb = RgbColor

    super().populate_replacement_map()

    is_dark_str: str = 'dark' if self.is_dark_ else 'light'

    mappy: dict = self.str_replace_map

    # Additional CLI colors
    mappy['NAME']         = self.name_
    mappy['LITE_OR_DARK'] = is_dark_str

    mappy['BG__CLI_NORM'] = str(Rgb.rgb_to_ansi256(mappy['BG__NORM']))
    mappy['FG__CLI_NORM'] = str(Rgb.rgb_to_ansi256(mappy['FG__NORM']))
    mappy['BG__CLI_BOLD'] = str(Rgb.rgb_to_ansi256(mappy['BG__BOLD']))
    mappy['FG__CLI_BOLD'] = str(Rgb.rgb_to_ansi256(mappy['FG__BOLD']))

    mappy['BLK_CLI_NORM'] = str(Rgb.rgb_to_ansi256(mappy['BLK_NORM']))
    mappy['RED_CLI_NORM'] = str(Rgb.rgb_to_ansi256(mappy['RED_NORM']))
    mappy['GRN_CLI_NORM'] = str(Rgb.rgb_to_ansi256(mappy['GRN_NORM']))
    mappy['YEL_CLI_NORM'] = str(Rgb.rgb_to_ansi256(mappy['YEL_NORM']))
    mappy['BLU_CLI_NORM'] = str(Rgb.rgb_to_ansi256(mappy['BLU_NORM']))
    mappy['VIO_CLI_NORM'] = str(Rgb.rgb_to_ansi256(mappy['VIO_NORM']))
    mappy['CYA_CLI_NORM'] = str(Rgb.rgb_to_ansi256(mappy['CYA_NORM']))
    mappy['WHT_CLI_NORM'] = str(Rgb.rgb_to_ansi256(mappy['WHT_NORM']))
    mappy['BLK_CLI_BOLD'] = str(Rgb.rgb_to_ansi256(mappy['BLK_BOLD']))
    mappy['RED_CLI_BOLD'] = str(Rgb.rgb_to_ansi256(mappy['RED_BOLD']))
    mappy['GRN_CLI_BOLD'] = str(Rgb.rgb_to_ansi256(mappy['GRN_BOLD']))
    mappy['YEL_CLI_BOLD'] = str(Rgb.rgb_to_ansi256(mappy['YEL_BOLD']))
    mappy['BLU_CLI_BOLD'] = str(Rgb.rgb_to_ansi256(mappy['BLU_BOLD']))
    mappy['VIO_CLI_BOLD'] = str(Rgb.rgb_to_ansi256(mappy['VIO_BOLD']))
    mappy['CYA_CLI_BOLD'] = str(Rgb.rgb_to_ansi256(mappy['CYA_BOLD']))
    mappy['WHT_CLI_BOLD'] = str(Rgb.rgb_to_ansi256(mappy['WHT_BOLD']))

    return
