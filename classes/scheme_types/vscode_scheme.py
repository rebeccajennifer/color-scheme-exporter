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
class VsCodeScheme(ColorScheme):

  OUT_EXT: str = 'json'

  COMPLETION_TEXT: str =str (
    '\nFollow instructions here for instructions on how to implement'
    ' a custom color scheme in VSCode:'
    '\nhttps://rebeccajennifer.com/reference/color-scheme__reference/vscode-color.html'
    '\n'
  )

  #_____________________________________________________________________
  # Mapping of input key names to color label names in template
  #_____________________________________________________________________
  TEMPLATE_PATH: str = 'templates/vscode/flux-bunny-template.json'

  #_____________________________________________________________________
  def populate_replacement_map(self) -> str:
    """
    Populate map of color labels in template with values from
    color scheme.
    """

    super().populate_replacement_map()

    key_bg_0 = RgbColor.make_background_color(self.accent_color0_, is_dark=self.is_dark_)
    key_bg_1 = RgbColor.make_background_color(self.accent_color1_, is_dark=self.is_dark_)
    key_bg_2 = RgbColor.make_background_color(self.accent_color2_, is_dark=self.is_dark_)

    key_fg_0 = RgbColor.make_foreground_color(self.accent_color0_, is_dark=self.is_dark_)
    key_fg_1 = RgbColor.make_foreground_color(self.accent_color1_, is_dark=self.is_dark_)
    key_fg_2 = RgbColor.make_foreground_color(self.accent_color2_, is_dark=self.is_dark_)

    color_map: dict = self.str_replace_map

    color_map['KEY_BG_0'] =  StringUtils.int_to_hex6(key_bg_0)
    color_map['KEY_BG_1'] =  StringUtils.int_to_hex6(key_bg_1)
    color_map['KEY_BG_2'] =  StringUtils.int_to_hex6(key_bg_2)
    color_map['KEY_FG_0'] =  StringUtils.int_to_hex6(key_fg_0)
    color_map['KEY_FG_1'] =  StringUtils.int_to_hex6(key_fg_1)
    color_map['KEY_FG_2'] =  StringUtils.int_to_hex6(key_fg_2)

    return
