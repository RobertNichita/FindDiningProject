# base image
FROM node:12.16.2

# install chrome for protractor tests
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update && apt-get install -yq google-chrome-stable

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
RUN npm install
RUN npm install -g @angular/cli@9.1.9

# add app
COPY . /app
RUN npm install -g @fortawesome/fontawesome-svg-core
RUN npm install -g @fortawesome/free-solid-svg-icons
RUN npm install -g @fortawesome/angular-fontawesome
RUN npm install -g @fortawesome/free-brands-svg-icons
RUN npm install -g @fortawesome/free-regular-svg-icons

RUN npm install -g bootstrap
RUN npm install -g ngx-bootstrap

# start app
CMD ng serve --host 0.0.0.0