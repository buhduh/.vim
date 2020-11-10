syntax on
set ignorecase
set smartcase
set backspace=indent,eol,start
set number
set shiftwidth=2
set tabstop=2
set expandtab
set smarttab
set ruler
set smartindent

execute pathogen#infect()

augroup vimrc
  autocmd! vimrc
  autocmd BufRead,BufNewFile *.cpp,*.cc,*.h,*.c,*.hpp,Makefile setlocal shiftwidth=4 tabstop=4 noexpandtab
  autocmd BufRead,BufNewFile * call vim_init#Init()
  autocmd FileType c,cpp,h,hpp source ~/.vim/syntax/vulkan1.0.vim
augroup END

let mapleader = " "

"map <C-n> :NERDTreeToggle<CR>
map <C-n> <plug>NERDTreeTabsToggle<CR>
map <silent> <leader>c :!clear<CR>
"map <silent> <leader>s :call stupid_brackets#MatchitRuby()<CR>

"folding macros for golang
"Was having trouble getting the grouped or ()|() regex working
"though it did work directly...
nmap <silent> <leader>f mz:g/^func.\+($/:normal V$h%$h%zf<CR><leader>of
nmap <silent> <leader>of :g/^func.\+{$/:normal $V%zf<CR><leader>cf
nmap <silent> <leader>cf :g/^const ($/:normal V%zf<CR><leader>if
nmap <silent> <leader>if :g/^import ($/:normal V%zf<CR><leader>vf
nmap <silent> <leader>vf :g/^var .\+{$/:normal V$h%zf<CR><leader>sf
"don't recurse on that last chain call
nnoremap <silent> <leader>sf :g/^type.\+{$/:normal V%zf<CR>'z

nnoremap <silent> <leader>j :normal ggVG<CR>:<c-u>call clean_json#CleanJSON()<CR>
vnoremap <silent> <leader>j :<c-u>call clean_json#CleanJSON()<CR>

"set foldmethod=indent
"set foldlevel=99

"let g:go_version_warning = 0

"NOTE, It is possible to run python directly:
"function! AFunc() "functions names must be capitalized
"python3 <<EOF
"print("In a function")
"EOF
"endfunction
