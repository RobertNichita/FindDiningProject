# Team Aqua Project Repository

  *Website* : https://team-aqua.wixsite.com/aqua/

## Files

The deliverable files are in the respective deliverable folders numbered. The snapshots of the burndown chart and task board are in the **Burndown and Task Board** folder.

## Development

`client-server` contains the Angular pageserver (frontend) and `server` contains the Django server for endpoints and database connection to MongoDB (backend).

#### Prerequisites
Docker is installed and running.

### To launch the Angular Pageserver:

*In development configuration:*
```
cd client-server && docker-compose -f docker-compose.yml up -d client-dev
```

*In production configuration:*
```
cd client-server && docker-compose -f docker-compose.yml up -d client-prod
```

### To launch the Django Server:
```
cd server && docker-compose -f docker-compose.yml up -d server
```

## Documentation

`sd-site` contains the Docusaurus for documentation of backend and frontend components. 

#### Prerequisites

[yarn](https://classic.yarnpkg.com/en/docs/install/) is installed.

### To launch the documentation site:
```
cd sd-site && yarn start
```
