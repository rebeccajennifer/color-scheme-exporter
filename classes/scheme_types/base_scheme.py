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
#   Base class for color schemes
#_______________________________________________________________________

import re

from os import path

from classes.color_scheme_strings import ColorSchemeStrings as Strings
from classes.rgb_color import RgbColor
from classes.rgb_color import RgbConst
from utilities.color_scheme_utils import GeneralUtils as Utils
from flux_bunny_utils.file_utils import FileUtils
from flux_bunny_utils.string_utils import StringUtils


#_______________________________________________________________________
class ColorScheme():
  """
  Contains base functionality to generate color schemes. This class
  cannot be used on its own - it must be inherited by a derived class.
  """

  BG_NORM_KEY     : str = 'background-color'
  BG_BOLD_KEY     : str = 'background-color-intense'
  FG_NORM_KEY     : str = 'foreground-color'
  FG_BOLD_KEY     : str = 'foreground-color-intense'
  KEY_BG0_KEY     : str = 'accent-color-0'
  KEY_BG1_KEY     : str = 'accent-color-1'
  KEY_BG2_KEY     : str = 'accent-color-2'
  CURSOR_COLOR    : str = 'cursor-color'
  PALETTE         : str = 'palette'
  NAME            : str = 'name'
  MODE            : str = 'mode'
  TEMPLATE_PATH   : str = None

  PREVIEW: str = str(
    f'\n{Strings.LINE}'
    f'\n{Strings.LINE}'
    '\n Your Color Scheme'
    '\n'
  )
  ALT_PREV: str = str(
    '\n-------------------------'
    '\n Alternative Backgrounds'
    '\n'
  )

  COMPLETION_TEXT: str = Strings.OUTPUT_STR

  #_____________________________________________________________________
  def __init__(self
    , out_dir: str = '.'
    , cfg = None):

    self.cursor_color_  = RgbConst.DEF_CRSR_BG

    self.bg_norm_color_ = RgbConst.DEF_BG_NORM
    self.fg_norm_color_ = RgbConst.DEF_FG_NORM
    self.bg_bold_color_ = RgbConst.DEF_BG_BOLD
    self.fg_bold_color_ = RgbConst.DEF_FG_BOLD

    self.accent_color0_ = RgbConst.DEF_ACCENT0
    self.accent_color1_ = RgbConst.DEF_ACCENT1
    self.accent_color2_ = RgbConst.DEF_ACCENT2

    self.palette_       = RgbConst.DEFAULT_RGB_INT_LIST
    self.name_          = 'theme-name'
    self.is_dark_       = True

    self.str_replace_map: dict = {}

    #___________________________________________________________________
    if (isinstance(cfg, dict)):
      self.construct_from_json(cfg)

    self.out_file_name_: str =\
      f'{self.name_}.{self.OUT_EXT}'

    FileUtils.verify_dir(path.abspath(out_dir))

    self.out_file_path_ = path.join(out_dir, self.out_file_name_)
    self.out_file_path_ = path.abspath(self.out_file_path_)

    self.color_scheme_str_: str = self.create_color_scheme_str()

    return

  #_____________________________________________________________________
  def construct_from_json(self, input_dict: dict) -> None:
    """
    Constructs color scheme from dictionary created from json.
    """
    if (self.MODE in input_dict):
      self.is_dark_ = True if input_dict['mode'] == 'dark' else False

    #___________________________________________________________________
    if (self.NAME in input_dict):
      # Ensure file names have no spaces
      self.name_ = input_dict[self.NAME].replace(' ', '-').lower()

    #___________________________________________________________________
    # Set background
    #___________________________________________________________________
    if (self.BG_NORM_KEY in input_dict):
      self.bg_norm_color_ =\
        StringUtils.str_hex_to_int(input_dict[self.BG_NORM_KEY])

    if (self.BG_BOLD_KEY in input_dict):
      self.bg_bold_color_ =\
        StringUtils.str_hex_to_int(input_dict[self.BG_BOLD_KEY])

    #___________________________________________________________________
    # Set foreground
    #___________________________________________________________________
    if (self.FG_NORM_KEY in input_dict):
      self.fg_norm_color_ =\
        StringUtils.str_hex_to_int(input_dict[self.FG_NORM_KEY])

    if (self.FG_BOLD_KEY in input_dict):
      self.fg_bold_color_ =\
        StringUtils.str_hex_to_int(input_dict[self.FG_BOLD_KEY])

    #___________________________________________________________________
    # Set accent colors
    #___________________________________________________________________
    if (self.KEY_BG0_KEY in input_dict):
      self.accent_color0_ =\
        StringUtils.str_hex_to_int(input_dict[self.KEY_BG0_KEY])

    if (self.KEY_BG1_KEY in input_dict):
      self.accent_color1_ =\
        StringUtils.str_hex_to_int(input_dict[self.KEY_BG1_KEY])

    if (self.KEY_BG2_KEY in input_dict):
      self.accent_color2_ =\
        StringUtils.str_hex_to_int(input_dict[self.KEY_BG2_KEY])

    #___________________________________________________________________
    if (self.PALETTE in input_dict):
      color_palette: list = input_dict[self.PALETTE]

      if (len(color_palette)):

        # Assumption that color palette is list of hex strings
        if (isinstance(color_palette[0], str)):
          self.palette_ =\
          Utils.str_list_to_hex_list(color_palette)

        #_______________________________________________________________
        # TODO modify function to take other types of dicts
        #      currently shouldn't ever enter this branch
        #_______________________________________________________________
        # Assumption that color palette is list of ints
        elif (isinstance(color_palette[0], int)):
          self.palette_ = color_palette

    return

  #_____________________________________________________________________
  def write_file(self) -> None:
    """
    Writes color scheme string to file.

    Parameters
    out_dir - path to directory
    """

    f = open(self.out_file_path_, 'w')
    f.write(self.color_scheme_str_)
    f.close()

    return

  #_____________________________________________________________________
  def print_color_scheme(self) -> None:
    """
    Prints color scheme to console as colored text.
    """

    bg: int = self.bg_norm_color_

    # Flag to determine if background color is light or dark
    is_lite_bg: bool = self.bg_norm_color_ >= 0x808080

    if (is_lite_bg):
      greyscale_list: list = RgbConst.ANSI_256_LITE_GREYS
    else:
      greyscale_list: list = RgbConst.ANSI_256_DARK_GREYS

    print(self.PREVIEW)

    TABLE_LINE: str = '\n' + (76 * '-')

    # Print table header
    header: str = str(
      TABLE_LINE +
      '\n Color    | Selected |              Color Scheme Preview with'
      '\n Scheme   | Backgrnd |               Alternative Backgrounds'
      + TABLE_LINE +
      '\n RGB Vals |'
    )

    header += RgbColor.construct_color_print_str\
      ( text=f' 0x{self.bg_norm_color_:06x} '
      , fg=self.fg_norm_color_
      , bg=bg
      )

    bg_color_list: list = [self.bg_norm_color_]

    # Make an abbreviated list
    for i in range(0, len(greyscale_list)):
      if (i % 3 == 0):
        bg_color_list.append(greyscale_list[i])


    for color in bg_color_list[1:len(bg_color_list)]:
      header += '|' + RgbColor.construct_color_print_str\
        ( text=f' 0x{color:06x} '
        , fg=self.fg_norm_color_
        , bg=color
        )

    header +='\n----------'

    for i in range(len(bg_color_list)):
      header += '-----------'
    print(header)

    colored_text: str = ''

    #___________________________________________________________________
    for i in range(0, len(self.palette_)):
      crnt_color: int = self.palette_[i]

      colored_text += RgbColor.construct_color_print_str\
        ( text=f' 0x{crnt_color:06x} '
        , fg=crnt_color
        )

      for grey in bg_color_list:
        colored_text += '|'

        colored_text += RgbColor.construct_color_print_str\
        ( text=f' Color {i:2d} '
        , fg=crnt_color
        , bg=grey
        )

      colored_text += '\n'

    print(colored_text)

    return

  #_____________________________________________________________________
  def on_completion(self):
    """
    Prints upon completion.
    """

    completion_text: str = str (
      f'\n{Strings.LINE}'
      f'\n{Strings.OUTPUT_STR}'
      f'\n{self.out_file_path_}'
      f'\n{Strings.LINE}'
      f'\n'
      f'\n{self.color_scheme_str_}'
      f'\n{Strings.LINE}'
      f'\n{self.COMPLETION_TEXT}'
    )

    print(completion_text)

  #_____________________________________________________________________
  def populate_replacement_map(self) -> str:
    """
    Populate map of color labels in template with values from
    color scheme. Used by classes that have template files.
    """

    self.str_replace_map: dict=\
    { 'BG__NORM' : StringUtils.int_to_hex6(self.bg_norm_color_)
    }

    self.str_replace_map: dict=\
    { 'BG__NORM' : StringUtils.int_to_hex6(self.bg_norm_color_)
    , 'FG__NORM' : StringUtils.int_to_hex6(self.fg_norm_color_)
    , 'BG__BOLD' : StringUtils.int_to_hex6(self.bg_bold_color_)
    , 'FG__BOLD' : StringUtils.int_to_hex6(self.fg_bold_color_)
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

    return

  #_____________________________________________________________________
  def create_color_scheme_str(self) -> str:
    """
    Creates color scheme string to be printed to a file.
    Used by classes that have template files.
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
    for key in self.str_replace_map:
      value = self.str_replace_map[key]
      text = text.replace(key, value)
      # Replace whole word only
      # Does not currently handle properties in vscode theme
      #pattern = fr'\b{re.escape(key)}\b'
      #text = re.sub(pattern, value, text)

    out_str: str = text


    return out_str
