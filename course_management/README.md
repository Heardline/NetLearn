### Структура БД:

Таблица `courses`
| Поле          | Тип данных       | Ограничения                    | Описание                       |
|---------------|------------------|--------------------------------|--------------------------------|
| id            | UUID PRIMARY KEY | NOT NULL                       | Уникальный идентификатор       |
| title         | String           | NOT NULL                       | Название курса                 |
| description   | Text             |                                | Описание курса                 |
| created_at    | Timestamp        | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Время создания курса           |
| updated_at    | Timestamp        |                                | Время последнего обновления курса|

Таблица `blocks`
| Поле          | Тип данных       | Ограничения                    | Описание                       |
|---------------|------------------|--------------------------------|--------------------------------|
| id            | UUID PRIMARY KEY | NOT NULL                       | Уникальный идентификатор блока |
| course_id     | UUID FOREIGN KEY | REFERENCES courses(id) ON DELETE CASCADE | ID курса                       |
| title         | String           | NOT NULL                       | Название блока                 |
| description   | Text             |                                | Описание блока                 |
| created_at    | Timestamp        | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Время создания блока           |
| updated_at    | Timestamp        |                                | Время последнего обновления блока|

Таблица `modules`
| Поле          | Тип данных       | Ограничения                    | Описание                       |
|---------------|------------------|--------------------------------|--------------------------------|
| id            | UUID PRIMARY KEY | NOT NULL                       | Уникальный идентификатор модуля|
| block_id      | UUID FOREIGN KEY | REFERENCES blocks(id) ON DELETE CASCADE | ID блока                       |
| title         | String           | NOT NULL                       | Название модуля                |
| description   | Text             |                                | Описание модуля                |
| created_at    | Timestamp        | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Время создания модуля          |
| updated_at    | Timestamp        |                                | Время последнего обновления модуля|

Таблица `topics`
| Поле          | Тип данных       | Ограничения                    | Описание                       |
|---------------|------------------|--------------------------------|--------------------------------|
| id            | UUID PRIMARY KEY | NOT NULL                       | Уникальный идентификатор темы  |
| module_id     | UUID FOREIGN KEY | REFERENCES modules(id) ON DELETE CASCADE | ID модуля                      |
| title         | String           | NOT NULL                       | Название темы                  |
| content       | Text             |                                | Содержание темы                |
| created_at    | Timestamp        | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Время создания темы            |
| updated_at    | Timestamp        |                                | Время последнего обновления темы|

### Бизнес Правила:
- Структура Курса должна быть гибкой, чтобы поддерживать различные сценарии обучения.
- Студенты могут видеть свой прогресс по темам, модулям, блокам и курсам.
- Процесс прохождения тем, модулей и блоков должен быть понятным и прозрачным для студента.

### API Методы:
- `GET /courses`: Получение списка всех курсов.
- `GET /courses/{course_id}`: Получение детальной информации о курсе.
- `GET /blocks/{block_id}`: Получение детальной информации о блоке.
- `GET /modules/{module_id}`: Получение детальной информации о модуле.
- `GET /topics/{topic_id}`: Получение детальной информации о теме.
- `POST /topics/{topic_id}/complete`: Отметка о завершении темы студентом.
