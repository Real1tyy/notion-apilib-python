# NotionLibrary
more information can be found here: [Notion-Project-Notebook](https://www.notion.so/NotionLibrary-6338b0ae6eab4327b58e509540f68e2e?pvs=4)

## Outline
NotionLibrary serves as an API library, wrapping the REST API calls that utilize requests to Notion calling ("https://api.notion.com/v1/"...).
So this provides the ability with work with Notion data directly utilizing data classes instead of json format.
#### Other functionality:
1.  adding here automated creations of pages.
2. Data rows formatting to make the values consistent.
3. Properties propagation.
4. Sub-pages and Parent pages communication and exchange of properties


## Requirements
Although the env or venv directory is not included in the version control, the list of dependencies (usually in requirements.txt or Pipfile for pipenv, or pyproject.toml for poetry) should be. This allows anyone cloning the repository on a different computer to recreate the exact environment by installing the dependencies listed in these files.

#### Steps:
1. Format requirements.txt with the dependencies from pip in env/
You can generate a requirements.txt file that lists all the packages installed in the virtual environment along with their versions using the following command:
```bash
pip freeze > requirements.txt
```
Then, someone else can recreate the environment by first creating a new virtual environment on their system and then running:
```bash
pip install -r requirements.txt
```
This ensures that the exact versions of the packages used in the project are installed, making it much easier to achieve consistent behavior across different setups.
