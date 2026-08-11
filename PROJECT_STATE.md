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

## Verification required before Class #014

Because the historical testing chat is unavailable, inspect the repository and record:

- Existing test files
- Existing fixtures
- Test database strategy
- Current passing test count
- Coverage tooling and latest report
- Untested layers and branches
