import sys
from secrets import choice
from plumbum.cli import Application, ExistingFile, SwitchAttr
#from plumbum.cli.switches import SwitchAttr


class XKCDPasswordGenerator(object):
    def __init__(self, wordlist_files=['russian_.txt']):
        self.words = []
        for wordlist_file in wordlist_files:
            with open(wordlist_file) as f:
                self.words.extend(map(lambda x:x[:-1], f))

    def generate_password(self, wordcount=4):
        pw = []
        for i in range(wordcount):
            pw.append(choice(self.words))
        return ' '.join(pw)

def endless():
    try:
        while input() == '':
            yield
    except:
        pass

class pwgen(Application):
    """генератор паролей по методу xkcd, n - количество необходимых паролей, при n=0 генератор будет выдавать ноые пароли по нажатию enter"""
    wordlist = SwitchAttr(
        ["-w", "--wordlist"], ExistingFile, "russian_.txt",
        list = True, help="файл со списком слов для генерации пароля")
    def main(self, n: int = 0):
        pwgen = XKCDPasswordGenerator(self.wordlist)
        if n != 0:
            iter = range(n)
        else:
            iter = endless()
        for _ in iter:
            pw = pwgen.generate_password()
            print(
                pw,
                " (",
                "Длина", len(pw), ","
                "длина cstr", len(pw.encode('utf-8')),
                ")")

if __name__ == "__main__":
    pwgen.run()
