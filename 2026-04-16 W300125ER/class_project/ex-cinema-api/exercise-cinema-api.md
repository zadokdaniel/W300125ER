# Exercise: Cinema API

In this exercise you will build a small Django project from scratch.
You will create **one project** and **two apps**, wire up URL routing,
and write a handful of views that return strings, JSON, and a 404
when a resource is not found.pip install Djangopip install Django

There is **no database and no models** — keep all the data as Python
lists/dicts inside each app's `views.py`.

---

## 1. Setup

1. Create a new virtual environment and install Django.
2. Start a new Django project named **`cinema`**.
3. Inside the project, create two apps:
   - **`movies`**
   - **`directors`**
4. Register both apps in `INSTALLED_APPS` (in `cinema/settings.py`).

> Tip: remember the commands `django-admin startproject` and
> `python manage.py startapp`.

---

## 2. URL routing

- In **`cinema/urls.py`**:
  - Route `movies/` → include the `movies` app's URLs.
  - Route `directors/` → include the `directors` app's URLs.
  - Route `''` (the root) → a simple welcome view that returns the
    string: `"Welcome to the Cinema API"`.

- Each app must have its **own** `urls.py` file.

---

## 3. The `movies` app

Use this list as your "database" inside `movies/views.py`:

```python
movies_data = [
    {"id": 1, "title": "Inception",      "year": 2010, "director_id": 1},
    {"id": 2, "title": "The Dark Knight","year": 2008, "director_id": 1},
    {"id": 3, "title": "Pulp Fiction",   "year": 1994, "director_id": 2},
    {"id": 4, "title": "Kill Bill",      "year": 2003, "director_id": 2},
    {"id": 5, "title": "Interstellar",   "year": 2014, "director_id": 1},
]
```

Implement the following endpoints:

| Method | URL                          | Returns                                                     |
|--------|------------------------------|-------------------------------------------------------------|
| GET    | `/movies/hello/`             | `HttpResponse` with the string `"Hello from the movies app!"` |
| GET    | `/movies/`                   | `JsonResvponse` with **all** movies                          |
| GET    | `/movies/<int:id>/`          | `JsonResponse` with the movie that has the matching `id`    |
| GET    | `/movies/by-year/<int:year>/`| `JsonResponse` with all movies released in that year        |

**404 requirement:**
- For `/movies/<int:id>/`, if no movie with that id exists, return a
  **404** response (e.g. via `Http404` or
  `HttpResponse(status=404)`).
- For `/movies/by-year/<int:year>/`, if no movies match, return a
  **404** as well.

---

## 4. The `directors` app

Use this list as your "database" inside `directors/views.py`:

```python
directors_data = [
    {"id": 1, "name": "Christopher Nolan",  "country": "UK"},
    {"id": 2, "name": "Quentin Tarantino",  "country": "USA"},
    {"id": 3, "name": "Hayao Miyazaki",     "country": "Japan"},
]
```

Implement the following endpoints:

| Method | URL                                  | Returns                                                       |
|--------|--------------------------------------|---------------------------------------------------------------|
| GET    | `/directors/`                        | `JsonResponse` with **all** directors                         |
| GET    | `/directors/<int:id>/`               | `JsonResponse` with the matching director, or **404**         |
| GET    | `/directors/by-country/<str:country>/` | `JsonResponse` with all directors from that country, or **404** if none |

---

## 5. Run and test

Run the dev server:

```bash
python manage.py runserver
```

Open the browser (or use `curl`) and verify each route:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/movies/hello/`
- `http://127.0.0.1:8000/movies/`
- `http://127.0.0.1:8000/movies/2/`
- `http://127.0.0.1:8000/movies/999/`  ← should be 404
- `http://127.0.0.1:8000/movies/by-year/2010/`
- `http://127.0.0.1:8000/movies/by-year/1900/` ← should be 404
- `http://127.0.0.1:8000/directors/`
- `http://127.0.0.1:8000/directors/1/`
- `http://127.0.0.1:8000/directors/by-country/USA/`
- `http://127.0.0.1:8000/directors/by-country/Mars/` ← should be 404

---

## Bonus (optional)

1. Add a route `/movies/<int:movie_id>/director/` that returns the
   director (JSON) of the movie with that id. Return 404 if either the
   movie or its director cannot be found.
2. Add a custom path converter that only accepts a 4-digit year (like
   the one shown in class) and use it for `/movies/by-year/<year>/`.
3. Use `name=` on each `path(...)` and try reversing a URL with
   `reverse()` from the Django shell.
