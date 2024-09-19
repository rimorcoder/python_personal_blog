# Personal Blog

https://roadmap.sh/projects/personal-blog

This is a demo personal blog application built with Flask. Follow the instructions below to set up and run the application on your local machine.

For demo purposes only! This should not be used in any production capacity. 

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed [Python](https://www.python.org/downloads/) 

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/rimorcoder/python_personal_blog.git
    cd personal-blog
    ```

2. **Create a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Set Environment Variables

Set the `SECRET_KEY` environment variable. This key is used for cryptographic signing in your application.

For Windows:
```sh
set SECRET_KEY=your_secret_key
```

For Unix-based systems (Linux, macOS):
```sh
export SECRET_KEY='your_secret_key'
```


## Running the Application
Start the development server:
```
python .\run.py
```

This will populate the sql database with fake blog data, as well as create an admin account for managing the blogs with the super secure credentials of:
```
username: admin
password: password
```

Open your web browser and go to `http://127.0.0.1:8000/` to see the application in action.
