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

from platform import system
from classes.scheme_types.base_scheme import ColorScheme

from classes.color_scheme_strings import ColorSchemeStrings as Strings
from flux_bunny_utils.string_utils import StringUtils


#_______________________________________________________________________
class VsCodeScheme(ColorScheme):

  OUT_EXT: str = 'vscode.json'

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

    self.color_replacement_map: dict=\
    { 'BG__NORM' : StringUtils.int_to_hex6(self.background_color_)
    , 'BG__BOLD' : StringUtils.int_to_hex6(self.background_color_) #intense_ # TODO: Add BG__INTENSE)
    , 'FG__NORM' : StringUtils.int_to_hex6(self.foreground_color_)
    , 'FG__BOLD' : StringUtils.int_to_hex6(self.foreground_color_) #intense_ # TODO: Add FG__INTENSE)
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
