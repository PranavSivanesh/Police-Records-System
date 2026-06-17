# Police Records System

Police Records System is a Flask web application for managing criminal and officer records. It stores data in CSV files, supports basic record operations, and includes crime-related visual graphs generated with Matplotlib.

## Features

- Dashboard showing total criminal and officer records
- View all criminal records
- Search criminal records by name
- Add new criminal records
- Update existing criminal records
- Delete criminal records
- View all officer records
- Search officer records by name
- Add new officer records
- Update existing officer records
- Delete officer records
- Generate crime-related graphs, including:
  - Most common crime types
  - Crime rate over the years
  - Crimes by emirate
  - Crimes against women
  - Crimes against senior citizens
  - Age distribution of criminals

## Tech Stack

- Python
- Flask
- HTML
- CSS
- CSV file storage
- Matplotlib

## Project Structure

```text
.
|-- app.py
|-- data/
|   |-- criminal.csv
|   `-- officer.csv
|-- static/
|   |-- styles.css
|   `-- images/
|       `-- graph.png
`-- templates/
    |-- base.html
    |-- index.html
    |-- graph.html
    |-- Criminals/
    |   |-- add_criminal.html
    |   |-- criminals.html
    |   |-- delete_criminal.html
    |   |-- search_criminal.html
    |   `-- update_criminal.html
    `-- Officers/
        |-- add_officers.html
        |-- officers.html
        |-- delete_officer.html
        |-- search_officers.html
        `-- update_officers.html
```

## Prerequisites

Before running the project, make sure you have:

- Python 3 installed
- `pip` installed
- A terminal or command prompt

You can check your Python version with:

```bash
python --version
```

## Setup Instructions

1. Clone or download the project.

```bash
git clone <repository-url>
```

2. Move into the project folder.

```bash
cd criminal
```

3. Create a virtual environment.

```bash
python -m venv venv
```

4. Activate the virtual environment.

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

5. Install the required packages.

```bash
pip install flask matplotlib
```

## Running the Application

Start the Flask application with:

```bash
python app.py
```

After the server starts, open this address in your browser:

```text
http://127.0.0.1:5000
```

The application will run in debug mode because `debug=True` is enabled in `app.py`.

## How to Use

1. Open the home page.
2. Use the Criminal Records section to view, search, add, update, or delete criminal records.
3. Use the Officer Records section to view, search, add, update, or delete officer records.
4. Use the Graphs section to view different crime statistics.
5. All changes made through the forms are saved directly into the CSV files.

## Data Storage

The project uses CSV files instead of a database.

`data/criminal.csv` stores criminal records in this format:

```text
ID, Name, Age, Gender, Crime, Place, Date
```

`data/officer.csv` stores officer records in this format:

```text
ID, Name, Age, Gender, Badge, Rank, Station
```

When a new record is added, the application automatically creates the next numeric ID based on the existing records.

## Graphs

Graphs are generated using Matplotlib. When a graph page is opened, the application creates a new chart and saves it as:

```text
static/images/graph.png
```

The graph page then displays this generated image.

## Important Notes

- Keep `criminal.csv` and `officer.csv` inside the `data` folder.
- Do not rename the `templates` or `static` folders because Flask depends on these names.
- The project currently uses CSV files, so it is best suited for small-scale record management or academic/demo use.
- If the CSV files are empty, add records from the web interface before using charts that depend on record data.

## Future Improvements

- Add login authentication
- Add form validation
- Replace CSV files with a database such as SQLite or MySQL
- Add success and error messages after form submissions
- Improve search with partial name matching
- Add export options for records
