# conference-viz API

## Requirements

Make sure you have Python 3.8+ installed.

### Setup Instructions

Open your terminal or command prompt and run the following commands :

```bash
# Create a virtual environment
python3 -m venv confviz-env

# Activate the virtual environment
source confviz-env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Application

To start the application :

```bash
python app.py
```

## API Documentation

You can access the API documentation via Swagger Docs once the app is running.

## API Endpoints

### Conference Details

- `GET /conferences` - Get all conferences
- `GET /conference/<string:_id>` - Get a specific conference by ID

### Acceptance Rates

- `GET /conferences/acceptance-rates` - Get acceptance rates for all conferences
- `GET /conference/<string:_id>/acceptance-rate` - Get acceptance rate for a specific conference

### Keywords

- `GET /conferences/keywords` - Get keywords for all conferences
- `GET /conference/<string:_id>/keywords` - Get keywords for a specific conference

### Papers

- `GET /conferences/papers` - Get all papers for all conferences
- `GET /conference/<string:_id>/papers` - Get papers for a specific conference

---
