# Fund-Flow App

## About

Fund-Flow is a console-based crowd-funding application developed in Python. It provides a simple, interactive command-line interface for managing crowd-funding campaigns, allowing users to create projects, view existing ones, and manage contributions.

## Features

* **User Authentication**: Secure user registration and login.

* **Project Management**:

    * Create new crowd-funding projects with details like title, description, total target, and start/end dates.

    * View all available projects.

    * Edit owned projects

    * Delete owned projects.

    * Search for projects by date.

## Demo

Watch a short video demonstration of the Fund-Flow App in action:

<video src="./demo_video.mov" controls autoplay loop muted width="100%"></video>

## Technologies Used

* **Python 3.13**: The core programming language.

* **[Poetry](https://python-poetry.org/)**: For dependency management and virtual environment setup.

## Setup and Installation

Follow these steps to get a local copy up and running on your machine.

### Prerequisites

* Python 3.x installed on your system.

* Poetry installed on your system.

    **Installing Poetry:**

    * **macOS / Linux / WSL:**

        ```bash
        curl -sSL https://install.python-poetry.org | python3 -
        ```

    * **Windows (PowerShell):**

        ```powershell
        (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
        ```

        *Note: After installation, you might need to add Poetry to your PATH. The installer usually prompts you for this, or you can find instructions in the [Poetry](https://python-poetry.org/) documentation.*

### Steps

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Naira98/Fund-Flow.git
    cd Fund-Flow
    ```

2.  **Install dependencies and create the virtual environment using Poetry:**

    ```bash
    poetry install
    ```

3.  **Activate the Poetry shell:**

    ```bash
    poetry shell
    ```

### Configuring VS Code

To ensure VS Code uses the correct Python interpreter from your Poetry virtual environment for linting, debugging, and running your scripts, follow these steps:

1.  **Open the Command Palette** (`Ctrl+Shift+P` or `Cmd+Shift+P`).

2.  Type `Python: Select Interpreter` and choose it.

3.  Select the interpreter path pointing to your Poetry environment, typically `./.venv/bin/python` (macOS/Linux/WSL) or `.\.venv\Scripts\python.exe` (Windows). If not found, select `Enter interpreter path...` and manually provide it.

## Usage

Once the application is set up and the Poetry shell is activated, you can run the main script.

1.  **Run the application:**

    ```bash
    python3 app.py
    ```

2.  Follow the on-screen prompts to navigate through the application, register, log in, create projects, or view existing ones.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the LICENSE file for details.
