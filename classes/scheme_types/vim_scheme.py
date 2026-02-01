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
      Modifies self.color_replacement_map to include CLI color mappings.
    """

    Rgb = RgbColor

    super().populate_replacement_map()

    color_map: dict = self.color_replacement_map

    # Additional CLI colors
    color_map['BG__NORM_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['BG__NORM']))
    color_map['FG__NORM_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['FG__NORM']))
    color_map['BG__BOLD_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['BG__BOLD']))
    color_map['FG__BOLD_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['FG__BOLD']))
    color_map['BLK_NORM_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['BLK_NORM']))
    color_map['RED_NORM_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['RED_NORM']))
    color_map['GRN_NORM_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['GRN_NORM']))
    color_map['YEL_NORM_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['YEL_NORM']))
    color_map['BLU_NORM_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['BLU_NORM']))
    color_map['VIO_NORM_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['VIO_NORM']))
    color_map['CYA_NORM_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['CYA_NORM']))
    color_map['WHT_NORM_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['WHT_NORM']))
    color_map['BLK_BOLD_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['BLK_BOLD']))
    color_map['RED_BOLD_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['RED_BOLD']))
    color_map['GRN_BOLD_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['GRN_BOLD']))
    color_map['YEL_BOLD_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['YEL_BOLD']))
    color_map['BLU_BOLD_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['BLU_BOLD']))
    color_map['VIO_BOLD_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['VIO_BOLD']))
    color_map['CYA_BOLD_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['CYA_BOLD']))
    color_map['WHT_BOLD_CLI'] = str(Rgb.ansi_256_from_rgb(color_map['WHT_BOLD']))

    return
