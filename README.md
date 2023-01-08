## Что это?

Это простой парсер в формат .csv для данных, выгружаемых из истории операций "Сбербанк.Онлайн". Написано и предназначено для личного использования: я веду учёт личных финансов в таблице и устал забивать руками каждый платёж по карте.

Программа не производит никаких взаимодействий с сайтом "Сбербанка" и личным кабинетом клиента по сети, не использует чужие данные и вообще не даёт доступа ни к чему такому, к чему изначально нет доступа у пользователя. Функционал программы ограничен предоставлением данных, изначально доступных пользователю, в удобной форме таблицы.

## Как использовать?

1. Заходим в личный кабинет в историю операций по карте. Кликаем на кнопку "Отчёт по карте". Настраиваем период, за который нужна выгрузка. Сохраняем страницу средствами браузера.
2. Открываем консоль, заходим в папку сохраненной страницы с окончанием "_files". Приложению для работы нужен файл index.html, он находится в данной папке.
3. Запускаем скрипт:
    make start
4. Если всё прошло успешно, то в этой же папке появится файл transactions.csv со списком транзакций  