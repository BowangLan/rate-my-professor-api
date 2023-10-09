# rate-my-professor-api

An unofficial API for ratemyprofessors.com.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Installing

1. Install a Python virtual environment:

   ```
   python -m venv venv
   source ./venv/bin/activate
   ```
   For windows:
   ```
   ./venv/Scripts/activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the scripts

Search school:

```
python -m scripts.search_school <search_query>
```

Search professors:

```
python -m scripts.search_professors <search_query>
```

Get one professor detail:

```
python -m scripts.get_professor_detail <professor_id>
```

Get one school detail:

```
python -m scripts.get_school_detail <school_id>
```
