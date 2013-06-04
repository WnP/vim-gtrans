""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                                                    "
"            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE             "
"   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION  "
"                                                                    "
"  0. You just DO WHAT THE FUCK YOU WANT TO.                         "
"                                                                    "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if !exists('g:gtrans_input_language')
    let g:gtrans_input_language = 'en'
endif

if !exists('g:gtrans_output_language')
    let g:gtrans_output_language = 'fr'
endif

pyfile <sfile>:p:h/gtrans.py

function! Gtrans()
    python vim_gtranslate()
endfunction

command! -nargs=0 Gtrans call Gtrans()
