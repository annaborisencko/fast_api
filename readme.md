# Домашнее задание к лекции «Создание REST API на FastApi» часть 1

Инструкцию по сдаче домашнего задания Вы найдете на главной странице репозитория.

# Задание 
Вам нужно написать на fastapi и докеризировать сервис объявлений купли/продажи.

У объявлений должны быть следующие поля:
 - заголовок
 - описание
 - цена
 - автор
 - дата создания

Должны быть реализованы следующе методы:
 - Создание: `POST /advertisement`
 - Обновление: `PATCH /advertisement/{advertisement_id}`
 - Удаление: `DELETE /advertisement/{advertisement_id}`
 - Получение по id: `GET  /advertisement/{advertisement_id}`
 - Поиск по полям: `GET /advertisement?{query_string}`

Авторизацию и аутентификацию реализовывать **не нужно**

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/annaborisencko/fast_api.git
cd fast_api
```

### 2. Настройка переменных окружения

Скопируйте файл .env.example в .env и заполните его необходимыми данными:

```bash
cp .env.example .env
```

Отредактируйте файл .env в любом текстовом редакторе.

```bash
nano .env
```

### 3. Запуск Docker контейнеров

Запустите все сервисы с помощью Docker Compose:

```bash
docker-compose up -d
```

Проверьте, что оба контейнера запущены и работают:

```bash
docker-compose ps
```

Вы должны увидеть два контейнера:

PROJECT_NAME-db - контейнер с PostgreSQL
PROJECT_NAME-app - контейнер с fast_api сервером

### 4. Выполнение клиентского скрипта

После успешного запуска контейнеров выполните клиентский скрипт:

```bash
docker-compose exec app python ../client.py
```

Или, если используете Python 3:

```bash
docker-compose exec app python3 ../client.py
```

Результат выполнения отобразится в терминале.

### 5. Остановка контейнеров

После проверки работы, остановите контейнеры

```bash
docker-compose down -v
```