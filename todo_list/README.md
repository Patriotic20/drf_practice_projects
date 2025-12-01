# Todo API — Example Usage

Below are example `curl` commands for interacting with your Todo API.

## 📌 Create a Todo

```bash
curl -X POST http://127.0.0.1:8000/api/todos/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn DRF", "description": "Complete tutorial"}'
```

## 📌 Get All Todos

```bash
curl http://127.0.0.1:8000/api/todos/
```

## 📌 Get Only Completed Todos

```bash
curl http://127.0.0.1:8000/api/todos/?completed=true
```

## 📌 Update a Todo

```bash
curl -X PUT http://127.0.0.1:8000/api/todos/1/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn DRF", "description": "Almost done!", "completed": true}'
```

## 📌 Delete a Todo

```bash
curl -X DELETE http://127.0.0.1:8000/api/todos/1/
```
