# Инструкция по установке 

## MkDocs

Инструкция по установке есть на [сайте MkDocs](https://www.mkdocs.org/#installation).

Надо установить:
* python [python.org](https://www.python.org/downloads/) !!!
* pip – менеджер пакет (ставится, обычно, вместе с питоном)
* mkdocs – пакет с движком mkdocs
```bash

```
Полезные ссылки:

* [mkdocs.org](https://www.mkdocs.org/)
* [плагины MkDocs](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins)
* [Темы MkDocs](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes)
* [markdown дополнения](https://python-markdown.github.io/extensions/)

## Тема

В проекте используется тема [material](https://squidfunk.github.io/mkdocs-material/getting-started/).

Для установки запускаем:
```bash
pip install mkdocs-material
```

Полезные ссылки:

* [Настройки темы material](https://squidfunk.github.io/mkdocs-material/getting-started/) 
* [Плагины из темы material](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
* [Проект темы material на GitHub](https://github.com/squidfunk/mkdocs-material)

## Плагины

В проекте используются плагины:
* [search](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins#search) – встроенный плагин поиска.
* [img2fig](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins#img2fig) – отображение картинок в отдельном теге с подписью внизу.

```bash
pip install mkdocs-img2fig-plugin
pip install mkdocs-section-index
pip install mkdocs-include-markdown-plugin
pip install mkdocs-video
pip install mkdocs-literate-nav
```


## Команды

Для разработки и проверки документации можно использовать команды:
* `mkdocs serve` – (с созданием pdf файлов) запуск локально сервера.
* `mkdocs serve -f dev.yml` (без создания pdf файлов)

* `mkdocs build` – сборка сайта в html формат. Собирается в каталог `site`.
* `mkdocs build -f admin-manuals.yml` (с созданием  pdf файла с инструкциями для администратора)

## Оформление текста

Чтобы включить увеличение изображения при помощи клика по нему, необходимо добавить {: .zoom} после объявления изображения, не отделяя пробелом. 

1. 
```html
<figure class="figure-image">
  <img src="../media/examplel.png" alt="Рисунок 1" class="zoom">
  <figcaption>Рисунок 1</figcaption>
</figure>
 ```
* <img alt="Рисунок 1" src="examplel.png" class="zoom"/>
несовместимо с **img2fig**, поэтому **требует запуск zoom.ipynb** для конвертации в вариант ниже:

2. 
```html
<figure class="figure-image"> 
  <img src="example2.png" class="zoom" alt="Рисунок 2">
  <figcaption>Рисунок 2</figcaption>
</figure>
```

Фича была добавлена при помощи файлов extra.js и extra.css. При подключённом плагине img2fig можно использовать вариант 1, а затем прогнать скрипт в zoom.py, который сконвертирует все рисунки из всех *.md файлов из варианта 1 в вариант 2. 
Для этого необходимо **запустить команду** в консоли в папке с файлом zoom.py:

```console
python zoom.py
```

В случае ошибки **no library called "cairo" was found** необходимо скачать библиотеки:

https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
