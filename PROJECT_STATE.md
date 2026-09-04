# Engineering Portfolio Platform — Project State

**Curriculum version:** 1.0.0  
**Repository:** `engineering-journey-platform`

## Current backend architecture

```text
HTTP request
    ↓
Marshmallow request schema
    ↓
Flask Blueprint route
    ↓
Service layer
    ↓
Repository layer
    ↓
SQLAlchemy
    ↓
SQLite development database
    ↓
Marshmallow response schema
    ↓
JSON response
```

## Implemented

- [x] Flask application factory
- [x] Blueprints
- [x] Config class and environment variables
- [x] SQLAlchemy integration
- [x] Alembic migrations
- [x] Project model
- [x] Project repository
- [x] Project service
- [x] Global API error handlers
- [x] Database rollback handling
- [x] Marshmallow create, update, and response schemas
- [x] Project CRUD API
- [x] Existing pytest infrastructure from an earlier sub-topic
- [x] Layered backend tests for routes, services, repositories, schemas, and error handlers
- [x] Test project factory helpers
- [x] Backend GitHub Actions workflow for pytest and coverage
- [x] Local class closeout command: `make class-check`

## Current database rule

The canonical development database is:

```text
backend/instance/project.sql
```

Flask and Alembic must use the same absolute SQLite path.

Tests must not use the development database.

## Not yet implemented

- [ ] User accounts
- [ ] Authentication
- [ ] Authorization and RBAC
- [ ] Email verification
- [ ] Password reset
- [ ] Redis
- [ ] Background jobs
- [ ] File/object storage
- [ ] Production deployment
- [ ] React/Next.js frontend
- [ ] Mobile clients
- [ ] AI features

## Current verification state

- Current class reported by learner: Class #019.
- Latest local test run: 72 passed.
- Latest line coverage run: 96%.
- Latest branch-aware CI-equivalent coverage run: 95.02%, above the 80% CI floor.
- Latest `make class-check` run: passed.
- Alembic current/head: `d9a2cc141e6a (head)`.
- Root-level `.coverage` is still tracked and should be removed from Git tracking.
- `ProjectUpdateSchema.validate_and_normalize()` still contains debug output.
- `datetime.utcnow()` deprecation warnings remain in the Project model.
