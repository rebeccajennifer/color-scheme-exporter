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
#   Replaces color labels in a VSCode template file with actual color
#   values.
#_______________________________________________________________________

from os import path

is_dark: bool = True

profile_name: str =\
  'flux-bunny-dark.json' if is_dark else 'flux-bunny-lite.json'

# TODO: Add command line arguments for template file and output file.
# TODO: Add option for dark vs light color scheme.
# TODO: Read from input json file
# TODO: Error handling for file read/write
def get_color_label_map() -> dict:
  """
  Returns a mapping of color labels to their RGB integer values.
  """

  color_label_map_dark: dict =\
  { 'FG__NORM': 'c6c6c6'
  , 'BG__NORM': '262626'
  , 'BG__BOLD': '1c1c1c'

  , 'BLK_NORM': '1c1c1c'
  , 'RED_NORM': 'd787af'
  , 'GRN_NORM': 'afd787'
  , 'YEL_NORM': 'ffaf87'
  , 'BLU_NORM': '87afd7'
  , 'VIO_NORM': 'af87d7'
  , 'CYA_NORM': '87d7af'
  , 'WHT_NORM': 'd7d7d7'
  , 'BLK_BOLD': '878787'
  , 'RED_BOLD': 'ff5f87'
  , 'GRN_BOLD': '87af5f'
  , 'YEL_BOLD': 'ffd787'
  , 'BLU_BOLD': '00afd7'
  , 'VIO_BOLD': 'af5faf'
  , 'CYA_BOLD': '5fafaf'
  , 'WHT_BOLD': 'eeeeee'
  }

  color_label_map_lite: dict =\
  { 'FG__NORM': '262626'
  , 'BG__NORM': 'e4e4e4'
  , 'BG__BOLD': 'dadada'

  , 'BLK_NORM': '121212'
  , 'RED_NORM': 'af005f'
  , 'GRN_NORM': '008700'
  , 'YEL_NORM': 'd75f00'
  , 'BLU_NORM': '005f87'
  , 'VIO_NORM': '870087'
  , 'CYA_NORM': '008787'
  , 'WHT_NORM': '878787'
  , 'BLK_BOLD': '262626'
  , 'RED_BOLD': 'd75f87'
  , 'GRN_BOLD': '0087af'
  , 'YEL_BOLD': 'd78700'
  , 'BLU_BOLD': '005faf'
  , 'VIO_BOLD': '875f87'
  , 'CYA_BOLD': '005f5f'
  , 'WHT_BOLD': 'afafaf'
  }

  if is_dark:
    return color_label_map_dark
  else:
    return color_label_map_lite

if __name__ == '__main__':

  color_label_map: dict = get_color_label_map()

  #_______________________________________________________________
  # File paths.
  #_______________________________________________________________

  script_dir: str = path.dirname(path.abspath(__file__))

  template_file: str = path.join(script_dir
    , 'templates'
    , 'flux-bunny-template.json'
  )

  output_fp: str = '.'

  #_______________________________________________________________
  # Load template file.
  #_______________________________________________________________
  with open(template_file, 'r') as file:
    text: str = file.read()

  #print(text)

  #_______________________________________________________________
  # Replace color labels.
  #_______________________________________________________________

  for key in color_label_map:
    value: str = color_label_map[key]

    label_str: str = f'#{key}'
    text = text.replace(label_str, f'#{value}')

  out_file: str = path.join('/home'
    , 'flux'
    , '.vscode'
    , 'extensions'
    , 'flux-bunny-themes'
    , profile_name
    )

  with open(out_file, 'w') as file:
    file.write(text)
