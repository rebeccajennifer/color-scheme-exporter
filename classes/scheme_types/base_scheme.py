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
  ACCENT0_KEY     : str = "accent-color-0"
  ACCENT1_KEY     : str = "accent-color-1"
  ACCENT2_KEY     : str = "accent-color-2"
  CURSOR_COLOR    : str = 'cursor-color'
  PALETTE         : str = 'palette'

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
    , name: str = Strings.DEFAULT_NAME
    , out_dir: str = '.', *arg):

    self.cursor_color_  = RgbConst.DEFAULT_CURSOR_COL

    self.bg_norm_color_ = RgbConst.DEF_BG_NORM
    self.fg_norm_color_ = RgbConst.DEF_FG_NORM
    self.bg_bold_color_ = RgbConst.DEF_BG_BOLD
    self.fg_bold_color_ = RgbConst.DEF_FG_BOLD
    self.accent_color0_ = RgbConst.DEF_ACCENT0
    self.accent_color1_ = RgbConst.DEF_ACCENT1
    self.accent_color2_ = RgbConst.DEF_ACCENT2

    self.palette_       = RgbConst.DEFAULT_RGB_INT_LIST
    self.name_          = name
    self.is_dark_       = True

    #___________________________________________________________________
    # Default with no arguments
    #___________________________________________________________________
    if (not len(arg)):
      return

    #___________________________________________________________________
    if (isinstance(arg[0], dict)):
      self.construct_from_json(arg[0])

    #___________________________________________________________________
    if (isinstance(arg[0], int)):
        self.bg_norm_color_ = arg[0]

    #___________________________________________________________________
    if (len(arg) > 1):
      try:
        self.fg_norm_color_ = arg[1]
      except TypeError:
        pass

    #___________________________________________________________________
    # Third argument is assumed to be a string containing white space
    # separated hex int strings, used when command line input. E.g.
    # TODO add example
    #___________________________________________________________________
    if (len(arg) > 2):
      try:
        rgb_colors: str = arg[2]

        rgb_color_str_list: list[str] = rgb_colors.split()

        self.palette_ =\
          Utils.str_list_to_hex_list(rgb_color_str_list)

      except TypeError:
        pass

    self.out_file_name_: str =\
      f'{self.name_}.{self.OUT_EXT}'

    FileUtils.verify_dir(path.abspath(out_dir))

    self.out_file_path_ = path.join(out_dir, self.out_file_name_)
    self.out_file_path_ = path.abspath(self.out_file_path_)

    self.color_scheme_str_: str = self.create_color_scheme_str()

    return

  #_____________________________________________________________________
  def construct_from_json(self, input_dict: dict):
    """
    Constructs color scheme from dictionary created from json.
    """

    #___________________________________________________________________
    if ('name' in input_dict):
      # Ensure file names have no spaces
      self.name_ = input_dict['name'].replace(' ', '-')

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
    if (self.ACCENT0_KEY in input_dict):
      self.accent_color0_ =\
        StringUtils.str_hex_to_int(input_dict[self.ACCENT0_KEY])

    if (self.ACCENT1_KEY in input_dict):
      self.accent_color1_ =\
        StringUtils.str_hex_to_int(input_dict[self.ACCENT1_KEY])

    if (self.ACCENT2_KEY in input_dict):
      self.accent_color2_ =\
        StringUtils.str_hex_to_int(input_dict[self.ACCENT2_KEY])

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
  def create_color_scheme_str(self):
    """
    Must be implemented by derived classes.
    """
    return