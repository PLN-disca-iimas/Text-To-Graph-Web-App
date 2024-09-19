# Text-To-Graph Web App

This is a web application that converts text into a graph representation.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/diegoavendano1998/Text-To-Graph-Web-App.git
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## API Routes

The following API routes are available:

- `/test/` (GET): This route returns the result of the 'get_test' method from the GraphTextService. It's implemented in the test function.

- `/` (GET): This route redirects to the 'graph_form' route. It's implemented in the index function.

- `/graph-form/` (GET): This route renders the graph form template. It's implemented in the graph_form function.

- `/generate-graph/` (POST): This route generates a graph based on the form data and file uploaded. It redirects to the 'graph_form' route if the graph generation fails, otherwise, it redirects to the 'graph_plot' route with the generated graph's document name. It's implemented in the generate_graph function.

- `/graph-plot/<docname>` (GET): This route renders the graph plot template and passes the necessary variables for displaying the graph. It's implemented in the graph_plot function.


## Libraries and Tech Stack

This project is built using the following libraries and technologies:

- Python
- Flask: A lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
- NetworkX: A Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
- Text to Graph API: A Python package for generating co-occurrence graphs from a corpus of documents.
- nltk: The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing for English written in the Python programming language.
- Matplotlib - a plotting library for creating static, animated, and interactive visualizations in Python.

## Usage

To start the web application, run the following command:
1. Activate the virtual environment:
    On Windows, use:
    ```bash
    source venv/bin/activate
    ```
    On Unix or MacOS, use:
    ```bash
    venv\Scripts\activate
    ```

2. To run the application, use the following command:

    ```bash
    python app.py
    ```

3. Generate test graph in http://0.0.0.0:5000/test
