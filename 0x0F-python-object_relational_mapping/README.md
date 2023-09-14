# 0x0F Python - Object-Relational Mapping (ORM)

## Overview

0x0F Python - Object-Relational Mapping (ORM) is a Python library that simplifies database interactions by allowing you to work with databases using Python objects instead of writing raw SQL queries. This README provides an introduction to using 0x0F ORM, its features, and how to get started.

## Features

0x0F ORM offers the following key features:

1. **Object-Relational Mapping**: Map Python classes to database tables, making it easy to create, read, update, and delete records without writing SQL queries.

2. **Model Definition**: Define database models using Python classes. Each class corresponds to a table, and class attributes define the table columns.

3. **Querying**: Perform complex database queries using Python methods and chaining. The library supports various querying options, including filtering, sorting, and aggregation.

4. **Transaction Support**: Manage database transactions easily to ensure data consistency.

5. **Database Agnostic**: 0x0F ORM supports multiple database systems, allowing you to switch databases without changing your application code.

6. **Migrations**: Automatically generate and apply database schema changes using migrations.

7. **Integration**: Seamless integration with popular Python frameworks such as Flask and Django.

## Getting Started

Follow these steps to start using 0x0F ORM in your Python project:

### 1. Installation

Install 0x0F ORM using pip:

```bash
pip install 0x0f-orm
```

### 2. Define Models

Define your database models as Python classes, inheriting from the `0x0f.orm.Model` class. For example:

```python
from 0x0f.orm import Model, fields

class User(Model):
    username = fields.StringField(max_length=50)
    email = fields.EmailField()
    age = fields.IntegerField()
```

### 3. Initialize the Database

Initialize the database connection by providing the database URL or configuration settings. You can do this in your application's configuration or directly in your code:

```python
from 0x0f.orm import Database

db = Database(database_url="postgresql://user:password@localhost/mydb")
```

### 4. Create Tables

Create the database tables based on your model definitions:

```python
db.create_tables([User])
```

### 5. Perform CRUD Operations

You can now use the defined models to interact with the database. For example:

```python
# Create a new user
user = User(username="johndoe", email="johndoe@example.com", age=30)
user.save()

# Query users
users = User.filter(age__gte=25)
for user in users:
    print(user.username, user.email)
```

### 6. Migrations

As your application evolves, use migrations to manage changes to your database schema. 0x0F ORM provides tools for generating and applying migrations.

## Documentation

For detailed information on using 0x0F ORM, refer to the official documentation at [https://docs.0x0f-orm.com](https://docs.0x0f-orm.com).

## Contributing

If you want to contribute to 0x0F ORM or report issues, please visit the GitHub repository at [https://github.com/Sarahemmy/0x0f-orm](https://github.com/Sarahemmy/0x0f-orm).

## License

0x0F ORM is released under the MIT License. See the LICENSE file for more details.

## Acknowledgments

Special thanks to the open-source community for their contributions and support in developing 0x0F ORM.

Happy coding with 0x0F ORM!
