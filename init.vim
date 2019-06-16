if &compatible
  set nocompatible
endif
" Add the dein installation directory into runtimepath
set runtimepath+=~/.local/share/dein/repos/github.com/Shougo/dein.vim

if dein#load_state('~/.local/share/dein')
  call dein#begin('~/.local/share/dein')

  call dein#add('~/.local/share/dein/repos/github.com/Shougo/dein.vim')
  call dein#add('Shougo/deoplete.nvim')
  if !has('nvim')
    call dein#add('roxma/nvim-yarp')
    call dein#add('roxma/vim-hug-neovim-rpc')
  endif
  call dein#add('arcticicestudio/nord-vim')
  call dein#add('joshdick/onedark.vim')
  call dein#add('crusoexia/vim-monokai')
  call dein#add('mhartington/oceanic-next')
  call dein#add('rust-lang/rust.vim')

  call dein#end()
  call dein#save_state()
endif

call dein#add('Shougo/deoplete.nvim')
if !has('nvim')
  call dein#add('roxma/nvim-yarp')
  call dein#add('roxma/vim-hug-neovim-rpc')
endif
let g:deoplete#enable_at_startup = 1

if (has("termguicolors"))
    set termguicolors
endif

filetype plugin indent on
syntax enable
colorscheme OceanicNext

autocmd Filetype rust colorscheme onedark

:set tabstop=4
:set shiftwidth=4
:set expandtab
