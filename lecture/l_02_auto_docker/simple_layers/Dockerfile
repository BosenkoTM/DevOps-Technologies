# Базовый образ
FROM node:18-alpine

# Рабочая директория
WORKDIR /app

# Копируем только package.json и package-lock.json
# Это отдельный слой для зависимостей
COPY package*.json ./

# Устанавливаем зависимости
# Это создаст слой с node_modules
RUN npm install

# Копируем остальные файлы проекта
# Это создаст слой с кодом приложения
COPY . .

# Открываем порт
EXPOSE 3000

# Запускаем приложение
CMD ["npm", "start"]

# sudo apt install npm
# Инициализируем npm проект
# npm init -y
# Создадим простой файл приложения index.js:
#echo 'console.log("Hello from Docker!");' > index.js

# Сборка образа docker build -t myapp .

# Запуск контейнера docker run -p 3000:3000 myapp
