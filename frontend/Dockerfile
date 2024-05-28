#FROM node:20-alpine
#
#WORKDIR /app
#
#COPY package.json package-lock.json ./
#
#RUN npm install
#
#COPY . .
#
#EXPOSE 5173
#
#CMD ["npm", "start"]
#
FROM node:20-alpine

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

RUN npm run build

EXPOSE 5173

CMD [ "npm", "run", "preview" ]