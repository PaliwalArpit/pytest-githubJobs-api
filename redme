# Pytest API testing framework

Pytest is the python based testing library used to automate testing for UI and backend.

## Installation locally

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the pytest.

```bash
pip install pytest
```
Use requests python library to make API calls

```bash
pip install requests
```

```bash
pip install -r requirement.txt
```

Run tests
```
pytest Tests/ Tests/githubApiTests.py
```
## Installation in venv

```bash
python3 -m venv env
source ./env/bin/activate 
```

Install dependencies by running
```
pip install -r requirement.txt
```

Run tests
```
pytest Tests/ Tests/githubApiTests.py
```
## Usage

```python
import pytest
import requests
response = requests.get(get_base_url + "/positions.json?description=testing&location=berlin")
assert response.status_code == 200

```
## Run test

```bash
pytest Tests/githubApiTests.py 

```
