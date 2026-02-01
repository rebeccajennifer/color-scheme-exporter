"_______________________________________________________________________
" Vim color file
" Maintainer:  Rebecca Rashkin <rebecca.jennifer.rabbit@gmail.com>
" Last Change: 2025 Oct  24
"_______________________________________________________________________
"_______________________________________________________________________
"        _   __   _   _ _   _   _   _         _
"   |   |_| | _  | | | V | | | | / |_/ |_| | /
"   |__ | | |__| |_| |   | |_| | \ |   | | | \_
"    _  _         _ ___  _       _ ___   _                    / /
"   /  | | |\ |  \   |  | / | | /   |   \                    (^^)
"   \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
"_______________________________________________________________________
"_______________________________________________________________________
"
"-----------------------------------------------------------------------
"   Copyright 2025, Rebecca Rashkin
"   -------------------------------
"   This code may be copied, redistributed, transformed, or built
"   upon in any format for educational, non-commercial purposes.
"
"   Please give me appropriate credit should you choose to use this
"   resource. Thank you :)
"-----------------------------------------------------------------------
"
"_______________________________________________________________________
"   //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\
"_______________________________________________________________________
"   DESCRIPTION
"   Base syntax highlighting file for color themes. Must be used in
"   conjunction with a colors definition file and a theme file.
"_______________________________________________________________________
"   NOTE
"_______________________________________________________________________
"   To find a token's highlight group, place your cursor on it and run:
"
"     :echo synIDattr(synID(line('.'), col('.'), 1), 'name')
"
"   The group name shows in the command area (bottom left).
"
"   If blank, the token isn't recognized as part of a highlight group.
"_______________________________________________________________________


"_______________________________________________________________________
exe ':hi Normal           ctermbg ='.cli_bg__norm 'guibg ='.gui_bg__norm
exe ':hi Normal           ctermfg ='.cli_fg__norm 'guifg ='.gui_fg__norm

exe ':hi NonText          ctermfg ='.cli_blu_norm 'guifg ='.gui_blu_norm

"_______________________________________________________________________
exe ':hi Cursor           ctermbg ='.cli_yel_norm 'guibg ='.gui_yel_norm
exe ':hi Cursor           ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm

"_______________________________________________________________________
" CursorLine: Enable with :set cursorline
" Underlines entire line where cursor is
"
" Option cursorline must be set for CursorLine* variables to take effect
"_______________________________________________________________________

" Option none disables the line
exe ':hi CursorLine       cterm   =  none           gui  =  none'
exe ':hi CursorLine       ctermbg ='.cli_bg__bold 'guibg ='.gui_blk_norm

" CursorLineNr: Sets color of current line
exe ':hi CursorLineNr     cterm   = bold           gui   =  bold'
exe ':hi CursorLineNr     ctermfg ='.cli_red_norm 'guifg ='.gui_red_norm

"exe ':hi CursorColumn     ctermbg ='.cli_000 'guibg ='.gui_000
"_______________________________________________________________________

" LineNr: Line number
exe ':hi LineNr           ctermfg ='.cli_fg__norm 'guifg ='.gui_fg__norm

"_______________________________________________________________________
" HIGHLIGHTED TEXT
"_______________________________________________________________________

" Visual: Text selection
exe ':hi Visual           cterm   =  bold          gui   =  bold'
exe ':hi Visual           cterm   =  bold          gui   =  bold'
exe ':hi Visual           ctermbg ='.cli_yel_norm 'guibg ='.gui_yel_norm
exe ':hi Visual           ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm

" Search: Highlighted text on search
exe ':hi Search           cterm   =  bold          gui   =  bold'
exe ':hi Search           ctermfg ='.cli_yel_norm 'guifg ='.gui_wht_norm
exe ':hi Search           ctermbg ='.cli_blk_norm 'guibg ='.gui_blk_norm

" Todo: TODO, FIXME
exe ':hi Todo             ctermbg ='.cli_bg__bold 'guibg ='.gui_bg__bold
exe ':hi Todo             ctermfg ='.cli_fg__norm 'guifg ='.gui_fg__norm

"_______________________________________________________________________
" CODE
"_______________________________________________________________________
"
exe ':hi Comment          ctermfg ='.cli_blk_bold 'guifg ='.gui_blk_bold
exe ':hi String           ctermfg ='.cli_mag_norm 'guifg ='.gui_cya_norm

" Special examples
"   .cpp : \n in strings, ()
exe ':hi Special          ctermfg ='.cli_yel_norm 'guifg ='.gui_yel_norm

" Statement examples
"   .cpp: sizeof
"   .vim: exe, let
exe ':hi Statement        ctermfg ='.cli_cya_norm 'guifg ='.gui_grn_norm

" Type examples
"   .cpp: int, class
"   .vim: Type, Search, Comment, Normal
exe ':hi Type             ctermfg ='.cli_mag_norm 'guifg ='.gui_mag_norm

" Constant examples
"   .cpp: 3 in 3 + i
"   .vim: 3 in ctermrg=3
exe ':hi Constant         ctermfg ='.cli_grn_norm 'guifg ='.gui_grn_norm

" MatchParen: Crnt & matching paren when one paren is under cursor
exe ':hi MatchParen       cterm   =  bold          gui   =  bold'
exe ':hi MatchParen       ctermbg ='.cli_blu_norm 'guibg ='.gui_blu_norm
exe ':hi MatchParen       ctermfg ='.cli_yel_norm 'guifg ='.gui_yel_norm

" PreProc examples
"   .cpp: #include, #define
exe ':hi PreProc          ctermfg ='.cli_blu_norm 'guifg ='.gui_blu_norm

" Operator examples
"   .cpp: + in 1 + 2
"   .vim: = in let foo = '0'
exe ':hi Operator         ctermfg ='.cli_red_norm 'guifg ='.gui_red_norm

" VimVar: Variables in vim script
"   .vim: a in let a = '0'
exe ':hi VimVar           ctermfg ='.cli_blu_norm 'guifg ='.gui_blu_norm


"_______________________________________________________________________
" Markdown

exe ':hi markdownH1       ctermfg ='.cli_red_norm 'guifg ='.gui_red_norm
exe ':hi markdownH2       ctermfg ='.cli_yel_norm 'guifg ='.gui_yel_norm
exe ':hi markdownH3       ctermfg ='.cli_grn_norm 'guifg ='.gui_grn_norm
exe ':hi markdownH4       ctermfg ='.cli_cya_norm 'guifg ='.gui_cya_norm

exe ':hi markdownH1       cterm   =  bold          gui   =   bold'
exe ':hi markdownH2       cterm   =  bold          gui   =   bold'
exe ':hi markdownH3       cterm   =  bold          gui   =   bold'
exe ':hi markdownH4       cterm   =  bold          gui   =   bold'

" markdownH#Delimiter: # symbols

exe ':hi markdownHeadingDelimiter ctermfg ='.cli_grn_norm 'guifg ='.gui_grn_norm

exe ':hi markdownH1Delimiter  ctermfg ='.cli_grn_norm 'guifg ='.gui_grn_norm
exe ':hi markdownH2Delimiter  ctermfg ='.cli_cya_norm 'guifg ='.gui_cya_norm
exe ':hi markdownH3Delimiter  ctermfg ='.cli_blu_norm 'guifg ='.gui_blu_norm
exe ':hi markdownH4Delimiter  ctermfg ='.cli_mag_norm 'guifg ='.gui_mag_norm

"_______________________________________________________________________
" These aren't working (?)
exe ':hi Identifier       ctermfg ='.cli_red_norm 'guifg ='.gui_blk_norm

" PreProc examples
"   .cpp: #define
exe ':hi Define           ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm

" Function examples
"   .py : happy in def happy(), int
exe ':hi Function         ctermfg ='.cli_cya_norm 'guifg ='.gui_red_norm
exe ':hi cFunction        ctermfg ='.cli_red_norm 'guifg ='.gui_red_norm

"_______________________________________________________________________
" StatusLine: footers for window panes
" Note: Background (bg) and foregroung (fg) values are flipped
"_______________________________________________________________________

" StatusLine: Footer for active pane when multiple windows open
exe ':hi StatusLine       ctermfg ='.cli_blu_norm 'guifg ='.gui_blu_norm
exe ':hi StatusLine       ctermbg ='.cli_blk_norm 'guibg ='.gui_blk_norm

" StatusLineNC: Footer for inactive (non current) window pane
exe ':hi StatusLineNC     ctermbg ='.cli_wht_norm 'guibg ='.gui_wht_norm
exe ':hi StatusLineNC     ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm

exe ':hi Statuslineterm   ctermfg ='.cli_yel_norm 'guifg ='.gui_yel_norm

" VertSplit: Divider between window panes
exe ':hi VertSplit        ctermbg ='.cli_cya_norm 'guibg ='.gui_blu_norm
exe ':hi VertSplit        ctermfg ='.cli_bg__bold 'guifg ='.gui_bg__bold

"_______________________________________________________________________
" VIM FUNCTIONALITY
"_______________________________________________________________________

" ModeMsg: Messages about current vim mode
"   *.*:  -- INSERT --, -- REPLACE --, -- VISUAL --
exe ':hi ModeMsg          ctermfg ='.cli_fg__norm 'guifg ='.gui_fg__norm
exe ':hi MoreMsg          ctermfg ='.cli_cya_norm 'guifg ='.gui_cya_norm

exe ':hi Error            ctermfg ='.cli_yel_norm 'guifg ='.gui_yel_norm
exe ':hi ErrorMsg         ctermbg ='.cli_red_norm 'guibg ='.gui_red_norm
exe ':hi ErrorMsg         ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm

"_______________________________________________________________________
" HIGHLIGHT GROUPS NOT IMPLEMENTED
"_______________________________________________________________________
"exe ':hi EndOfBuffer      ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi StatusLineTerm   ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi StatusLineTermNC ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi PmenuSel         ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi Pmenu            ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi PmenuSbar        ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi PmenuThumb       ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi TabLineSel       ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi TabLine          ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi TabLineFill      ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi ToolbarLine      ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi ToolbarButton    ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi SpecialKey       ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi QuickFixLine     ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi Folded           ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi FoldColumn       ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi SignColumn       ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi VisualNOS        ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi WarningMsg       ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi Question         ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi IncSearch        ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi WildMenu         ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi Underlined       ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi lCursor          ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi SpellBad         ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi SpellCap         ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi SpellLocal       ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi SpellRare        ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi Structure        ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi Directory        ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi Conceal          ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi Ignore           ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi Title            ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi DiffAdd          ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi DiffChange       ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi DiffText         ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm
"exe ':hi DiffDelete       ctermfg ='.cli_blk_norm 'guifg ='.gui_blk_norm

"_______________________________________________________________________
" VARIABLE DEFINITIONS
"_______________________________________________________________________
"_______________________________________________________________________
" 📄 General UI Elements
"
" Normal            : The main text area where editing occurs.
"
" NonText           : Characters that are not actually text, such as ~
"                     at the end of the buffer or trailing whitespace.
"
" EndOfBuffer       : The lines beyond the end of the buffer (often ~).
"
" StatusLine        : The status line of the current window (usually
"                     shows file name, mode, etc.).
"
" StatusLineNC      : Status lines of non-current windows.
"
" StatusLineTerm    : Terminal emulator version of the status line.
"
" StatusLineTermNC  : Terminal emulator version for non-current windows.
"
" VertSplit         : The vertical split separator between windows.
"
" LineNr            : Line numbers in the left column.
"
" CursorLineNr      : Line number of the cursor line (useful when
"                     highlighting the current line).
"
" CursorLine        : The line under the cursor (horizontal highlight).
"
" CursorColumn      : The column under the cursor (vertical highlight).
"
" ColorColumn       : Highlight column(s) (like at 80 chars for style
"                     guides).
"
" SignColumn        : Column used for signs (e.g. for GitGutter or
"                     diagnostics).
"
" Folded            : Folded text.
"
" FoldColumn        : Column showing fold levels.
"
" QuickFixLine      : The current selected quickfix list line.
"
" ToolbarLine       : Used for GUI toolbar background (rarely used).
"
" ToolbarButton     : Used for buttons in toolbars (GUI).
"
" TabLine           : The tab pages line when more than one tab page is
"                     open.
"
" TabLineSel        : The selected tab.
"
" TabLineFill       : The area after the last tab.
"
" Visual            : Visual mode selection.
"
" VisualNOS         : Visual mode when not owning the selection.
"
" MatchParen        : Highlight for matching parens.
"
" Conceal           : Hidden text shown with conceallevel > 0.
"
" Ignore            : Placeholder for ignored text (same fg and bg
"                     usually).
"
" ______________________________________________________________________
" 🗂 Menus & Popup
"
" Pmenu             : Popup menu (e.g. completion menu).
"
" PmenuSel          : Selected item in popup menu.
"
" PmenuSbar         : Scrollbar in popup menu.
"
" PmenuThumb        : Thumb (the draggable bar) of the popup menu
"                     scrollbar.
"
" WildMenu          : Wild menu (like tab-completion on command line).
"
" ______________________________________________________________________
" 🔁 Mode/Message/Interaction
"
" Cursor            : The character under the cursor (used in GUI).
"
" lCursor           : Same as above but for guicursor.
"
" ModeMsg           : Messages about mode (e.g. "-- INSERT --").
"
" WarningMsg        : Warning messages (e.g. :echohl WarningMsg).
"
" ErrorMsg          : Error messages (e.g. when a command fails).
"
" MoreMsg           : "Press ENTER" messages.
"
" Question          : Prompts like :confirm.
"
" ______________________________________________________________________
" 🔍 Search and Match
"
" Search            : Matches from / and ?.
"
" IncSearch         : While typing a search (incremental search).
"
" MatchParen        : Highlight of matching parenthesis, bracket, or
"                     brace.
"
" ______________________________________________________________________
" 🪧 Diagnostics & Spell Check
"
" Error             : Generic error highlight (can apply to code or
"                     messages).
"
" SpellBad          : Misspelled words.
"
" SpellCap          : Capitalization errors.
"
" SpellLocal        : Local spell check error.
"
" SpellRare         : Rare word warning.
"
" ______________________________________________________________________
" 🧠 Syntax Highlighting
"
" Comment           : Code comments.
"
" String            : String literals.
"
" Identifier        : Variable or constant names.
"
" VimVar            : Variables in Vim scripting
"
" Function          : Function or method names.
"
" Special           : Special characters or constructs (e.g. \n, @).
"
" Statement         : Control flow (e.g. if, for, while).
"
" Constant          : Numeric, character, boolean constants.
"
" PreProc           : Preprocessor directives (e.g. #define).
"
" Type              : Data types (int, float, etc.).
"
" Operator          : Operators (+, -, =, etc.).
"
" Define            : Macros or #define specifically.
"
" Structure         : Struct/union definitions.
"
" Directory         : Directory names in file lists.
"
" ______________________________________________________________________
" 📌 Miscellaneous
"
" Title             : Titles (e.g., window titles or headers).
"
" Underlined        : Text that is underlined.
"
" Todo              : Used for TODO, FIXME, etc. (visually highlighted).
"
" SpecialKey        : Special keyboard characters (e.g., ^I for Tab).
"
" Directory         : Directory names in netrw or command output.
"
" DiffAdd           : Lines added in a diff.
"
" DiffChange        : Changed lines in a diff.
"
" DiffText          : The actual changed text.
"
" DiffDelete        : Deleted lines in a diff.
"
" ______________________________________________________________________

