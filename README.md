# 42pxTest - ТЕСТОВОЕ ЗАДАНИЕ Python/Django

### Описание
Реализован сервис, который уменьшает картинки по заданным размерам.

### Требования
+ Наличие IDE (https://www.jetbrains.com/pycharm/)
+ Docker desktop (https://www.docker.com/products/docker-desktop/)

### Инструкция по запуску
___
+ Склонировать проект в локальный репозиторий:

  ``` git clone https://github.com/RomanDeveloper1111/42pxTest.git ```
+ В корне проекта добавить файл .env и заполнить по примеру содержимого файла .env_example в корне проекта:

   ```
   SECRET_KEY=
   DEBUG=
   ALLOWED_HOSTS=
   HOST=

   POSTGRES_DB=
   POSTGRES_USER=
   POSTGRES_PASSWORD=
   POSTGRES_HOST=
   POSTGRES_PORT=
   ```

+ Находясь в корне проекта запустить команду по сборке docker image и запуску контейнеров.
  ```
  docker-compose up
  ```
> #### Примечание
  В случае ожидания соединения с базой данных на стороне web-app остановить все контейнеры и запустить команду выше снова.

### Инпоинты
+ ```
  /api/resize_picture/
  ```
  Методы: ```POST```

  Данные:
    ```
      image: required

      width: required

      height: optional
    ```

  Ответ:
  
      HTTP_200_OK
  
      HTTP_201_CREATED
  
      HTTP_400_BAD_REQUEST
  
      - link (hash_link; example: {"link": "http://localhost:8000/media/709c1e56cb9043e98a4700563f1a2cd9_600x600.jpg"})
