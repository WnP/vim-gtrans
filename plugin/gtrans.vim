let g:gtrans_input_language = 'en'
let g:gtrans_output_language = 'fr'

pyfile <sfile>:p:h/gtrans.py

function! Gtrans()
python vim_gtranslate()
endfunction

command! -nargs=0 Gtrans call Gtrans()
