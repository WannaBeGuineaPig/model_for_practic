# MkDocs
## Инструкция по установке есть на сайте MkDocs.

### Надо установить:

python python.org
pip – менеджер пакет (ставится, обычно, вместе с питоном)
mkdocs – пакет с движком mkdocs

`pip install mkdocs`
Полезные ссылки:

mkdocs.org

### плагины MkDocs

Темы MkDocs

markdown дополнения

Тема
В проекте используется тема material.

Для установки запускаем:

`pip install mkdocs-material`
Полезные ссылки:

Настройки темы material
Плагины из темы material
Проект темы material на GitHub
Плагины
В проекте используются плагины:

search – встроенный плагин поиска.
img2fig – отображение картинок в отдельном теге с подписью внизу.
pip install mkdocs-img2fig-plugin

Для разработки и проверки документации можно использовать команды
* `mkdocs serve` (с созданием pdf файлов)
* `mkdocs serve -f dev.yml` (без создания pdf файлов)
* `mkdocs build -f admin-manuals.yml` (с созданием  pdf файла с инструкциями для администратора)

Перед запуском надо установить mkdocs и его расширения. Сделать это можно при помощи команды, запущенной в папке mkdocs
```
pip install -r requirements.txt
```

Чтобы включить увеличение изображения, необходимо добавить . Если не работает (а это происходит при работе плагина img2fig), то использовать html-вариант. Автоматический конвертер первого варианта во второй (zoom.py) есть в bitedo-doc и документации ERP.
```
а) ![Рис 1](examplel.png)
б) <img alt="Рис 1" src="examplel.png" class="zoom"/>
```

В случае ошибки **no library called "cairo" was found** необходимо скачать библиотеки:

https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases

Если при запуске команды **mkdocs serve -f dev.yml** появляется ошибка что данная команда не определена, то в переменнах средах укажите путь: **C:\Users\User\AppData\Roaming\Python\Python310\Scripts**