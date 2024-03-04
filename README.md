## Тестовое задание для UpTrader

1. Клонируйте репозиторий
   
   ```sh
   git clone https://github.com/alexeisanko/rlt_task.git
   ```
2. Войдите в виртуальное окружение и установите необходимые библиотеки
   ```sh
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Примените миграции 
   ```sh
   python manage.py migrate
   ```

 4. Заполните БД
  
    Если хотите вручную заполнить то необходимо создать суперпользователя и создать записи через админ-панель
     ```sh
     python manage.py createsuperuser
     ```
    Так же реализована команда для самостоятельного заполнения случайными данными
     ```sh
     python manage.py load_simple_data
     ```
