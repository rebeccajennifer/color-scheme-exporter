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
#   GNOME color scheme
#_______________________________________________________________________

from classes.scheme_types.base_scheme import ColorScheme
from classes.rgb_color import RgbConst, RgbColor


#_______________________________________________________________________
class GnomeScheme(ColorScheme):
  """
  Used to generate a color scheme file for GNOME Terminal.
  """

  OUT_EXT: str = 'dconf'

  COMPLETION_TEXT: str =str (
    '\nGNOME terminal themes are often saved to:'
    '\n~/.themes'
  )

  #_____________________________________________________________________
  def create_color_entry(rgb_map: dict) -> str:

    red: int = rgb_map[RgbConst.RED_STR]
    grn: int = rgb_map[RgbConst.GRN_STR]
    blu: int = rgb_map[RgbConst.BLU_STR]

    out_str: str =\
      f"'rgb({red}, {grn}, {blu})'"

    return out_str

  #_____________________________________________________________________
  def create_color_scheme_str(self) -> str:
    """
    Creates Gnome color scheme string to be printed to a file.
    """

    BACKGND: str = ColorScheme.BG_NORM_KEY
    FOREGND: str = ColorScheme.FG_NORM_KEY
    PALETTE: str = ColorScheme.PALETTE

    backgnd: dict = RgbColor.get_rgb_from_hex(self.background_color_)
    foregnd: dict = RgbColor.get_rgb_from_hex(self.foreground_color_)

    out_str: str = \
      '[/]'\
      f'\n{BACKGND}={GnomeScheme.create_color_entry(backgnd)}'\
      f'\n{FOREGND}={GnomeScheme.create_color_entry(foregnd)}'\
      f'\n{PALETTE}=[{self.create_palette_str()}]'

    return out_str

  #_____________________________________________________________________
  def create_palette_str(self) -> str:
    """
    Creates string for color palette.
    """

    out_str: str = ''

    palette: list[int] = self.palette_

    for i in range(len(palette)):
      color: int = palette[i]
      rgb_dict: dict = RgbColor.get_rgb_from_hex(color)
      color_entry: str = GnomeScheme.create_color_entry(rgb_dict)

      out_str = f'{out_str}{color_entry}'

      if (i != len(palette) - 1):
        out_str = f'{out_str},'

    return out_str
