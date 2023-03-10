## sbpars - simply bank ordering parser

### Что это?

Это простой парсер в форматы .csv и .xlsx для данных, выгружаемых из истории операций по карте одного банка. Написано и предназначено для личного использования: я веду учёт личных финансов в таблице и устал забивать руками каждый платёж по карте.

Программа не производит никаких взаимодействий с сайтом банка и личным кабинетом клиента по сети, не использует чужие данные и вообще не даёт доступа ни к чему такому, к чему изначально нет доступа у пользователя. Функционал программы ограничен предоставлением данных, изначально доступных пользователю, в удобной форме таблицы.

### Как использовать?

Заходим в личный кабинет в историю операций по карте. Кликаем на кнопку "Отчёт по карте". Настраиваем период, за который нужна выгрузка. Сохраняем страницу средствами браузера.

Открываем консоль, заходим в папку сохраненной страницы с окончанием "_files". Приложению для работы нужен файл index.html, он находится в данной папке.

Далее два варианта: можно установить утилиту через pip, можно работать с исходным кодом.

*Вариант 1*

Устанавливаем и запускаем в папке, где находится index.html:
```
pip install sbpars
sbpars
```

*Вариант 2*

Копируем index.html в папку со скриптом и запускаем

```
pip install poetry
make start
```

Если всё прошло успешно, то в этой же папке появятся файлы transactions с расширениями .csv и .xlsx со списком транзакций
