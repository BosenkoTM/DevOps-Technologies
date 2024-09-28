## Лабораторная 2. Docker Compose

### Задача
Создать docker-compose.yml из минимум трех сервисов

**На основе Dockerfile из ЛР 1 создать композ проект. Обязательные требования:**
- минимум 1 init + 2 app сервиса (одноразовый init + приложение + бд или что-то другое, главное чтоб работало в связке)
- автоматическая сборка образа из лежащего рядом Dockerfile и присваивание ему (образу) имени
- жесткое именование получившихся контейнеров 
- минимум один из сервисов обязательно с depends_on
- минимум один из сервисов обязательно с volume
- минимум один из сервисов обязательно с прокидыванием порта наружу
- минимум один из сервисов обязательно с ключом command и/или entrypoint (можно переиспользовать тот же, что в Dockerfile)
- добавить healthcheck
- все env-ы прописать не в сам docker-compose.yml, а в лежащий рядом файл .env
- должна быть явно указана network (одна для всех)
### Запуск
```commandline
cd lab2
```
```commandline
cp .env.example .env
```
```commandline
docker-compose up
```
OpenAPI: 
```commandline
http://localhost:8000/api/docs
```
Health Check:
```commandline
http://localhost:8000/health
```

### Ответы на вопросы
**1. Можно ли ограничивать ресурсы (например, память или CPU) для сервисов в docker-compose.yml? Если нет, то почему, если да, то как?**
Да, в Docker Compose можно ограничивать ресурсы для контейнеров, используя специальные параметры в файле docker-compose.yml.
Чтобы ограничить память для контейнера, можно использовать параметр mem_limit. 

**Например:**
```yaml
services:
  my_service:
    image: my_image
    memory: 512m # Устанавливает ограничение памяти в 512 МБ
```
Для ограничения использования CPU, можно использовать параметры cpu_quota и cpu_period. cpu_quota определяет долю CPU, доступную для контейнера, а cpu_period задает период времени, за который эта квота применяется. 

**Например:**
```yaml
services:
  my_service:
    image: my_image
    cpu_quota: 50000 # Ограничивает использование CPU до 50% от одного ядра
    cpu_period: 100000 # Период времени в микросекундах (100000 = 100 мс)
```
В этом примере контейнер my_service будет ограничен использованием 50% от одного ядра CPU.

Ограничения ресурсов помогают предотвратить ситуации, когда один контейнер потребляет слишком много ресурсов и влияет на работу других контейнеров или хоста Docker.


\
**2.Как можно запустить только определенный сервис из docker-compose.yml, не запуская остальные?**

Чтобы запустить только определенный сервис из docker-compose.yml, не запуская остальные, можно использовать команду:
```commandline
docker-compose up service_name
```
Заменить <service_name> на имя сервиса, который хотим запустить.

