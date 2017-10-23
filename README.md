# Генератор паролей по методу XKCD
Для работы необходим Python3 и библиотека Plumbum.
Также для начала работы необходимо выполнить:
```bash
git submodule init
git submodule update
```

## Использование
```bash
python pwgen.py -w google-10000-english/google-10000-english.txt 
```

```bash
python pwgen.py --help
генератор паролей по методу xkcd, n - количество необходимых паролей, при n=0 генератор будет выдавать ноые пароли по нажатию enter

Использование:
    pwgen.py [ОПЦИИ] [n=0]

Мета-опции
    -h, --help                                Печатает это сообщение и выходит
    --help-all                                Печатает помощь по всем подкомандам и выходит
    -v, --version                             Печатает версию этой программы и выходит

Опции
    -w, --wordlist ЗНАЧЕНИЕ:ExistingFile      файл со списком слов для генерации пароля; по умолчанию - 'russian_.txt';
                                              может быть передана несколько раз
```

## Источники
В репозиторий включены списки слов русского и английского языков:
russian.txt, russian_.txt и russian_surnames.txt из [этого репозитория](https://github.com/danakt/russian-words)
russian_5k_freq.txt составлен на основе [словаря 5000 частотных русских слов](http://www.artint.ru/projects/frqlist.php)
для английского языка используется [репозиторий из 10000 самых частотных английскихслов](https://github.com/first20hours/google-10000-english)
