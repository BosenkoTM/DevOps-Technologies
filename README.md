# DevOps-Technologies

## Описание
Курс посвящен знакомству и работе с технологиями контейнеризации и DevOps практиками. Предлагается подробно рассмотреть технологии контейнеризации и оркестрации, их особенности, преимущества/недостатки, и действительно ли они так повсеместно необходимы и почему. Повышенное внимание будет уделено природе понятия DevOps, а также особенностями микросервисной инфраструктуры. Также в рамках дисциплины будут получены практические навыки работы с Docker, Docker Compose и Kubernetes


## Содержание практических работ

[Практическая работа 2.1. Введение в Linux](http://95.131.149.21/moodle/mod/assign/view.php?id=1074)

[Практическая работа 2.2. Создание и управление репозиториями на GitHub. Работа с ветками, слияниями, разрешение конфликтов](http://95.131.149.21/moodle/mod/assign/view.php?id=1091)

[Практическая работа 3.1. Dockerfile](Lesson%203%20Containerizing%20Applications/lab3_1)

[Практическая работа 3.2. Docker Compose](Lesson%203%20Containerizing%20Applications/lab3_2)

[Практическая работа 4.1. Kubernetes](Lesson%204%20Orchestration%20of%20applications/lab4_1)

[Практическая работа 4.2. Сервис в Kubernetes](https://github.com/BosenkoTM/DevOps-Technologies/tree/main/Lesson%204%20Orchestration%20of%20applications/lab4_2)

# Установка Docker Ubuntu 22.04

1. Установка вспомогательных пакетов 

Для корректной работы Docker требуется наличие нескольких пакетов. Они помогут в безопасности, управлении репозиториями и взаимодействии с интернетом:

`curl` – это инструмент командной строки для передачи данных и работы с `URL`-адресами;

`software-properties-common` – этот пакет предоставляет скрипты для управления программным обеспечением и добавления репозиториев;

`ca-certificates` – необходим для безопасной передачи данных и подтверждения подлинности сертификатов;

`apt-transport-https` – позволяет работать с репозиториями, которые передают данные по протоколу `HTTPS`.

  ```bash
  sudo apt install curl software-properties-common ca-certificates apt-transport-https -y
  ```

2. Для обеспечения безопасности установки Docker необходимо добавить ключ `GPG` с официального репозитория. Этот ключ гарантирует подлинность загружаемых пакетов. 

  ```bash
  wget -O- https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor | sudo tee /etc/apt/keyrings/docker.gpg > /dev/null
  ```
3. Добавить репозиторий Docker для доступа к его последним версиям.
  ```bash
  echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu jammy stable"| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```

4. После добавления нового репозитория важно снова обновить индексы пакетов, чтобы APT узнал о новом источнике. Проверка репозитория Docker. Установка Docker.Проверка статуса Docker.
```bash
sudo apt update
```
```bash
apt-cache policy docker-ce
```
```bash
sudo apt install docker-ce -y
```
```bash
sudo systemctl status docker
```
# Установка Docker Compose Ubuntu 22.04

Существует несколько способов установки Docker Compose V2 в систему Ubuntu 22.04:
- установка вместе с `Docker Desktop`;
- установка из репозитория как плагина `docker-compose-plugin`;
- установка автономной версии `Docker Compose V2`.
  
## Установка автономной версии Docker Compose V2

1. Создать каталог для Docker Compose:
```bash
mkdir -p ~/.docker/cli-plugins/
```
2. Загрузить последнюю стабильную версию Docker Compose с [официальной страницы релизов Docker](https://github.com/docker/compose/releases)

```bash
curl -SL https://github.com/docker/compose/releases/download/АКТУАЛЬНАЯ_ВЕРСИЯ/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
```
где `АКТУАЛЬНАЯ_ВЕРСИЯ` актуализируем в ветке [https://github.com/docker/compose/releases/](https://github.com/docker/compose/releases/)

3. Убедиться, что файл docker-compose имеет правильные разрешения для выполнения команды:
```bash
chmod +x ~/.docker/cli-plugins/docker-compose
```
4. Проверить установленную версию Docker Compose:
```bash
sudo docker compose version
```























