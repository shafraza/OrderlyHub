# OrderlyHub: Django Inventory and Order Management System

Welcome to OrderlyHub, the Django Inventory and Order Management System! This project provides a REST API for managing articles and orders within a business.

## Features

- **Inventory Management**: Allows users to create, edit, and list articles with configurable attributes such as reference, name, description, price, and tax information.
- **Order Management**: Enables users to create, edit, and list orders with associated articles, providing details like total prices with and without taxes.
- **API Endpoints**: Offers RESTful API endpoints for performing CRUD operations on articles and orders, supporting JSON payloads for seamless integration with client applications.
- **Data Validation**: Ensures data integrity by validating inputs and handling errors gracefully to maintain consistency in the database.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development and clean design.
- **Django REST Framework (DRF)**: A powerful toolkit for building Web APIs in Django, providing serialization, authentication, and permission classes.
- **MySQL Database**: A robust and widely used relational database management system for storing and retrieving data efficiently.
- **Python 3**: The programming language used for writing the backend logic and API endpoints.
- **Docker**: A containerization platform that simplifies the deployment process by packaging applications and their dependencies into containers.

## Hexagonal Architecture

OrderlyHub follows the principles of hexagonal architecture to achieve a modular, flexible, and testable design. Here's how the architecture is reflected in the project's code structure:

- **Core Business Logic**: Represented by models, views, and other components within the Django app. This is where essential business rules and operations, such as managing articles and orders, reside.

- **Ports (Interfaces)**: Correspond to the API endpoints defined in views. These endpoints act as ports through which external systems, like clients consuming the API, interact with the application.

- **Adapters**:
  - **Serializers**: Located in "serializers.py" files, these adapters translate data between the core business logic (models) and external systems (API clients).
  - **Views**: Serve as adapters by handling HTTP requests and responses. They translate incoming HTTP requests into method calls on the core business logic and outgoing responses into HTTP responses.
  - **Database Adapters**: Represented by Django's ORM, these adapters connect the core business logic to the database, allowing data persistence and retrieval.

- **Independence of Frameworks**: The core business logic remains independent of any specific frameworks or technologies. It's encapsulated within the Django app's models and views, enabling easier migration, testing, and evolution of the system.

- **Testability**: Hexagonal architecture promotes testability by isolating the core business logic from external dependencies. You can write unit tests for models and views without needing to involve external systems like databases or APIs.

By adhering to hexagonal architecture principles, OrderlyHub achieves a modular, flexible, and testable design, with clear separation of concerns between the core business logic and external interfaces.


## Setup Instructions

### Docker

To set up and run OrderlyHub using Docker, follow these steps:

1. **Clone the Repository**: 
git clone https://github.com/shafraza/OrderlyHub.git
cd OrderlyHub

2. **Build Docker Image**: 
docker build -t orderlyhub .


3. **Run Docker Container**:
docker run -p 8000:8000 orderlyhub


4. **Access the API**:
Visit `http://127.0.0.1:8000/api/` in your browser to access the API endpoints for managing articles and orders.


## API Documentation

- **Articles Endpoint**: 
- `GET /api/items/`: List all articles.
- `POST /api/items/`: Create a new article.
- `GET /api/items/<id>/`: Retrieve details of a specific article.
- `PUT /api/items/<id>/`: Update details of a specific article.
- `DELETE /api/items/<id>/`: Delete a specific article.

- **Orders Endpoint**: 
- `GET /api/orders/`: List all orders.
- `POST /api/orders/`: Create a new order.
- `GET /api/orders/<id>/`: Retrieve details of a specific order.
- `PUT /api/orders/<id>/`: Update details of a specific order.

For detailed request and response formats, please refer to the API documentation available at `http://127.0.0.1:8000/api/docs/` when the server is running.

## Contributors

- Shafaqat Ali (@shafraza): Software Engineer


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
