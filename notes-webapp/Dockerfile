FROM node:latest

WORKDIR /notes-webapp

ENV PATH /notes-webapp/node_modules/.bin:$PATH

COPY package.json /notes-webapp/package.json
RUN npm install
RUN npm install -g @angular/cli

COPY . /notes-webapp

CMD ng serve --host 0.0.0.0
