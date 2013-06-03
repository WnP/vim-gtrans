
let g:gtrans_input_language = 'en'
let g:gtrans_output_language = 'fr'

let s:gtrans_path_sdir = expand('<sfile>:p:h')

function! Gtrans()
execute 'pyfile '.s:gtrans_path_sdir.'/gtrans.py'
endfunction

command! -nargs=0 Gtrans call Gtrans()
