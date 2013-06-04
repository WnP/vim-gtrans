######################################################################
#                                                                    #
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE             #
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION  #
#                                                                    #
#  0. You just DO WHAT THE FUCK YOU WANT TO.                         #
#                                                                    #
######################################################################

import vim
import translate
import urllib2
import string


def __do_visual(buff, cur, res=''):
    cursor = cur.window.cursor

    if cursor[0] == buff.mark('<')[0]:

        if buff.mark('<')[0] == buff.mark('>')[0]:

            return buff[
                buff.mark('<')[0] - 1][
                    buff.mark('<')[1]:buff.mark('>')[1]]
        else:
            res = buff[buff.mark('<')[0] - 1][buff.mark('<')[1]:]

            for x in xrange(buff.mark('>')[0] - buff.mark('<')[0] - 1):
                res = ' '.join((res, buff[buff.mark('<')[0] + x]))

            return ' '.join((
                res,
                buff[buff.mark('>')[0] - 1][:buff.mark('>')[1]]))


def __do_cursor(cur, res=''):
    cursor = cur.window.cursor
    line = cur.buffer[cursor[0] - 1]
    unwordable = ''.join((string.punctuation, string.whitespace))

    x = line[cursor[1]]
    i = 0
    while x not in unwordable and i + cursor[1] >= 0:
        res = ''.join((x, res))
        i -= 1
        x = line[cursor[1] + i]

    x = line[cursor[1] + 1]
    i = 1
    while x not in unwordable and i + cursor[1] <= len(line):
        res = "".join((res, x))
        i += 1
        x = line[cursor[1] + i]
    return res


def vim_gtranslate():
    to_lang = vim.eval('g:gtrans_output_language') or 'fr'
    from_lang = vim.eval('g:gtrans_input_language') or 'en'
    trans = translate.Translator(to_lang=to_lang, from_lang=from_lang)

    encoding = vim.eval('&encoding') or 'utf-8'

    buff = vim.current.buffer
    cur = vim.current
    cursor = cur.window.cursor
    res = ''

    if buff.mark('<') and buff.mark('>') and cursor[1] == 0 \
            and buff.mark('<')[0] <= cursor[0] <= buff.mark('>')[0]:
        # visual mode
        res = __do_visual(buff, cur)
    else:
        # cursor mode
        res = __do_cursor(cur)

    translated = ''
    try:
        translated = trans.translate(res if res else '')
    except urllib2.HTTPError:
        pass
    print translated.encode(encoding)
