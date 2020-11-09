if !has('python3')
  echo "python3 is required for vim_init#Init()"
  finish
endif

let s:dir = expand("<sfile>:p:h:h")
function! vim_init#Init()
  execute "py3file " . s:dir . "/python/main.py"
endfunction
