from flask import flash
import unicodedata

def hankaku(words):  #半角全角判定関数
    for word in words:
        result = unicodedata.east_asian_width(word)
        if result == 'Na':
            return True
        else:
            flash('半角数字で入力してください')
            break