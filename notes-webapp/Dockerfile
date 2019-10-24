FROM node:latest

WORKDIR /notes-webapp

ARG ANGULAR_PORT=8080

ENV ANGULAR_PORT=${ANGULAR_PORT}
EXPOSE ${ANGULAR_PORT}


# ENV PATH /notes-webapp/node_modules/.bin:$PATH

# COPY package.json /notes-webapp/package.json
RUN npm install
RUN npm install -g @angular/cli

COPY . /notes-webapp

CMD ng serve
