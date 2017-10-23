import sys
from secrets import choice
from plumbum.cli import Application, ExistingFile, SwitchAttr
#from plumbum.cli.switches import SwitchAttr


class XKCDPasswordGenerator(object):
    def __init__(self, wordlist_file='russian_.txt'):
        with open(wordlist_file) as f:
            self.words = list(map(lambda x:x[:-1], f))

    def generate_password(self):
        pw = []
        for i in range(4):
            pw.append(choice(self.words))
        return ' '.join(pw)

def endless():
    try:
        while input() == '':
            yield
    except:
        pass

class pwgen(Application):
    wordlist = SwitchAttr(["-w", "--wordlist"], ExistingFile, "russian_.txt")
    def main(self, n: int = 4):
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
