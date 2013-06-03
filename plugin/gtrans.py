import vim
import translate
import urllib2
import string

to_lang = vim.eval('g:gtrans_output_language') or 'fr'
from_lang = vim.eval('g:gtrans_input_language') or 'en'
trans = translate.Translator(to_lang=to_lang, from_lang=from_lang)

encoding = vim.eval('&encoding') or 'utf-8'
unwordable = ''.join((string.punctuation, string.whitespace))

cur = vim.current
markL = cur.buffer.mark('<')
markR = cur.buffer.mark('>')
cursor = cur.window.cursor

res = ''

if markL and markR and cursor[1] == 0 and markL[0] <= cursor[0] <= markR[0]:
    # visual mode
    if cursor[0] == markL[0]:
        if markL[0] == markR[0]:
            res = cur.buffer[markL[0] - 1][markL[1]:markR[1]]
        else:
            res = cur.buffer[markL[0] - 1][markL[1]:]
            for x in xrange(markR[0] - markL[0] - 1):
                res = ' '.join((res, cur.buffer[markL[0] + x]))
            res = ' '.join((res, cur.buffer[markR[0] - 1][:markR[1]]))
else:
    # cursor mode
    line = vim.current.buffer[cursor[0] - 1]
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

translated = ''
try:
    translated = trans.translate(res)
except urllib2.HTTPError:
    pass
print translated.encode(encoding)
