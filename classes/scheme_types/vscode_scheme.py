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
  TEMPLATE_PATH: str = 'templates/flux-bunny-template.json'

  #_____________________________________________________________________
  def populate_replacement_map(self) -> str:
    """
    Populate map of color labels in template with values from
    color scheme.
    """

    key_bg_0 = RgbColor.make_background_color(self.accent_color0_, is_dark=self.is_dark_)
    key_bg_1 = RgbColor.make_background_color(self.accent_color1_, is_dark=self.is_dark_)
    key_bg_2 = RgbColor.make_background_color(self.accent_color2_, is_dark=self.is_dark_)

    key_fg_0 = RgbColor.make_foreground_color(self.accent_color0_, is_dark=self.is_dark_)
    key_fg_1 = RgbColor.make_foreground_color(self.accent_color1_, is_dark=self.is_dark_)
    key_fg_2 = RgbColor.make_foreground_color(self.accent_color2_, is_dark=self.is_dark_)

    self.color_replacement_map: dict=\
    { 'BG__NORM' : StringUtils.int_to_hex6(self.bg_norm_color_)
    , 'BG__BOLD' : StringUtils.int_to_hex6(self.bg_bold_color_)
    , 'FG__NORM' : StringUtils.int_to_hex6(self.fg_norm_color_)
    , 'FG__BOLD' : StringUtils.int_to_hex6(self.fg_bold_color_)
    , 'KEY_BG_0' : StringUtils.int_to_hex6(key_bg_0)
    , 'KEY_BG_1' : StringUtils.int_to_hex6(key_bg_1)
    , 'KEY_BG_2' : StringUtils.int_to_hex6(key_bg_2)
    , 'KEY_FG_0' : StringUtils.int_to_hex6(key_fg_0)
    , 'KEY_FG_1' : StringUtils.int_to_hex6(key_fg_1)
    , 'KEY_FG_2' : StringUtils.int_to_hex6(key_fg_2)
    , 'BLK_NORM' : StringUtils.int_to_hex6(self.palette_[0])
    , 'RED_NORM' : StringUtils.int_to_hex6(self.palette_[1])
    , 'GRN_NORM' : StringUtils.int_to_hex6(self.palette_[2])
    , 'YEL_NORM' : StringUtils.int_to_hex6(self.palette_[3])
    , 'BLU_NORM' : StringUtils.int_to_hex6(self.palette_[4])
    , 'VIO_NORM' : StringUtils.int_to_hex6(self.palette_[5])
    , 'CYA_NORM' : StringUtils.int_to_hex6(self.palette_[6])
    , 'WHT_NORM' : StringUtils.int_to_hex6(self.palette_[7])
    , 'BLK_BOLD' : StringUtils.int_to_hex6(self.palette_[8])
    , 'RED_BOLD' : StringUtils.int_to_hex6(self.palette_[9])
    , 'GRN_BOLD' : StringUtils.int_to_hex6(self.palette_[10])
    , 'YEL_BOLD' : StringUtils.int_to_hex6(self.palette_[11])
    , 'BLU_BOLD' : StringUtils.int_to_hex6(self.palette_[12])
    , 'VIO_BOLD' : StringUtils.int_to_hex6(self.palette_[13])
    , 'CYA_BOLD' : StringUtils.int_to_hex6(self.palette_[14])
    , 'WHT_BOLD' : StringUtils.int_to_hex6(self.palette_[15])
    }

  #_____________________________________________________________________
  def create_color_scheme_str(self) -> str:
    """
    Creates color scheme string to be printed to a file.
    """

    self.populate_replacement_map()

    #_______________________________________________________________
    # Load template file.
    #_______________________________________________________________
    with open(self.TEMPLATE_PATH, 'r') as file:
      text: str = file.read()

    #_______________________________________________________________
    # Replace color labels.
    #_______________________________________________________________

    for key in self.color_replacement_map:
      value: str = self.color_replacement_map[key]

      label_str: str = f'#{key}'
      text = text.replace(label_str, f'#{value}')

    out_str: str = text


    return out_str
