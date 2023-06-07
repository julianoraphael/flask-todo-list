# Flask Todo List

This is a simple Todo List application built with Flask.

## Installation

### Prerequisites
- Python 3.x
- pip package manager (usually comes with Python)

### Clone the repository

git clone https://github.com/your-username/flask-todo-list.git
cd flask-todo-list


### Install dependencies
pip install -r requirements.txt


## Usage

### Running with Docker

1. Build the Docker image:

docker build -t flask-todo-list .


2. Run the Docker container:

docker run -d -p 5000:5000 flask-todo-list


3. Access the application in your browser at [http://localhost:5000](http://localhost:5000).

### Running with Docker Compose

1. Make sure Docker Compose is installed on your system.

2. Run the application using Docker Compose:

docker-compose up -d

3. Access the application in your browser at [http://localhost:5000](http://localhost:5000).

### Running directly with Python

1. Activate the virtual environment (optional but recommended):

source venv/bin/activate


2. Run the application:

python app.py


3. Access the application in your browser at [http://localhost:5000](http://localhost:5000).

## Contributing

Contributions are welcome! If you find any issues or want to enhance the application, feel free to open a pull request.

## License

This project is licensed under the MIT License.
