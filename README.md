## Сущности

### Сериал
Поля:
- "id" - уникальный идентификатор
- "title" - название
- "description" - кратное описание
- "release_date" - дата выхода
- "seasons" - кол-во сезонов
- "genre" - many to many
- "age_rating" - возрастной рейтинг, ссылка на сущность


### Жанр
- "id" - уникальный идентификатор
- "name, unique" - название, уникально
- "description" - кратное описание


### Возрастной рейтинг
- "name, unique"
- "description"

#### Рейтинги
- рейтинг G - без ограничений
- рейтинг PG - рекомендуется присутствие родителей
- рейтинг PG13 - детям старше 13 лет
- рейтинг PG16 - зрителям старше 13 лет
- рейтинг PG18 - зрителям старше 18 лет



## Таблицы

### Сериал
Поля:
- "id" - bigint pk
- "title" - str, not null, index
- "description" - not null, default '""'
- "release_date" - "date", not null
- "seasons" - "uint", default '1'
- "genre" - many to many
- "age_rating" - nullable


### Жанр
Поля:
- "id" - int pk
- "name" - str, unique, not null, index
- "description" - not null, default '""'


### Возрастной рейтинг
- "name, unique" - str, unique, not null, index
- "description" - not null, default '""'
