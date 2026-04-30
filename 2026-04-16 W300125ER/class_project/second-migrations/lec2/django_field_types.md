# Django Model Field Types

Quick reference for every built-in `models.*` field, when to use it, how the DB stores it, the parameters you'll actually reach for, and (for relations) the connection type.

---

## String / Text Fields

| Field | When to use it | DB representation | Important parameters | Relation |
|---|---|---|---|---|
| `CharField` | Short, bounded strings (names, titles, labels) | `VARCHAR(max_length)` | `max_length` (**required**), `blank`, `null`, `default`, `unique`, `db_index`, `choices` | — |
| `TextField` | Long / unbounded text (descriptions, articles, comments) | `TEXT` | `blank`, `null`, `default`, `max_length` (form-only, not DB) | — |
| `SlugField` | URL-safe short labels (`my-post-title`) | `VARCHAR(max_length)` (default 50) | `max_length`, `unique`, `allow_unicode`, `db_index` (default `True`) | — |
| `EmailField` | Email addresses (adds email validator) | `VARCHAR(254)` by default | `max_length`, `unique` | — |
| `URLField` | Web URLs (adds URL validator) | `VARCHAR(200)` by default | `max_length` | — |

---

## Numeric Fields

| Field | When to use it | DB representation | Important parameters | Relation |
|---|---|---|---|---|
| `IntegerField` | Standard whole numbers (-2.1B … 2.1B) | `INTEGER` | `default`, `null`, `validators`, `choices` | — |
| `BigIntegerField` | Very large whole numbers (-9.2 quintillion … 9.2 quintillion) | `BIGINT` | same as Integer | — |
| `SmallIntegerField` | Small whole numbers (-32k … 32k) — saves space | `SMALLINT` | same as Integer | — |
| `PositiveIntegerField` | Counts, quantities, IDs that can never be negative | `INTEGER` (with check ≥ 0) | same as Integer | — |
| `PositiveSmallIntegerField` | Small non-negative values (age, rating 1–5) | `SMALLINT` (with check ≥ 0) | same as Integer | — |
| `PositiveBigIntegerField` | Huge non-negative values | `BIGINT` (with check ≥ 0) | same as Integer | — |
| `FloatField` | Approximate decimal numbers (scientific data) — **never** for money | `DOUBLE PRECISION` / `REAL` | `default`, `null` | — |
| `DecimalField` | Exact decimals — **money**, precise measurements | `NUMERIC(max_digits, decimal_places)` | `max_digits` (**required**), `decimal_places` (**required**) | — |
| `AutoField` | Auto-incrementing integer PK (Django adds one if you don't define a PK) | `INTEGER AUTO_INCREMENT` / `SERIAL` | `primary_key=True` | — |
| `BigAutoField` | Auto-incrementing PK for huge tables (Django default since 3.2) | `BIGINT AUTO_INCREMENT` / `BIGSERIAL` | `primary_key=True` | — |
| `SmallAutoField` | Auto-incrementing PK for small reference tables | `SMALLINT AUTO_INCREMENT` | `primary_key=True` | — |

---

## Boolean

| Field | When to use it | DB representation | Important parameters | Relation |
|---|---|---|---|---|
| `BooleanField` | True/False flags (`is_active`, `is_published`) | `BOOLEAN` (or `TINYINT(1)` on MySQL) | `default`, `null` (allows nullable boolean instead of the deprecated `NullBooleanField`) | — |

---

## Date / Time

| Field | When to use it | DB representation | Important parameters | Relation |
|---|---|---|---|---|
| `DateField` | Calendar dates (birthdays, due dates) | `DATE` | `auto_now` (set on every save), `auto_now_add` (set once on create), `default` | — |
| `DateTimeField` | Timestamps (`created_at`, `updated_at`) | `DATETIME` / `TIMESTAMP` | `auto_now`, `auto_now_add`, `default=timezone.now` | — |
| `TimeField` | Time of day (opening hours) | `TIME` | `auto_now`, `auto_now_add` | — |
| `DurationField` | A length of time (`timedelta`) | `INTERVAL` (Postgres) / `BIGINT` microseconds (others) | `default` | — |

> ⚠️ `auto_now` and `auto_now_add` are mutually exclusive with each other and with `default`.

---

## Files / Binary

| Field | When to use it | DB representation | Important parameters | Relation |
|---|---|---|---|---|
| `FileField` | Uploaded files (PDFs, docs) — file lives on disk/S3, only path stored | `VARCHAR(100)` (path) | `upload_to`, `storage`, `max_length` | — |
| `ImageField` | Same as `FileField` but validates it's an image (requires Pillow) | `VARCHAR(100)` (path) | `upload_to`, `height_field`, `width_field` | — |
| `FilePathField` | Pick from existing files in a server directory | `VARCHAR(max_length)` | `path` (**required**), `match`, `recursive`, `allow_files`, `allow_folders` | — |
| `BinaryField` | Raw binary blob (small) — discouraged, prefer `FileField` | `BLOB` / `BYTEA` | `max_length`, `editable` (default `False`) | — |

---

## Identifiers / Network

| Field | When to use it | DB representation | Important parameters | Relation |
|---|---|---|---|---|
| `UUIDField` | Globally unique IDs (better PK than int when exposing IDs publicly) | `UUID` (Postgres) / `CHAR(32)` | `default=uuid.uuid4`, `primary_key`, `unique` | — |
| `GenericIPAddressField` | IPv4 and/or IPv6 addresses | `CHAR(39)` (or `INET` on Postgres) | `protocol` (`'both'`/`'IPv4'`/`'IPv6'`), `unpack_ipv4` | — |

---

## Structured Data

| Field | When to use it | DB representation | Important parameters | Relation |
|---|---|---|---|---|
| `JSONField` | Schemaless / nested data (settings, payloads, tags) | `JSONB` (Postgres) / `JSON` (MySQL/Oracle) / `TEXT` (SQLite) | `default=dict`/`list`, `encoder`, `decoder` | — |

---

## Relationship Fields

| Field | When to use it | DB representation | Important parameters | Relation type |
|---|---|---|---|---|
| `ForeignKey` | "Many of THIS belong to one of THAT" (a `Choice` belongs to one `Question`) | Column on this table holding the FK to the other table's PK (e.g. `question_id INTEGER REFERENCES question(id)`) | `to` (target model, **required**), `on_delete` (**required**: `CASCADE`, `PROTECT`, `SET_NULL`, `SET_DEFAULT`, `SET(...)`, `DO_NOTHING`, `RESTRICT`), `related_name`, `related_query_name`, `null`, `blank`, `limit_choices_to`, `db_index` (default `True`) | **Many-to-One (N:1)** |
| `OneToOneField` | Extending another model 1-to-1 (a `Profile` for one `User`) | Same as `ForeignKey` but with a `UNIQUE` constraint on the FK column | `to` (**required**), `on_delete` (**required**), `parent_link`, `related_name`, `null`, `blank` | **One-to-One (1:1)** |
| `ManyToManyField` | Many on each side (a `Post` has many `Tag`s, a `Tag` is on many `Post`s) | **Separate join table** with two FKs (no column on either side's table) | `to` (**required**), `through` (custom join model), `through_fields`, `related_name`, `symmetrical` (only for self-referential), `blank`, `db_table` | **Many-to-Many (N:N)** |

### `on_delete` cheat sheet (FK / OneToOne)

| Value | What happens when the referenced row is deleted |
|---|---|
| `CASCADE` | Delete this row too (most common for "owned" data) |
| `PROTECT` | Raise `ProtectedError` — block the deletion |
| `RESTRICT` | Like `PROTECT` but lighter; allows the cascade if a different path also deletes this row |
| `SET_NULL` | Set this FK to `NULL` (requires `null=True`) |
| `SET_DEFAULT` | Set to the field's `default` (requires a default) |
| `SET(value_or_callable)` | Set to a specific value |
| `DO_NOTHING` | Do nothing — you'd better handle integrity yourself |

---

## Universal Parameters (work on almost every field)

| Parameter | Purpose |
|---|---|
| `null` | Allow `NULL` in DB. Default `False`. Avoid on string fields — use `blank` instead. |
| `blank` | Allow empty value in **forms/validation** (not the DB). Default `False`. |
| `default` | Default value (literal or callable like `timezone.now`). |
| `unique` | Add a `UNIQUE` constraint. |
| `db_index` | Add a DB index on this column. |
| `primary_key` | Make this the PK (Django auto-adds an `id` PK if none is set). |
| `choices` | Restrict to a fixed set of values (great with `TextChoices` / `IntegerChoices`). |
| `editable` | If `False`, hidden from admin/forms. |
| `help_text` | Shown in forms and admin. |
| `verbose_name` | Human-readable name. |
| `validators` | List of custom validator callables. |
| `db_column` | Override the DB column name. |

---

## Quick "which one do I pick?" guide

- **Money?** → `DecimalField(max_digits=…, decimal_places=2)`. Never `FloatField`.
- **Short string?** → `CharField(max_length=…)`. **Long string?** → `TextField`.
- **Created/updated timestamps?** → `DateTimeField(auto_now_add=True)` and `DateTimeField(auto_now=True)`.
- **Belongs to one parent?** → `ForeignKey(Parent, on_delete=models.CASCADE)`.
- **Extends another row 1:1?** → `OneToOneField`.
- **Tags / categories / many on both sides?** → `ManyToManyField`.
- **Public-facing ID?** → `UUIDField(primary_key=True, default=uuid.uuid4, editable=False)`.
- **Flexible/nested data?** → `JSONField` (defaults to `dict` or `list`).
