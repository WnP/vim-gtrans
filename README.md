# vim-gtrans

## Introduction

vim-gtrans is a vim plugin which allow you to translate words or sentences by using Google Translate.

## Requirements

- vim compiled with python (+python option)
- [google-translate-python](https://github.com/terryyin/google-translate-python)

## Variables

gtrans define 2 variables which can be redefine, defaults values are:

    let g:gtrans_input_language = 'en'
    let g:gtrans_output_language = 'fr'

## Usage

**Cursor Mode**: simply run `:Gtrans` command will return the translation for the word under the cursor

**Visual Mode**: select an area, run `:'<,>':call Gtrans()` command return the translation for the given area
