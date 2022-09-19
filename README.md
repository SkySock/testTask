# Тестовое задание

Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
 - Django Модель Item с полями (name, description, price) 
API с двумя методами:
   - GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
   - GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
### Бонусные задачи:
- :white_check_mark: Запуск используя Docker
- :white_check_mark: Использование environment variables
- :white_check_mark: Просмотр Django Моделей в Django Admin панели
- :white_check_mark: Запуск приложения на удаленном сервере, доступном для тестирования
- :white_check_mark: Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
- :white_large_square: Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 
- :white_large_square: Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
- :white_large_square: Реализовать не Stripe Session, а Stripe Payment Intent.


### Запуск с Docker
1. Сделать git clone репозитория
2. В корне проекта создать и заполнить файл `.env`
```dotenv
DEBUG=1
SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1'
DATABASE=postgres
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_DB=stripe
POSTGRES_USER=stripe_app
POSTGRES_HOST=stripe-task-db
POSTGRES_PORT=5432
POSTGRES_PASSWORD=password

STRIPE_KEY=your-stripe-key
```
3. Собрать образ
```commandline
docker-compose build
```
4. Запустить
```commandline
docker-compose up
```
5. Создать и применить миграции
```commandline
docker exec -ti testTask-stripe-task-api-1 /bin/bash
```
```commandline
python ./manage.py makemigrations
python ./manage.py migrate
```
6. Создать суперпользователя
```commandline
python ./manage.py createsuperuser
```

### Доступ к приложению
Приложение запущено на `http://5.159.100.121/`

#### Endpoints
`admin/` - административная панель

`buy/{id}/` - получение session-id для item

`buy-order/{id}/` - получение session-id для order

`item/{id}/` - страница с кнопкой для оплаты item

`order/{id}/` - страница с кнопкой для оплаты order

#### Просмотреть товары и заказы в БД можно через тестового пользователя админки:
login - `test`

password - `t1e2s3t4`
