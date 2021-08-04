# ToDoList

## Overview

This command line application runs a to-do list which enables the user to add, edit and delete elements of the list. This application supports two languages for those commands: English and French. The main goal of this project is to implement the MVC (Model, View, Contoller) Design Pattern as well as considering the quality and maintainability aspects by implementing the appropriate Unit Tests.
The items added to the to-do are stored into the SQL database PostgreSQL

## Technologies
* Python --version 3.8.3
* Docker --version 20.10.5
* PostgreSQL
*

## Usage

Run the following commands in a terminal in order to use the application
**Set up**

Install Docker by following their tutorial https://docs.docker.com/engine/install/

**Start docker**
```
cd pgAdmin
docker-compose up
```

**install all dependencies***
```
pip3 install -r requirements.txt
```

**Start the program**
```
python3 main.py
```


To run SQL with Docker: ["How to Run PostgreSQL and pgAdmin Using Docker"](https://towardsdatascience.com/how-to-run-postgresql-and-pgadmin-using-docker-3a6a8ae918b5) from Mahbub Zaman

**Commands to control the application**

#### Adding element to the list

Inserting the first item:
```
Add item1
```

> output:
```
1. item1
```


Inserting a second item:
```
Add item2
```

> output:
```
1. item1
2. item2
```

#### deleting item in the list

```
Delete 2
```

> output:

```
1. item1
```

#### editing item in the list:

```
Edit 1 newItem
```

> output:
```
1. newItem
```

#### To Exit the program
```
Quit
```

French version: \
Add -> Ajoute \
Edit -> Modifie \
Delete -> Efface \
Quite -> Quitte
