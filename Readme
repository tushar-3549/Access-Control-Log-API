## Technical Task: Simple Access Control Log API

This project logs door access events using Django REST Framework.

### Setup

1. Clone repository
```bash
git clone https://github.com/tushar-3549/Access-Control-Log-API
cd Access-Control-Log-API
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Migrate database
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run server
```bash
python manage.py runserver
```

6. Test APIs with Postman or curl:

POST: `http://127.0.0.1:8000/api/logs/`
```json
{
  "card_id": "C1001",
  "door_name": "Main Entrance",
  "access_granted": true
}
```

- GET: `http://127.0.0.1:8000/api/logs/`

- GET single: `http://127.0.0.1:8000/api/logs/1/`

- PUT: `http://127.0.0.1:8000/api/logs/1/`

- DELETE: `http://127.0.0.1:8000/api/logs/1/`

- Filter: `http://127.0.0.1:8000/api/logs/?card_id=C1001`

7. Check `system_events.log` for create/delete entries.

```
[2026-01-07 19:35:15] - CREATE: Access log created for card C1001. Status: GRANTED.
[2026-01-07 19:38:00] - DELETE: Access log (ID: 1) for card C1001 was deleted.
```

**Docker**
```bash
docker build -t access_control .
docker run -p 8000:8000 access_control
```
