if &compatible
    set nocompatible
endif

:set tabstop=4
:set shiftwidth=4
:set expandtab

set runtimepath+=~/.cache/dein/repos/github.com/Shougo/dein.vim

if dein#load_state('~/.cache/dein')
  call dein#begin('~/.cache/dein')

  call dein#add('~/.cache/dein/repos/github.com/Shougo/dein.vim')
  call dein#add('itchyny/lightline.vim')
  call dein#add('Shougo/deoplete.nvim')
  call dein#add('drewtempelmeyer/palenight.vim')
  call dein#add('kaicataldo/material.vim')
  call dein#add('arcticicestudio/nord-vim')
  call dein#add('rust-lang/rust.vim')
  call dein#add('dense-analysis/ale')
  call dein#end()
  call dein#save_state()
endif

if (has('termguicolors'))
    set termguicolors
endif

let g:deoplete#enable_at_startup = 1
let g:ale_linters = {'rust' : ['rls']}
let g:lightline = {
      \ 'colorscheme': 'one',
      \ }

colorscheme palenight
filetype plugin indent on
syntax enable
