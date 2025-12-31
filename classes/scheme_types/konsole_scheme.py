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
#   Konsole color scheme
#_______________________________________________________________________

# TODO need to fix to work with base class

from classes.rgb_color import RgbColor, RgbConst
from classes.scheme_types.base_scheme import ColorScheme

from utilities.color_scheme_utils import GeneralUtils as Utils


#_______________________________________________________________________
class KonsoleScheme(ColorScheme):
  """
  Used to generate a color scheme file for Konsole.
  """

  OUT_EXT: str = 'colorscheme'
  INTENSE_BOLD: str  = 'intense-bold'
  BACKGROUND_COLOR_INTENSE: str = 'background-color-intense'
  FOREGROUND_COLOR_INTENSE: str = 'foreground-color-intense'
  PALETTE_COLOR_COUNT: int = 8

  COMPLETION_TEXT: str =str (
    '\nUser created Konsole color themes are often saved to:'
    '\n~/.local/share/konsole/'
  )

  #_____________________________________________________________________
  def __init__(self, *arg):
    """
    Constructor, takes additional argument to base class.

    Parameters
    intense_bold - set intense colors to appear bold, presence in json
                   file input takes precedence
    """

    #___________________________________________________________________
    # Set class specific defaults
    #___________________________________________________________________
    self.intense_bold_ = True
    self.background_color_intense_: int = RgbConst.DEFAULT_BACKGROUND
    self.foreground_color_intense_: int = RgbConst.DEFAULT_FOREGROUND

    if (len(arg) and isinstance(arg[0], bool)):
      self.intense_bold_ = arg[0]
      arg = arg[1:len(arg)]

    super(KonsoleScheme, self).__init__(*arg)

    #___________________________________________________________________
    # Account for konsole specific parameters in json
    #___________________________________________________________________
    if (len(arg) and isinstance(arg[0], dict)):
      d: dict = arg[0]

      try:
        self.intense_bold_ = Utils.str_to_bool(d[self.INTENSE_BOLD])
      except:
        self.intense_bold_ = True

      try:
        self.background_color_intense_ =\
          Utils.str_hex_to_int(d[self.BACKGROUND_COLOR_INTENSE])
      except:
        self.background_color_intense_ =\
          d[self.BG_NORM_KEY]

      try:
        self.foreground_color_intense_ =\
          Utils.str_hex_to_int(d[self.FOREGROUND_COLOR_INTENSE])
      except:
        self.foreground_color_intense_ =\
          d[self.FG_NORM_KEY]
    #___________________________________________________________________

    self.normal_colors_: list[int] = self.palette_[0:8]
    self.intense_colors_: list[int] = self.palette_[8:16]

    self.construct_label_list()

    self.color_scheme_str_: str = self.create_color_scheme_str()

    return

  #_____________________________________________________________________
  def construct_label_list(self):
    """
    Construct the list of labels for color scheme.
    """

    self.label_list_: list[str] = ['Background', 'BackgroundIntense']

    for i in range(self.PALETTE_COLOR_COUNT):
      self.label_list_.append(f'Color{i}')
      self.label_list_.append(f'Color{i}Intense')

    self.label_list_.append('Foreground')
    self.label_list_.append('ForegroundIntense')

    return

  #_____________________________________________________________________
  # TODO URGENT account for scheme name
  #_____________________________________________________________________
  def create_simple_entry(self, rgb_color: int, label: str) -> str:
    """
    Creates color entry.

    Parameters
    rgb_color - 24 bit RGB color to represent
    label     - label in color scheme file

    Sample Output
    [Color2Intense]
    Bold=true
    Color=215,0,0
    """

    rgb_map: dict = RgbColor.get_rgb_from_hex(rgb_color)

    red: int = rgb_map[RgbConst.RED_STR]
    grn: int = rgb_map[RgbConst.GRN_STR]
    blu: int = rgb_map[RgbConst.BLU_STR]

    outstr = f'[{label}]'

    # Add Bold configuration if applicable
    if(self.intense_bold_ and ('Intense' in label)):
      outstr = f'{outstr}\nBold=true'

    outstr = f'{outstr}\nColor={red},{grn},{blu}\n\n'

    return outstr

  #_____________________________________________________________________
  def create_color_scheme_str(self) -> str:
    """
    Creates color scheme string to be printed to a file.
    """

    out_str: str = ''

    label_index: int = 0

    background_normal_str: str = self.create_simple_entry(
      rgb_color=self.background_color_
      , label=self.label_list_[label_index])

    label_index = label_index + 1

    background_intense_str: str = self.create_simple_entry(
      rgb_color=self.background_color_intense_
      , label=self.label_list_[label_index])

    label_index = label_index + 1

    out_str: str = f'{background_normal_str}{background_intense_str}'

    #___________________________________________________________________
    # Iterate through palette and append to out_str
    # Assumption that normal_colors_ and intense_colors_ are same size
    #___________________________________________________________________
    for i in range(len(self.normal_colors_)):

      color_normal_str: str = self.create_simple_entry(
        rgb_color=self.normal_colors_[i]
        , label=self.label_list_[label_index])

      label_index = label_index + 1

      color_intense_str: str = self.create_simple_entry(
        rgb_color=self.intense_colors_[i]
        , label=self.label_list_[label_index])

      label_index = label_index + 1

      out_str = f'{out_str}{color_normal_str}{color_intense_str}'
    #___________________________________________________________________

    foreground_normal_str: str = self.create_simple_entry(
      rgb_color=self.foreground_color_
      , label=self.label_list_[label_index])

    label_index = label_index + 1

    foreground_intense_str: str = self.create_simple_entry(
      rgb_color=self.foreground_color_intense_
      , label=self.label_list_[label_index])

    out_str: str =\
      f'{out_str}{foreground_normal_str}{foreground_intense_str}'\
      '[General]'\
      f'\nDescription={self.name_}'\
      '\nOpacity=1'\
      '\nWallpaper='

    return out_str
