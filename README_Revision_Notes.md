# Python, Conda, MongoDB & Logging Revision Notes

## Conda vs `venv`

  -----------------------------------------------------------------------
  `venv`                              `conda`
  ----------------------------------- -----------------------------------
  Built into Python                   Requires Anaconda/Miniconda

  Manages Python packages             Manages Python packages + Python
                                      versions + native libraries

  Uses `pip`                          Uses `conda` (and optionally `pip`)

  Lightweight                         Larger but more powerful

  Best for MLOps, Docker, CI/CD       Best for Data Science, ML, GPU
                                      environments
  -----------------------------------------------------------------------

**Flow** 1. Create environment 2. Activate environment 3. Install
packages 4. Run project

### venv

``` bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Conda

``` bash
conda create -n myenv python=3.11
conda activate myenv
pip install -r requirements.txt
conda deactivate
```

### Useful flags

-   `-n` = `--name` (environment name)
-   `-r` = `--requirement` (read packages from a file)
-   `-e .` = Install the current project in editable mode.

### Why `conda init powershell`?

It modifies the PowerShell profile so `conda activate` can change the
PATH, set Conda environment variables, and update the prompt.

------------------------------------------------------------------------

# pyproject.toml

Modern Python project's central configuration file.

It can define: - Project metadata - Dependencies - Build system - Tool
configurations (Black, Pytest, Ruff, etc.)

------------------------------------------------------------------------

# MongoDB Atlas

MongoDB Atlas is MongoDB's managed cloud database service.

Hierarchy:

    MongoDB Atlas
        └── Cluster
              └── Database
                    └── Collection
                          └── Document
                                └── Fields

## SQL vs MongoDB

  SQL        MongoDB
  ---------- ------------
  Server     Cluster
  Database   Database
  Table      Collection
  Row        Document
  Column     Field

### Example

``` python
DB_NAME = "Proj1"
COLLECTION_NAME = "Proj1-Data"
```

Database:

    Proj1

Collection:

    Proj1-Data

### Connection URL

    mongodb+srv://username:password@cluster.mongodb.net/

Contains: - Protocol - Username - Password - Cluster address -
Connection options

**Never commit credentials to GitHub. Use environment variables or a
`.env` file.**

### Upload data

``` python
collection.insert_many(data)
```

-   `data` → list of dictionaries
-   Inserts multiple documents
-   Returns inserted document IDs

------------------------------------------------------------------------

# Logging

Purpose: - Save application events - Help debugging - Record errors

## Components

``` python
logging
```

Built-in logging module.

``` python
RotatingFileHandler
```

Rotates logs after reaching a size limit.

``` python
from_root()
```

Returns the project root directory.

``` python
logger = logging.getLogger()
```

Creates the logger.

``` python
logger.setLevel(logging.DEBUG)
```

Minimum logging level accepted.

Levels:

-   DEBUG
-   INFO
-   WARNING
-   ERROR
-   CRITICAL

``` python
logging.Formatter(...)
```

Controls log message format.

``` python
StreamHandler()
```

Logs to the terminal.

``` python
RotatingFileHandler(...)
```

Logs to a file.

``` python
logger.addHandler(...)
```

Connects handlers to the logger.

Flow:

    logging.info()
          │
          ├── Terminal
          └── Log File
