
let g:gtrans_input_language = 'en'
let g:gtrans_output_language = 'fr'

function! Gtrans()
execute 'pyfile '.expand('<sfile>:p:h').'/gtrans.py'
endfunction

command! -nargs=0 Gtrans call Gtrans()
