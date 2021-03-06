# Django project boilerplate
Шаблон Django проекта с использованием логирования и готовый для работы с Docker.

Для сборки и запуска приложения необходимо создать `.env` и `.env_docker_db`(если необходимо использовать базу данных для разработки) выполнить следующие команды находясь в главной директории проекта. Описание файлов `.env` и `.env_docker_db` расположены далее.
```
docker-compose up -d --build
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py collectstatic
docker-compose exec app python manage.py createsuperuser
```

## Структура проекта
Весь код проекта находится в директории `src`.

Все настройки и основные файлы проекта расположены в директории `core`.

## Настройки проекта
Основные настройки проекта разбиты на несколько файлов, но объеденены и доступны обычным способом через `django.conf.settings`.

Настройки разбиты на неколько файлов:
* `django.py` - все основные настройки Django;
* `third_party.py` - все основные настройки касающиеся сторонних библиотек таких как DRF, Celery и других;
* `dev.py` - настройки используемые только во время разработки - если Django запущен в режиме отладки с флагом `DEBUG=True`;
* `production.py` - настройки используемые на продакшене, когда Django запущен в боевом режиме с флагом `DEBUG=False`.

Настройки повторяющиеся в несколько файлах переопределяют друг друга в порядке расположения файлов в списке выше. Настройки в файлах `dev.py` и `production.py` используеются независимо друг от друга и в зависимости от флага `DEBUG` подгружается только один из них.

Вы можете расширить спикок файлов используемых для описания настроек. Для этого можно вынести их в отдельные файлы и модифицировать файл `core/settings/__init__.py`.

###  Настройка проекта через переменные окружения
Все главные настройки Django поумолчанию берутся из переменных окружения. Окружение читается из файла `.env` в корне проекта.

Файл `.env.template` является шаблоном файла окружения и содержит пример наиболее часто используемых настроек.

Ниже приведен список возможных переменных с описанием их назначения. Переменные, которые обязательны для заполнения, помечены * , если переменная иммет значение по умолчанию, то оно описано/указано в скобках. 

```
# Общие настройки Django
  DJANGO_DEBUG (False) - определяет флаг DEBUG в настройках Django
* DJANGO_SECRET_KEY - секретный ключ используемый Django, записывается в переменную SECRET_KEY в настройках Django 
  ALLOWED_HOSTS (localhost,127.0.0.1) - конвертируется в список и записывается в переменную ALLOWED_HOSTS. Представляет собой строку в которой запианы разрешенные хосты и ip адреса через запятую без дополнительных пробелов.
  INTERNAL_IPS - определяется аналогично ALLOWED_HOSTS, только устанавливает переменную INTERNAL_IPS настроек Django.

# Настройки статики и медиа файлов
  STATIC_URL_BASE (/static/) - переменная STATIC_URL_BASE настроек Django.
  STATIC_DIR (static) - переменная определяющая директорию внутри public в которой сохраняются и монтируются файлы статики.
  Так как в боевом режиме за отдачу статики отвечает Nginx необходимо, чтобы slug в STATIC_URL_BASE и имя директории STATIC_DIR должны совпадать для корректной отдачи. Это также касается описанных ниже MEDIA_BASE_URL и MEDIA_DIR, они тоже должны согласовываться между собой.
  MEDIA_URL_BASE (/media/) - переменная MEDIA_URL_BASE настроек Django.
  MEDIA_DIR (media) - переменная определяющая директорию внутри public в которой сохраняются и монтируются медиа файлы.

# Настройки базы данных
* DB_DRIVER_ENGINE (django.db.backends.postgresql) - python драйвер базы данных, подробнее см. документацию Django
* DB_NAME - имя базы данных
* DB_USER - имя пользователя для доступа к указанной базе
* DB_PASSWORD - пароль пользователя для доступа к базе данных
  DB_HOST (localhost) - хост на котором расположена база данных. При работе с базой данных db поднимаемой в докере, нужно установить имя хоста db (подробнее см. ниже описание контейнеров).
  DB_PORT (5432) - порт хоста на котором работает база данных.

# Настройки логирования
  LOGS_ENABLED (по умолчанию устанавливается как not DEBUG, т.е. логирование работает только в боевом режиме) - указывает необходимо ли производить логирование.
  LOGS_DIR (директория "logs/django/" в корне проекта) - путь по которому логи пишутся в контейнере. Изменить путь по которому логи контейнера монтируются и доступны на локальной машине можно в docker-compose.yml в разделе volumes контейнера app.
  ВАЖНО: директория в которую пишутся логи должна существовать как в контейнере так и на локальной машине по пути куда логи контейнера монтируются.

# Настройки email
  DJANGO_EMAIL_BACKEND (django.core.mail.backends.console.EmailBackend) - python модуль - драйвер email бекенда. Задает переменную EMAIL_BACKEND Django настроек.
  DEFAULT_FROM_EMAIL (default@django.dev) - задает переменную DEFAULT_FROM_EMAIL настроек Django.
  # Переменные ниже используются для идентификации доступа к DEFAULT_FROM_EMAIL почте и устанавливаются в настройках Django только если переменная DEFAULT_FROM_EMAIL установлена.
  EMAIL_HOST - переменная EMAIL_HOST настроек Django.
  EMAIL_PORT - переменная EMAIL_PORT настроек Django.
  EMAIL_HOST_USER - переменная EMAIL_HOST_USER настроек Django.
  EMAIL_HOST_PASSWORD - переменная EMAIL_HOST_PASSWORD настроек Django.
```

Ниже приведены примеры минимального и расширенного конфигов.

**Минимальный .env**
```
DJANGO_SECRET_KEY=cf#drw+$0sih)rgwwe7o8)0db3d!up%(5p803e9h6njiisq^fx

DB_DRIVER_ENGINE=django.db.backends.postgresql
DB_NAME=test_db
DB_USER=db_user
DB_PASSWORD=test_user_1234
DB_HOST=db
```

**Расширенный .env**
```
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=cf#drw+$0sih)rgwwe7o8)0db3d!up%(5p803e9h6njiisq^fx
ALLOWED_HOSTS=localhost,127.0.0.1
INTERNAL_IPS=localhost,127.0.0.1

DB_DRIVER_ENGINE=django.db.backends.postgresql
DB_NAME=test_db
DB_USER=db_user
DB_PASSWORD=test_user_1234
DB_HOST=db
DB_PORT=5432

LOGS_ENABLED=True
LOGS_DIR=/app/logs/

STATIC_URL_BASE=/s/
STATIC_DIR=s
MEDIA_URL_BASE=/m/
MEDIA_DIR=m
```

## Запуск и работа с веб-приложеним
Для удобства проект уже готов к использованию Docker. Файл `Dockerfile` описывает сборку контейнера самого приложения Django. Данное приложение запускает Django в синхронном режиме через `gunicorn` с 3-мя воркерами. Изменить команду запуска и/или увеличить кол-во воркеров можно отредактировав `Dockerfile`. 

Для удобства разработки и развертывания на боевом сервере в проекте имеется настройка `docker-compose` - файл `docker-compose.yml`.

В конфигурации `docker-compose` настроены три приложения:
* `nginx` - сервер Nginx проксирующий трафик на приложение Django - `app`
* `app` - Django приложение 
* `db` - база данных PostgreSQL 12

**ВНИМАНИЕ**
Настоятельно не рекомендуется использовать базу данных через `docker-compose` на боевой машине! 
На реальном сервере следует запускать базу как обычное приложение Linux или подключаться к другому серверу на котором настроена база.

**НЕ ЗАБЫВАЙТЕ ДЕЛАТЬ БЕКАПЫ ;-)**

Запустить контейнеры можно обычным для `docker-compose` способом.

Поднятие контейнеров:
```
docker-compose up -d
```

Поднятие контейнеров с повторной сборкой если есть изменения в образах:
```
docker-compose up -d --build
```

Выключение контейнеров:
```
docker-compose down
```

Выключение контейнеров с удалением данных (очисткой docker volume'ов)
```
docker-compose down -v
```

**При первом запуске нужно также, после поднятия контейнеров со сборкой, выполнить следующие команды:**
```
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py collectstatic
docker-compose exec app python manage.py createsuperuser
```

Команда `migrate` применит миграции если необходимо, ее нужно также выполнять после создания новых миграции.

`collectstatic` - скопирует статичные файлы, чтобы `nginx` смог выполнить ее раздачу. Ее нужно повторно выполнять после изменения статичных файлов.

Команда `createsuperuser` - стандартно создаст суперпользователя для доступа к админ панели.

### Описание контейнеров

#### Nginx
`nginx` собирается как отдельный `Docker` контейнер. Конфигурация `nginx` и `Dockerfile` используемый для сборки его контейнера находятся в каталоге `thrird_party_services/nginx/`.

По умолчанию `nginx` слушает порт на 80 внутри подсети в которой работают контейнеры и прокидывает его на порт 8888 на локальной машине. Также `nginx` напрямую отдает статические и медиа файлы.

#### App
`app` собирается как Django приложение используя `Dockerfile` расположенный в корне проекта. Приложение запускается с использованием файла `.env` для определения переменных окружения.

Возможные настройки описаны выше в разделе по настройке проекта через переменные окружения.

#### PostgreSQL
`db` - контейнер с базой данных PostgreSQL 12. **НЕ СЛЕДУЕТ ИСПОЛЬЗОВАТЬ ДАННЫЙ ВАРИАНТ БАЗЫ ДАННЫХ НА БОЕВОМ СЕРВЕРЕ**. Данная база подходит для работы на период отладки и разработки. Настройки базы данных которая поднимается в контейнере берутся из файла `.env_docker_db`. Шаблон для заполнения этого файла имеется в виде`.env_docker_db.template`.

```
POSTGRES_USER - имя пользователя для доступа к базе
POSTGRES_PASSWORD - пароль для пользователя
POSTGRES_DB - имя базы данных
```

Для доступа к данной базе со стороны контейнера приложения `app` необходимо в качестве хоста использовать значение `db`, а в качества имени базы данных и пользователя соответвующие значения указанные в файле `.env_docker_db`.

По умолчанию в `docker-compose.yml` настроен проброс порта базы `db` на порт 5432 локальной машины. Это сделано для удобной отладки проекта без пересборки Docker образов проекта, а запуская девелопмент сервер Django (через `manage.py runserver`) и подключаясь к тойже БД на время этапов разработки, когда часто необходимо пересобирать контейнер или проверять изменения в статики, так как в этом случае не надо запускать `collectstatic` для отображения изменений. 
