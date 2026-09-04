# Engineering Journey Academy — Course Tracker

**Curriculum version:** 1.0.0
**Status:** Active
**Current class:** #019
**Last fully verified completed class:** #013
**Backfill verification needed:** #014-#018
**Next class:** #019 — CI Foundations with GitHub Actions

## Completed classes

- [x] #001 Thinking Like a Software Engineer
- [x] #002 Setting Up Your Engineering Workspace Like a Professional
- [x] #003 How Computers Execute Programs
- [x] #004 Computer Networking for Backend Engineers
- [x] #005 Building Your First Flask API
- [x] #006 Flask Application Factory and Blueprints
- [x] #007 Configuration Management with Environment Variables
- [x] #008 Integrating SQLAlchemy and Building Your First Model
- [x] #009 Database Migrations with Alembic
- [x] #010 Repository Pattern
- [x] #011 Service Layer
- [x] #012 Global Error Handling and Safe Database Rollbacks
- [x] #013 Request Validation and Response Schemas with Marshmallow
- [ ] #019 CI Foundations with GitHub Actions

## Learner-reported current position

The learner reports being on Class #019. Repository evidence exists for work after Class #013, including layered tests, factories, schema/error-handler testing notes, coverage strategy notes, and CI workflow work.

Do not mark Classes #014-#018 complete until each class has been verified against its implementation, notes or assignment evidence, tests, coverage, and migration state.

## Existing unnumbered/sub-topic knowledge

Pytest testing was taught extensively as a sub-topic between July 25 and July 27, 2026. The exact source chat is unavailable. Therefore:

- Do not teach pytest as completely new material.
- Class #014 must build on the existing testing foundation.
- Verify the repository's actual tests before changing the test architecture.

## Current project milestone

The Flask backend includes:

- Application factory
- Blueprints
- Environment-based configuration
- SQLAlchemy
- Alembic
- Project model
- Repository layer
- Service layer
- Global error handlers
- Marshmallow request and response schemas
- Existing pytest infrastructure
- Layered test organization and project test factories
- Schema and error-handler tests
- Branch-aware coverage command for CI
- Backend GitHub Actions workflow
- Local class closeout trigger: `make class-check`

## Current curriculum note

The learner reports the current class as #019, and the latest repository evidence is `notes/ci-foundations-github-actions.md` plus `.github/workflows/backend-ci.yml`.

`MASTER_SYLLABUS.md` still lists #019 as Code Quality Tooling and #020 as Continuous Integration. Resolve that syllabus mismatch before marking Class #019 complete.

## Continuation rule

When the learner says `next class`, `continue class`, or `continue course`:

1. Read `CURRICULUM_VERSION.md`.
2. Read this tracker.
3. Read the matching entry in `MASTER_SYLLABUS.md`.
4. Verify `PROJECT_STATE.md`.
5. Continue only with the next incomplete numbered class.

## Update checklist after every class

- [ ] Mark the class completed here.
- [ ] Set the next class.
- [ ] Update `PROJECT_STATE.md`.
- [ ] Add a dated entry to `CHANGELOG.md`.
- [ ] Update persistent memory with the class number and material project changes.
