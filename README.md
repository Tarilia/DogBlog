### Test and linter status
[![Maintainability](https://api.codeclimate.com/v1/badges/2cf1b49cd0e2430bd660/maintainability)](https://codeclimate.com/github/Tarilia/project/maintainability)
[![Linter](https://github.com/Tarilia/project/actions/workflows/test.yml/badge.svg)](https://github.com/Tarilia/project/actions/workflows/test.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2cf1b49cd0e2430bd660/test_coverage)](https://codeclimate.com/github/Tarilia/project/test_coverage)

### DogBlog

 - веб-cайт, созданный на основе фреймворка Django.
 - для верстки используется Bootstrap5.
 - позволяет пользователям читать/добавлять/комментировать статьи, отправлять обратную связь.

### Установка:

 - клонировать этот репозиторий
 - poetry install
 - make migrate
 - make dev - для локального использования
 - make start - для продакшена

 Для настройки приложения, нужно установить в .env следующие переменные среды:

 - DEBUG
 - DATABASE_URL
 - SECRET_KEY
 - EMAIL_HOST_USER
 - EMAIL_HOST_PASSWORD
 - REDIS_LOCATION
 - CELERY_BROKER_URL
 - CELERY_RESULT_BACKEND

### Docker:
 Для настройки нужно установить в .env следующие переменные среды:
 - DATABASE_URL в следующийем формате: DATABASE_URL={provider}://{user}:{password}@{host}:{port}/{db}
 - POSTGRES_PASSWORD
 - POSTGRES_USER
 - POSTGRES_DB

Запуск: docker-compose up

### Визуализация:
- главная страница сайта. Статьи можно фильтровать по категориям и по тегам:

[![2024-06-30-135014.png](https://i.postimg.cc/gk9M1zXL/2024-06-30-135014.png)](https://postimg.cc/NL47HwxQ)

- для доступа к основному функционалу сайта, необходима аутентификация и авторизация пользователя:

[![2024-06-30-135110.png](https://i.postimg.cc/vBkPYM0j/2024-06-30-135110.png)](https://postimg.cc/Hc003GD4)

[![image.png](https://i.postimg.cc/CKMrJcZv/image.png)](https://postimg.cc/68ShpLfR)

- после авторизации доступен профиль пользователя, с возможностью обновлять данные:

[![image.png](https://i.postimg.cc/2jLcHb6f/image.png)](https://postimg.cc/3W7FNwmL)

- добавление статьи доступно только авторизованным пользователям:

[![image.png](https://i.postimg.cc/26VcN37h/image.png)](https://postimg.cc/N9v71sVj)

- изменить и удалить статью может только автор или администратор сайта:

[![image.png](https://i.postimg.cc/mgBm2mSb/image.png)](https://postimg.cc/KRpP0rVV)

- под статьей есть возможность оставить комментарий. Изменять и удалять может только автор или администратор сайта:

[![image.png](https://i.postimg.cc/KjT04VVY/image.png)](https://postimg.cc/y3Vmbf7q)

- обратная связь реализована в ассинхронном режиме. Письмо приходит на почту и в админ панель:

[![image.png](https://i.postimg.cc/zfdtQTKq/image.png)](https://postimg.cc/PLwQppS7)
