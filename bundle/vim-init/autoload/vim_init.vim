if !has('python3')
  echo "python3 is required for vim_init#Init()"
  finish
endif

"TODO, i probably want to enable options and what not so I don't do this for all header files
let s:dir = expand("<sfile>:p:h:h")
function! vim_init#Init()
  execute "py3file " . s:dir . "/python/main.py"
endfunction
