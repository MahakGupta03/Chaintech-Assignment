# Chaintech-Assignment

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MahakGupta03/Chaintech-Assignment.git
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    env\Scripts\activate  # On Windows
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- Navigate to the home page to register yourself.
- Go to the Users page to view the list of registered users.
