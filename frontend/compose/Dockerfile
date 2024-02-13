FROM node:21-alpine

WORKDIR /app

COPY ./frontend/package.json .

RUN npm install

COPY ./frontend .

EXPOSE 5173

# dev
CMD [ "npm", "run", "dev" ]

# serve
#RUN npm run build
#CMD [ "npm", "run", serve" ]