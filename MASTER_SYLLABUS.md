# Engineering Journey Academy — Master Syllabus

**Curriculum version:** 1.0.0  
**Primary project:** `engineering-journey-platform`  
**Current class:** #014  
**Last completed class:** #013

## Authority and reconstruction notice

Classes #001–#013 are based on the learner's authoritative record.

Class #014 onward is the versioned forward curriculum reconstructed from the recovered roadmap and stated academy goals. It is not represented as a verbatim recovery of missing chat history. Future changes must be recorded in `CHANGELOG.md` and follow semantic curriculum versioning.

## Class format

Every class should contain:

1. Lesson goal
2. Explanation
3. Code or practical task
4. Assignment
5. Testing requirements where applicable
6. Project-state update
7. What to do next

---

## Class #001 — Thinking Like a Software Engineer

**Status:** ✅ Completed

**Topics**
- Engineering mindset
- systems thinking
- decomposition
- professional problem-solving.

**Project/Lab Deliverable**
- Write engineering reflection notes.


## Class #002 — Setting Up Your Engineering Workspace Like a Professional

**Status:** ✅ Completed

**Topics**
- Terminal workflow
- Git history
- repository organization
- professional commits.

**Project/Lab Deliverable**
- Create the academy repository structure and commit it.


## Class #003 — How Computers Execute Programs

**Status:** ✅ Completed

**Topics**
- Source code
- compilation
- interpretation
- memory
- variables
- Python versus Go execution.

**Project/Lab Deliverable**
- Run and compare small Python and Go programs.


## Class #004 — Computer Networking for Backend Engineers

**Status:** ✅ Completed

**Topics**
- Client/server
- DNS
- HTTP
- requests
- responses
- JSON
- APIs.

**Project/Lab Deliverable**
- Inspect and explain a real HTTP request.


## Class #005 — Building Your First Flask API

**Status:** ✅ Completed

**Topics**
- Virtual environments
- dependencies
- Flask server
- routes
- curl.

**Project/Lab Deliverable**
- Create root and health endpoints.


## Class #006 — Flask Application Factory and Blueprints

**Status:** ✅ Completed

**Topics**
- Application factory
- modular routing
- Blueprints
- scalable structure.

**Project/Lab Deliverable**
- Refactor the Flask application.


## Class #007 — Configuration Management with Environment Variables

**Status:** ✅ Completed

**Topics**
- .env files
- config classes
- secrets
- development versus production settings.

**Project/Lab Deliverable**
- Add environment-driven configuration.


## Class #008 — Integrating SQLAlchemy and Building Your First Model

**Status:** ✅ Completed

**Topics**
- ORM concepts
- Flask-SQLAlchemy
- database URI
- Project model.

**Project/Lab Deliverable**
- Create and register the Project model.


## Class #009 — Database Migrations with Alembic

**Status:** ✅ Completed

**Topics**
- Schema versioning
- autogenerate
- upgrade
- downgrade
- revision tracking.

**Project/Lab Deliverable**
- Create and apply the initial migration.


## Class #010 — Repository Pattern

**Status:** ✅ Completed

**Topics**
- Persistence abstraction
- CRUD repositories
- separation from HTTP.

**Project/Lab Deliverable**
- Create ProjectRepository.


## Class #011 — Service Layer

**Status:** ✅ Completed

**Topics**
- Business rules
- orchestration
- dependency injection
- thin routes.

**Project/Lab Deliverable**
- Create ProjectService and CRUD flows.


## Class #012 — Global Error Handling and Safe Rollbacks

**Status:** ✅ Completed

**Topics**
- Application errors
- HTTP mapping
- rollback
- safe 500 responses.

**Project/Lab Deliverable**
- Centralize error handlers.


## Class #013 — Request Validation and Response Schemas with Marshmallow

**Status:** ✅ Completed

**Topics**
- Load/dump
- create/update schemas
- URL validation
- unknown fields.

**Project/Lab Deliverable**
- Add project request and response schemas.


## Class #014 — Testing the Layered Flask Architecture

**Status:** ⏭ Next

**Topics**
- Use the existing pytest foundation to organize tests by schema, service, repository, route, and error-handler layers.

**Project/Lab Deliverable**
- Create a layered test matrix and fill critical gaps.


## Class #015 — Service Unit Tests with Fakes and Parametrization

**Status:** ⬜ Planned

**Topics**
- Fake repositories
- pytest.raises
- parametrization
- business-rule tests.

**Project/Lab Deliverable**
- Unit-test ProjectService without Flask or a database.


## Class #016 — Repository Integration Tests

**Status:** ⬜ Planned

**Topics**
- Temporary SQLite database
- CRUD verification
- constraints
- transaction behavior.

**Project/Lab Deliverable**
- Build repository integration tests.


## Class #017 — Schema and Error-Handler Testing

**Status:** ⬜ Planned

**Topics**
- Marshmallow edge cases
- error response contracts
- unexpected-error safety.

**Project/Lab Deliverable**
- Test validation details and global handlers.


## Class #018 — Coverage Strategy and Test Quality

**Status:** ⬜ Planned

**Topics**
- Line versus branch coverage
- meaningful assertions
- test smells
- coverage gates.

**Project/Lab Deliverable**
- Establish a justified coverage threshold.


## Class #019 — Code Quality Tooling

**Status:** ⬜ Planned

**Topics**
- Formatting
- linting
- import sorting
- type-checking foundations.

**Project/Lab Deliverable**
- Configure Ruff/Black or equivalent tools.


## Class #020 — Continuous Integration for the Flask Backend

**Status:** ⬜ Planned

**Topics**
- GitHub Actions
- test and lint jobs
- coverage artifacts
- required checks.

**Project/Lab Deliverable**
- Create the first CI workflow.


## Class #021 — User Model and Identity Design

**Status:** ⬜ Planned

**Topics**
- User schema
- email uniqueness
- timestamps
- account states.

**Project/Lab Deliverable**
- Add the User model and migration.


## Class #022 — Password Hashing and Credential Safety

**Status:** ⬜ Planned

**Topics**
- Hashing
- salts
- password policy
- secure verification.

**Project/Lab Deliverable**
- Implement password hashing utilities and tests.


## Class #023 — User Registration

**Status:** ⬜ Planned

**Topics**
- Registration schema
- duplicate accounts
- service and repository flow.

**Project/Lab Deliverable**
- Create POST /auth/register.


## Class #024 — User Login

**Status:** ⬜ Planned

**Topics**
- Credential verification
- safe errors
- login tests.

**Project/Lab Deliverable**
- Create POST /auth/login.


## Class #025 — JWT Access Tokens

**Status:** ⬜ Planned

**Topics**
- JWT structure
- claims
- signing
- expiration
- protected routes.

**Project/Lab Deliverable**
- Issue and validate access tokens.


## Class #026 — Refresh Tokens

**Status:** ⬜ Planned

**Topics**
- Refresh flow
- rotation
- expiry
- revocation risks.

**Project/Lab Deliverable**
- Implement refresh-token endpoint.


## Class #027 — Token Revocation and Blacklisting

**Status:** ⬜ Planned

**Topics**
- Logout semantics
- token identifiers
- blacklist persistence.

**Project/Lab Deliverable**
- Implement secure logout.


## Class #028 — Email Verification

**Status:** ⬜ Planned

**Topics**
- Verification tokens
- account activation
- resend flow.

**Project/Lab Deliverable**
- Add email-verification workflow.


## Class #029 — Password Reset

**Status:** ⬜ Planned

**Topics**
- Reset requests
- expiring tokens
- safe responses.

**Project/Lab Deliverable**
- Implement reset request and confirmation.


## Class #030 — Role-Based Access Control

**Status:** ⬜ Planned

**Topics**
- Roles
- permissions
- decorators
- service-level authorization.

**Project/Lab Deliverable**
- Protect administrative endpoints.


## Class #031 — Authentication and Authorization Test Suite

**Status:** ⬜ Planned

**Topics**
- Unit, integration, security, and failure-path tests.

**Project/Lab Deliverable**
- Complete auth regression coverage.


## Class #032 — Project Ownership and User Relationships

**Status:** ⬜ Planned

**Topics**
- One-to-many relationships
- foreign keys
- ownership rules.

**Project/Lab Deliverable**
- Attach projects to users.


## Class #033 — SQL Constraints and Data Integrity

**Status:** ⬜ Planned

**Topics**
- Unique, check, not-null, foreign-key constraints.

**Project/Lab Deliverable**
- Enforce integrity in migrations and tests.


## Class #034 — Pagination

**Status:** ⬜ Planned

**Topics**
- Limit/offset
- metadata
- page contracts
- boundary cases.

**Project/Lab Deliverable**
- Paginate project listings.


## Class #035 — Filtering and Sorting

**Status:** ⬜ Planned

**Topics**
- Query parameters
- whitelists
- dynamic filters
- deterministic ordering.

**Project/Lab Deliverable**
- Add filtered and sorted project queries.


## Class #036 — Search

**Status:** ⬜ Planned

**Topics**
- Case-insensitive search
- indexed fields
- relevance basics.

**Project/Lab Deliverable**
- Add portfolio project search.


## Class #037 — Database Indexes and Query Plans

**Status:** ⬜ Planned

**Topics**
- Indexes
- EXPLAIN
- trade-offs
- write cost.

**Project/Lab Deliverable**
- Measure and improve a slow query.


## Class #038 — Transactions Across Multiple Repositories

**Status:** ⬜ Planned

**Topics**
- Atomic workflows
- service-owned transactions
- rollback strategy.

**Project/Lab Deliverable**
- Refactor a multi-step operation transactionally.


## Class #039 — Soft Deletion and Auditability

**Status:** ⬜ Planned

**Topics**
- deleted_at
- filtering
- restoration
- audit implications.

**Project/Lab Deliverable**
- Add reversible project deletion.


## Class #040 — Audit Logs

**Status:** ⬜ Planned

**Topics**
- Actor, action, target, metadata, timestamps.

**Project/Lab Deliverable**
- Record critical account and project actions.


## Class #041 — API Versioning and Compatibility

**Status:** ⬜ Planned

**Topics**
- Versioning strategies
- deprecation
- backward compatibility.

**Project/Lab Deliverable**
- Introduce /api/v1.


## Class #042 — REST API Design Review

**Status:** ⬜ Planned

**Topics**
- Resources
- methods
- idempotency
- status codes
- consistency.

**Project/Lab Deliverable**
- Review and standardize API contracts.


## Class #043 — OpenAPI Documentation for Flask

**Status:** ⬜ Planned

**Topics**
- API descriptions
- examples
- error schemas
- discoverability.

**Project/Lab Deliverable**
- Publish machine-readable API documentation.


## Class #044 — Logging and Correlation IDs

**Status:** ⬜ Planned

**Topics**
- Structured logs
- request IDs
- levels
- sensitive data.

**Project/Lab Deliverable**
- Add request-scoped correlation IDs.


## Class #045 — Rate Limiting and Abuse Protection

**Status:** ⬜ Planned

**Topics**
- Limits
- identifiers
- headers
- brute-force protection.

**Project/Lab Deliverable**
- Protect auth and public endpoints.


## Class #046 — Caching with Redis

**Status:** ⬜ Planned

**Topics**
- Cache-aside
- TTL
- invalidation
- serialization.

**Project/Lab Deliverable**
- Cache a read-heavy endpoint.


## Class #047 — Background Jobs

**Status:** ⬜ Planned

**Topics**
- Queues
- retries
- idempotency
- failure handling.

**Project/Lab Deliverable**
- Move email delivery to a background task.


## Class #048 — File Uploads and Object Storage

**Status:** ⬜ Planned

**Topics**
- Multipart requests
- validation
- filenames
- storage abstraction.

**Project/Lab Deliverable**
- Add project image uploads.


## Class #049 — Production Configuration

**Status:** ⬜ Planned

**Topics**
- Environment separation
- secrets
- secure defaults
- startup validation.

**Project/Lab Deliverable**
- Create production config validation.


## Class #050 — Flask Backend Milestone Review

**Status:** ⬜ Planned

**Topics**
- Architecture review
- testing
- security
- documentation
- technical debt.

**Project/Lab Deliverable**
- Release Flask backend v1.


## Class #051 — Relational Database Foundations

**Status:** ⬜ Planned

**Topics**
- Tables
- keys
- normalization
- joins
- transactions.

**Project/Lab Deliverable**
- Model the platform schema on paper.


## Class #052 — PostgreSQL Essentials

**Status:** ⬜ Planned

**Topics**
- Types
- schemas
- psql
- constraints
- JSONB overview.

**Project/Lab Deliverable**
- Run the platform locally on PostgreSQL.


## Class #053 — MySQL Essentials

**Status:** ⬜ Planned

**Topics**
- Storage engines
- types
- indexes
- SQL modes.

**Project/Lab Deliverable**
- Compare MySQL behavior with PostgreSQL.


## Class #054 — Advanced SQL Queries

**Status:** ⬜ Planned

**Topics**
- Joins
- subqueries
- CTEs
- window functions.

**Project/Lab Deliverable**
- Build analytics queries for the portfolio.


## Class #055 — Database Concurrency and Isolation

**Status:** ⬜ Planned

**Topics**
- Locks
- isolation levels
- race conditions
- deadlocks.

**Project/Lab Deliverable**
- Reproduce and fix a concurrency issue.


## Class #056 — Database Backup and Restore

**Status:** ⬜ Planned

**Topics**
- Logical backups
- restore tests
- recovery planning.

**Project/Lab Deliverable**
- Document and test a restore procedure.


## Class #057 — Redis Data Structures

**Status:** ⬜ Planned

**Topics**
- Strings
- hashes
- sets
- sorted sets
- streams.

**Project/Lab Deliverable**
- Implement a small Redis-backed feature.


## Class #058 — Database Performance Project

**Status:** ⬜ Planned

**Topics**
- Profiling
- indexing
- batching
- N+1 prevention.

**Project/Lab Deliverable**
- Produce a database performance report.


## Class #059 — FastAPI Foundations

**Status:** ⬜ Planned

**Topics**
- ASGI
- path operations
- request/response models
- development server.

**Project/Lab Deliverable**
- Create a FastAPI service.


## Class #060 — Pydantic Models and Validation

**Status:** ⬜ Planned

**Topics**
- Typed schemas
- validators
- serialization
- settings.

**Project/Lab Deliverable**
- Model project API contracts with Pydantic.


## Class #061 — FastAPI Dependency Injection

**Status:** ⬜ Planned

**Topics**
- Depends
- reusable dependencies
- request context.

**Project/Lab Deliverable**
- Inject services and repositories.


## Class #062 — SQLAlchemy 2.x with FastAPI

**Status:** ⬜ Planned

**Topics**
- Sessions
- typed models
- repository integration.

**Project/Lab Deliverable**
- Connect FastAPI to PostgreSQL.


## Class #063 — Alembic in FastAPI

**Status:** ⬜ Planned

**Topics**
- Metadata wiring
- migrations
- environment configuration.

**Project/Lab Deliverable**
- Create and apply FastAPI migrations.


## Class #064 — Async Python Fundamentals

**Status:** ⬜ Planned

**Topics**
- Event loop
- await
- blocking work
- concurrency limits.

**Project/Lab Deliverable**
- Compare sync and async endpoints.


## Class #065 — Async Database Access

**Status:** ⬜ Planned

**Topics**
- Async sessions
- transaction scopes
- pitfalls.

**Project/Lab Deliverable**
- Implement an async repository.


## Class #066 — FastAPI Authentication

**Status:** ⬜ Planned

**Topics**
- OAuth2 flows
- JWT
- dependencies
- current user.

**Project/Lab Deliverable**
- Protect FastAPI routes.


## Class #067 — FastAPI Error Handling

**Status:** ⬜ Planned

**Topics**
- Exception handlers
- validation errors
- consistent contracts.

**Project/Lab Deliverable**
- Standardize error responses.


## Class #068 — FastAPI Testing

**Status:** ⬜ Planned

**Topics**
- TestClient
- async tests
- dependency overrides
- fixtures.

**Project/Lab Deliverable**
- Build unit and API tests.


## Class #069 — Background Tasks and WebSockets

**Status:** ⬜ Planned

**Topics**
- Task execution
- real-time communication
- connection lifecycle.

**Project/Lab Deliverable**
- Add a real-time notification prototype.


## Class #070 — FastAPI Observability and Production

**Status:** ⬜ Planned

**Topics**
- Logging
- metrics
- tracing
- workers
- deployment concerns.

**Project/Lab Deliverable**
- Release FastAPI service v1.


## Class #071 — Flask versus FastAPI Architecture Review

**Status:** ⬜ Planned

**Topics**
- Framework trade-offs
- portability of services and repositories.

**Project/Lab Deliverable**
- Document migration and reuse decisions.


## Class #072 — Go Language Foundations

**Status:** ⬜ Planned

**Topics**
- Syntax
- variables
- control flow
- functions
- tooling.

**Project/Lab Deliverable**
- Build command-line exercises.


## Class #073 — Go Packages and Modules

**Status:** ⬜ Planned

**Topics**
- go.mod
- packages
- visibility
- dependency management.

**Project/Lab Deliverable**
- Structure a multi-package service.


## Class #074 — Structs, Methods, and Interfaces

**Status:** ⬜ Planned

**Topics**
- Composition
- interfaces
- behavior-driven design.

**Project/Lab Deliverable**
- Model portfolio entities.


## Class #075 — Errors and Defensive Go

**Status:** ⬜ Planned

**Topics**
- Error values
- wrapping
- sentinel errors
- panic boundaries.

**Project/Lab Deliverable**
- Design service errors.


## Class #076 — HTTP Servers in Go

**Status:** ⬜ Planned

**Topics**
- net/http
- handlers
- routing
- JSON.

**Project/Lab Deliverable**
- Create a Go REST API.


## Class #077 — Middleware and Request Context

**Status:** ⬜ Planned

**Topics**
- Logging
- auth
- recovery
- context cancellation.

**Project/Lab Deliverable**
- Add reusable middleware.


## Class #078 — Bun ORM Foundations

**Status:** ⬜ Planned

**Topics**
- Models
- connections
- queries
- migrations.

**Project/Lab Deliverable**
- Connect Go to PostgreSQL with Bun.


## Class #079 — Repository and Service Layers in Go

**Status:** ⬜ Planned

**Topics**
- Interfaces
- dependency injection
- testability.

**Project/Lab Deliverable**
- Port a project feature to Go.


## Class #080 — Go Validation and API Contracts

**Status:** ⬜ Planned

**Topics**
- Validation strategy
- DTOs
- response consistency.

**Project/Lab Deliverable**
- Validate create/update requests.


## Class #081 — Go Authentication

**Status:** ⬜ Planned

**Topics**
- Password hashing
- JWT
- middleware
- authorization.

**Project/Lab Deliverable**
- Implement protected endpoints.


## Class #082 — Go Concurrency

**Status:** ⬜ Planned

**Topics**
- Goroutines
- channels
- worker pools
- synchronization.

**Project/Lab Deliverable**
- Build a concurrent processing feature.


## Class #083 — Go Context and Graceful Shutdown

**Status:** ⬜ Planned

**Topics**
- Timeouts
- cancellation
- signal handling.

**Project/Lab Deliverable**
- Add graceful server shutdown.


## Class #084 — Go Testing

**Status:** ⬜ Planned

**Topics**
- Table-driven tests
- httptest
- fakes
- integration tests.

**Project/Lab Deliverable**
- Build a complete Go test suite.


## Class #085 — Go Performance and Profiling

**Status:** ⬜ Planned

**Topics**
- Benchmarks
- pprof
- allocations
- optimization.

**Project/Lab Deliverable**
- Profile a slow code path.


## Class #086 — Go Production Service

**Status:** ⬜ Planned

**Topics**
- Configuration
- logs
- metrics
- deployment packaging.

**Project/Lab Deliverable**
- Release Go service v1.


## Class #087 — Go Capstone Microservice

**Status:** ⬜ Planned

**Topics**
- Service boundaries
- events
- API integration.

**Project/Lab Deliverable**
- Integrate a Go service into the platform.


## Class #088 — C# and .NET Foundations

**Status:** ⬜ Planned

**Topics**
- .NET SDK
- C# syntax
- types
- project structure.

**Project/Lab Deliverable**
- Create a .NET console application.


## Class #089 — Object-Oriented C#

**Status:** ⬜ Planned

**Topics**
- Classes
- interfaces
- inheritance
- composition
- records.

**Project/Lab Deliverable**
- Model platform domain objects.


## Class #090 — LINQ and Collections

**Status:** ⬜ Planned

**Topics**
- Queries
- transformations
- deferred execution.

**Project/Lab Deliverable**
- Build data-processing exercises.


## Class #091 — Asynchronous C#

**Status:** ⬜ Planned

**Topics**
- Task
- async/await
- cancellation
- common mistakes.

**Project/Lab Deliverable**
- Implement asynchronous workflows.


## Class #092 — ASP.NET Core Fundamentals

**Status:** ⬜ Planned

**Topics**
- Web API templates
- controllers/minimal APIs
- middleware.

**Project/Lab Deliverable**
- Create an ASP.NET Core API.


## Class #093 — Dependency Injection in ASP.NET Core

**Status:** ⬜ Planned

**Topics**
- Service lifetimes
- registrations
- interfaces.

**Project/Lab Deliverable**
- Wire repositories and services.


## Class #094 — Entity Framework Core

**Status:** ⬜ Planned

**Topics**
- DbContext
- entities
- querying
- change tracking.

**Project/Lab Deliverable**
- Connect to PostgreSQL.


## Class #095 — EF Core Migrations

**Status:** ⬜ Planned

**Topics**
- Migration lifecycle
- deployment
- rollback planning.

**Project/Lab Deliverable**
- Create and apply schema migrations.


## Class #096 — ASP.NET Core Validation and Error Handling

**Status:** ⬜ Planned

**Topics**
- DTO validation
- problem details
- exception middleware.

**Project/Lab Deliverable**
- Standardize API errors.


## Class #097 — ASP.NET Core Authentication

**Status:** ⬜ Planned

**Topics**
- Identity concepts
- JWT
- claims
- policies.

**Project/Lab Deliverable**
- Implement authentication.


## Class #098 — Authorization Policies and Roles

**Status:** ⬜ Planned

**Topics**
- Policy-based authorization
- resource checks.

**Project/Lab Deliverable**
- Protect administrative actions.


## Class #099 — Testing C# Applications

**Status:** ⬜ Planned

**Topics**
- xUnit
- mocks
- WebApplicationFactory
- integration databases.

**Project/Lab Deliverable**
- Build service and API tests.


## Class #100 — Clean Architecture in .NET

**Status:** ⬜ Planned

**Topics**
- Domain, application, infrastructure, API boundaries.

**Project/Lab Deliverable**
- Refactor a feature into clean architecture.


## Class #101 — Background Services and Messaging

**Status:** ⬜ Planned

**Topics**
- Hosted services
- queues
- retries.

**Project/Lab Deliverable**
- Process an asynchronous job.


## Class #102 — Observability in .NET

**Status:** ⬜ Planned

**Topics**
- Structured logging
- health checks
- metrics.

**Project/Lab Deliverable**
- Add production diagnostics.


## Class #103 — ASP.NET Core Production Deployment

**Status:** ⬜ Planned

**Topics**
- Configuration
- containers
- reverse proxy
- runtime.

**Project/Lab Deliverable**
- Release .NET service v1.


## Class #104 — C# Capstone Service

**Status:** ⬜ Planned

**Topics**
- Enterprise-style feature
- integration
- documentation.

**Project/Lab Deliverable**
- Integrate the .NET service into the platform.


## Class #105 — HTML and CSS Foundations

**Status:** ⬜ Planned

**Topics**
- Semantic HTML
- forms
- layout
- accessibility basics.

**Project/Lab Deliverable**
- Build a static portfolio page.


## Class #106 — Modern JavaScript Foundations

**Status:** ⬜ Planned

**Topics**
- Modules
- arrays
- objects
- promises
- fetch.

**Project/Lab Deliverable**
- Consume an API from the browser.


## Class #107 — TypeScript Foundations

**Status:** ⬜ Planned

**Topics**
- Types
- interfaces
- unions
- generics
- narrowing.

**Project/Lab Deliverable**
- Convert JavaScript exercises to TypeScript.


## Class #108 — React Foundations

**Status:** ⬜ Planned

**Topics**
- Components
- JSX
- props
- rendering.

**Project/Lab Deliverable**
- Create the first React interface.


## Class #109 — React State and Events

**Status:** ⬜ Planned

**Topics**
- useState
- event handling
- derived state.

**Project/Lab Deliverable**
- Build interactive project cards.


## Class #110 — React Effects and Data Fetching

**Status:** ⬜ Planned

**Topics**
- useEffect
- loading
- errors
- cancellation.

**Project/Lab Deliverable**
- Fetch projects from the backend.


## Class #111 — React Forms

**Status:** ⬜ Planned

**Topics**
- Controlled inputs
- validation
- submissions.

**Project/Lab Deliverable**
- Build project create/edit forms.


## Class #112 — React Router

**Status:** ⬜ Planned

**Topics**
- Routes
- layouts
- parameters
- navigation.

**Project/Lab Deliverable**
- Create multi-page portfolio navigation.


## Class #113 — React Authentication

**Status:** ⬜ Planned

**Topics**
- Token handling
- auth context
- login flow.

**Project/Lab Deliverable**
- Add login and logout UI.


## Class #114 — Protected Routes and Authorization UI

**Status:** ⬜ Planned

**Topics**
- Guards
- role-aware rendering
- access denied states.

**Project/Lab Deliverable**
- Protect dashboard pages.


## Class #115 — Tailwind CSS Foundations

**Status:** ⬜ Planned

**Topics**
- Utility classes
- responsive design
- design tokens.

**Project/Lab Deliverable**
- Style the portfolio UI.


## Class #116 — Reusable Component Design

**Status:** ⬜ Planned

**Topics**
- Composition
- variants
- accessibility
- component APIs.

**Project/Lab Deliverable**
- Build a component library.


## Class #117 — React Testing

**Status:** ⬜ Planned

**Topics**
- Vitest/Jest
- Testing Library
- mocking APIs
- accessibility queries.

**Project/Lab Deliverable**
- Test forms and protected pages.


## Class #118 — Frontend State Management

**Status:** ⬜ Planned

**Topics**
- Context
- reducers
- server state
- state boundaries.

**Project/Lab Deliverable**
- Choose and apply a state strategy.


## Class #119 — Frontend Performance

**Status:** ⬜ Planned

**Topics**
- Memoization
- code splitting
- rendering analysis.

**Project/Lab Deliverable**
- Optimize a measurable bottleneck.


## Class #120 — React Frontend Milestone

**Status:** ⬜ Planned

**Topics**
- Integration
- UX review
- error handling
- deployment readiness.

**Project/Lab Deliverable**
- Release React frontend v1.


## Class #121 — Next.js App Router

**Status:** ⬜ Planned

**Topics**
- Routes
- layouts
- nested segments
- conventions.

**Project/Lab Deliverable**
- Create a Next.js application.


## Class #122 — Server and Client Components

**Status:** ⬜ Planned

**Topics**
- Execution boundaries
- serialization
- interactivity.

**Project/Lab Deliverable**
- Split a feature correctly.


## Class #123 — Next.js Data Fetching and Caching

**Status:** ⬜ Planned

**Topics**
- Server fetch
- revalidation
- cache behavior.

**Project/Lab Deliverable**
- Render portfolio data server-side.


## Class #124 — Next.js Forms and Server Actions

**Status:** ⬜ Planned

**Topics**
- Mutations
- validation
- progressive enhancement.

**Project/Lab Deliverable**
- Create a project mutation flow.


## Class #125 — Next.js Authentication

**Status:** ⬜ Planned

**Topics**
- Sessions
- cookies
- middleware
- protected content.

**Project/Lab Deliverable**
- Implement secure authentication.


## Class #126 — Next.js API Integration

**Status:** ⬜ Planned

**Topics**
- Backend-for-frontend patterns
- route handlers
- errors.

**Project/Lab Deliverable**
- Integrate Flask/FastAPI services.


## Class #127 — SEO and Metadata

**Status:** ⬜ Planned

**Topics**
- Metadata API
- structured data
- social previews.

**Project/Lab Deliverable**
- Optimize public portfolio pages.


## Class #128 — Images and Performance

**Status:** ⬜ Planned

**Topics**
- Image optimization
- fonts
- bundles
- Core Web Vitals.

**Project/Lab Deliverable**
- Improve performance scores.


## Class #129 — Next.js Testing

**Status:** ⬜ Planned

**Topics**
- Unit, component, and end-to-end testing.

**Project/Lab Deliverable**
- Test a critical user journey.


## Class #130 — Next.js Deployment

**Status:** ⬜ Planned

**Topics**
- Builds
- environment variables
- runtime choices.

**Project/Lab Deliverable**
- Deploy the web application.


## Class #131 — Portfolio Content and Case Studies

**Status:** ⬜ Planned

**Topics**
- Project storytelling
- architecture diagrams
- outcomes.

**Project/Lab Deliverable**
- Publish project case studies.


## Class #132 — Next.js Frontend Milestone

**Status:** ⬜ Planned

**Topics**
- Accessibility
- performance
- reliability
- release.

**Project/Lab Deliverable**
- Release portfolio web v1.


## Class #133 — React Native Foundations

**Status:** ⬜ Planned

**Topics**
- Native components
- navigation
- platform differences.

**Project/Lab Deliverable**
- Create a mobile project browser.


## Class #134 — React Native API and Authentication

**Status:** ⬜ Planned

**Topics**
- Networking
- secure token storage
- forms.

**Project/Lab Deliverable**
- Add authenticated mobile access.


## Class #135 — React Native State and Offline UX

**Status:** ⬜ Planned

**Topics**
- Caching
- optimistic updates
- connectivity.

**Project/Lab Deliverable**
- Support resilient project viewing.


## Class #136 — React Native Testing and Release

**Status:** ⬜ Planned

**Topics**
- Component tests
- device tests
- build pipeline.

**Project/Lab Deliverable**
- Produce a release candidate.


## Class #137 — Flutter and Dart Foundations

**Status:** ⬜ Planned

**Topics**
- Dart types
- widgets
- layout
- state.

**Project/Lab Deliverable**
- Create a Flutter project browser.


## Class #138 — Flutter Navigation and Forms

**Status:** ⬜ Planned

**Topics**
- Routes
- forms
- validation
- lifecycle.

**Project/Lab Deliverable**
- Build project create/edit screens.


## Class #139 — Flutter API and Authentication

**Status:** ⬜ Planned

**Topics**
- HTTP
- serialization
- secure storage.

**Project/Lab Deliverable**
- Connect to the backend.


## Class #140 — Flutter State Management

**Status:** ⬜ Planned

**Topics**
- Provider/Riverpod/BLoC concepts
- architecture.

**Project/Lab Deliverable**
- Apply a state-management approach.


## Class #141 — Flutter Testing

**Status:** ⬜ Planned

**Topics**
- Unit
- widget
- integration tests.

**Project/Lab Deliverable**
- Test a mobile workflow.


## Class #142 — Mobile Notifications

**Status:** ⬜ Planned

**Topics**
- Push concepts
- permissions
- backend integration.

**Project/Lab Deliverable**
- Prototype notifications.


## Class #143 — Mobile Deployment Fundamentals

**Status:** ⬜ Planned

**Topics**
- Signing
- builds
- store readiness.

**Project/Lab Deliverable**
- Create release documentation.


## Class #144 — Mobile Track Review

**Status:** ⬜ Planned

**Topics**
- React Native versus Flutter trade-offs.

**Project/Lab Deliverable**
- Document technology decisions.


## Class #145 — Linux for Production

**Status:** ⬜ Planned

**Topics**
- Processes
- permissions
- services
- filesystems
- logs.

**Project/Lab Deliverable**
- Operate a small server safely.


## Class #146 — Docker Foundations

**Status:** ⬜ Planned

**Topics**
- Images
- containers
- layers
- Dockerfiles.

**Project/Lab Deliverable**
- Containerize one backend.


## Class #147 — Docker Compose

**Status:** ⬜ Planned

**Topics**
- Multi-service development
- networks
- volumes
- health checks.

**Project/Lab Deliverable**
- Run app, database, and Redis together.


## Class #148 — Container Security and Optimization

**Status:** ⬜ Planned

**Topics**
- Non-root users
- small images
- secrets
- scanning.

**Project/Lab Deliverable**
- Harden Docker images.


## Class #149 — Nginx and Reverse Proxies

**Status:** ⬜ Planned

**Topics**
- Routing
- TLS termination
- static files
- upstreams.

**Project/Lab Deliverable**
- Proxy backend and frontend.


## Class #150 — GitHub Actions CI/CD

**Status:** ⬜ Planned

**Topics**
- Build, test, scan, package, deploy workflows.

**Project/Lab Deliverable**
- Create a deployment pipeline.


## Class #151 — Cloud and VPS Deployment

**Status:** ⬜ Planned

**Topics**
- Servers
- DNS
- firewalls
- environment management.

**Project/Lab Deliverable**
- Deploy the platform.


## Class #152 — HTTPS and Certificate Management

**Status:** ⬜ Planned

**Topics**
- TLS
- certificates
- renewal
- secure headers.

**Project/Lab Deliverable**
- Enable HTTPS.


## Class #153 — Secrets Management

**Status:** ⬜ Planned

**Topics**
- Secret stores
- rotation
- least privilege.

**Project/Lab Deliverable**
- Remove deployment secrets from files.


## Class #154 — Monitoring and Alerting

**Status:** ⬜ Planned

**Topics**
- Metrics
- dashboards
- SLOs
- alerts.

**Project/Lab Deliverable**
- Create service health dashboards.


## Class #155 — Centralized Logging

**Status:** ⬜ Planned

**Topics**
- Log shipping
- search
- retention
- privacy.

**Project/Lab Deliverable**
- Aggregate application logs.


## Class #156 — Distributed Tracing

**Status:** ⬜ Planned

**Topics**
- Trace context
- spans
- cross-service debugging.

**Project/Lab Deliverable**
- Trace a request across services.


## Class #157 — Reliability Engineering

**Status:** ⬜ Planned

**Topics**
- SLIs
- SLOs
- error budgets
- incident response.

**Project/Lab Deliverable**
- Define reliability objectives.


## Class #158 — DevOps Milestone

**Status:** ⬜ Planned

**Topics**
- Production review
- recovery
- security
- automation.

**Project/Lab Deliverable**
- Release production platform v1.


## Class #159 — Machine Learning Foundations for Engineers

**Status:** ⬜ Planned

**Topics**
- Training versus inference
- features
- evaluation
- overfitting.

**Project/Lab Deliverable**
- Build a small ML experiment.


## Class #160 — Hugging Face Fundamentals

**Status:** ⬜ Planned

**Topics**
- Models
- tokenizers
- pipelines
- model hub.

**Project/Lab Deliverable**
- Run a pretrained model.


## Class #161 — Model Inference APIs

**Status:** ⬜ Planned

**Topics**
- Wrappers
- batching
- latency
- error handling.

**Project/Lab Deliverable**
- Expose a model through FastAPI.


## Class #162 — AI Service Testing

**Status:** ⬜ Planned

**Topics**
- Deterministic tests
- fixtures
- model mocking
- quality checks.

**Project/Lab Deliverable**
- Test an AI wrapper.


## Class #163 — Embeddings

**Status:** ⬜ Planned

**Topics**
- Vector representations
- similarity
- chunking implications.

**Project/Lab Deliverable**
- Generate and compare embeddings.


## Class #164 — Vector Databases

**Status:** ⬜ Planned

**Topics**
- Indexes
- metadata filters
- retrieval
- persistence.

**Project/Lab Deliverable**
- Store and query vectors.


## Class #165 — RAG Foundations

**Status:** ⬜ Planned

**Topics**
- Ingestion
- chunking
- retrieval
- generation
- citations.

**Project/Lab Deliverable**
- Build a simple RAG pipeline.


## Class #166 — RAG Evaluation

**Status:** ⬜ Planned

**Topics**
- Retrieval quality
- groundedness
- relevance
- test datasets.

**Project/Lab Deliverable**
- Create an evaluation harness.


## Class #167 — Prompt and Context Engineering

**Status:** ⬜ Planned

**Topics**
- Instructions
- context windows
- structured outputs.

**Project/Lab Deliverable**
- Improve a production prompt flow.


## Class #168 — AI Security and Privacy

**Status:** ⬜ Planned

**Topics**
- Prompt injection
- data leakage
- access controls
- redaction.

**Project/Lab Deliverable**
- Threat-model the AI feature.


## Class #169 — AI Observability

**Status:** ⬜ Planned

**Topics**
- Latency
- token usage
- quality
- drift
- traces.

**Project/Lab Deliverable**
- Create AI monitoring metrics.


## Class #170 — Model Optimization

**Status:** ⬜ Planned

**Topics**
- Quantization
- batching
- caching
- hardware trade-offs.

**Project/Lab Deliverable**
- Improve inference efficiency.


## Class #171 — Medical AI Engineering Considerations

**Status:** ⬜ Planned

**Topics**
- Safety boundaries
- validation
- auditability
- privacy.

**Project/Lab Deliverable**
- Design a safe medical-use wrapper.


## Class #172 — Production RAG Architecture

**Status:** ⬜ Planned

**Topics**
- Queues
- storage
- re-indexing
- multitenancy.

**Project/Lab Deliverable**
- Design a scalable RAG system.


## Class #173 — AI-Powered Platform Feature

**Status:** ⬜ Planned

**Topics**
- Backend-first AI product integration.

**Project/Lab Deliverable**
- Add an AI feature to the portfolio platform.


## Class #174 — AI Engineering Milestone

**Status:** ⬜ Planned

**Topics**
- Testing
- security
- documentation
- deployment.

**Project/Lab Deliverable**
- Release AI feature v1.


## Class #175 — System Design Fundamentals

**Status:** ⬜ Planned

**Topics**
- Requirements
- constraints
- capacity
- high-level architecture.

**Project/Lab Deliverable**
- Design a URL shortener.


## Class #176 — Scalability and Load Balancing

**Status:** ⬜ Planned

**Topics**
- Horizontal scaling
- statelessness
- routing.

**Project/Lab Deliverable**
- Scale an API design.


## Class #177 — Caching Systems

**Status:** ⬜ Planned

**Topics**
- Cache policies
- consistency
- stampedes
- invalidation.

**Project/Lab Deliverable**
- Design a caching strategy.


## Class #178 — Queues and Event-Driven Architecture

**Status:** ⬜ Planned

**Topics**
- Brokers
- delivery semantics
- consumers
- retries.

**Project/Lab Deliverable**
- Design a notification pipeline.


## Class #179 — Data Partitioning and Replication

**Status:** ⬜ Planned

**Topics**
- Sharding
- replicas
- consistency
- failover.

**Project/Lab Deliverable**
- Design data scaling.


## Class #180 — Microservices and Service Boundaries

**Status:** ⬜ Planned

**Topics**
- Bounded contexts
- contracts
- operational costs.

**Project/Lab Deliverable**
- Decompose a monolith deliberately.


## Class #181 — Distributed Systems Trade-offs

**Status:** ⬜ Planned

**Topics**
- CAP
- consensus basics
- clocks
- partial failure.

**Project/Lab Deliverable**
- Analyze a distributed failure.


## Class #182 — Security Architecture

**Status:** ⬜ Planned

**Topics**
- Threat modeling
- trust boundaries
- least privilege.

**Project/Lab Deliverable**
- Threat-model the platform.


## Class #183 — Observability Architecture

**Status:** ⬜ Planned

**Topics**
- Logs
- metrics
- traces
- incident diagnosis.

**Project/Lab Deliverable**
- Design an observability stack.


## Class #184 — System Design Interview Framework

**Status:** ⬜ Planned

**Topics**
- Clarification
- APIs
- data
- scaling
- failures
- trade-offs.

**Project/Lab Deliverable**
- Complete a timed design interview.


## Class #185 — Data Structures and Algorithms I

**Status:** ⬜ Planned

**Topics**
- Complexity
- arrays
- strings
- hash maps.

**Project/Lab Deliverable**
- Solve and explain core problems.


## Class #186 — Data Structures and Algorithms II

**Status:** ⬜ Planned

**Topics**
- Stacks
- queues
- trees
- graphs.

**Project/Lab Deliverable**
- Solve intermediate problems.


## Class #187 — Backend Interview Preparation

**Status:** ⬜ Planned

**Topics**
- HTTP
- databases
- auth
- testing
- debugging.

**Project/Lab Deliverable**
- Complete a mock backend interview.


## Class #188 — Behavioral Interviews and STAR

**Status:** ⬜ Planned

**Topics**
- Ownership
- conflict
- failure
- impact.

**Project/Lab Deliverable**
- Write reusable STAR stories.


## Class #189 — CV, LinkedIn, and GitHub

**Status:** ⬜ Planned

**Topics**
- Positioning
- achievements
- project evidence
- discoverability.

**Project/Lab Deliverable**
- Publish job-ready profiles.


## Class #190 — Open Source Contribution

**Status:** ⬜ Planned

**Topics**
- Issue selection
- communication
- pull requests
- review.

**Project/Lab Deliverable**
- Contribute to an external project.


## Class #191 — Capstone Architecture and Planning

**Status:** ⬜ Planned

**Topics**
- Requirements
- milestones
- risks
- architecture decisions.

**Project/Lab Deliverable**
- Approve the final capstone plan.


## Class #192 — Capstone Implementation Sprint I

**Status:** ⬜ Planned

**Topics**
- Core backend and database.

**Project/Lab Deliverable**
- Deliver the first integrated milestone.


## Class #193 — Capstone Implementation Sprint II

**Status:** ⬜ Planned

**Topics**
- Frontend, auth, and product workflows.

**Project/Lab Deliverable**
- Deliver the second milestone.


## Class #194 — Capstone Implementation Sprint III

**Status:** ⬜ Planned

**Topics**
- AI/service integration and mobile or secondary client.

**Project/Lab Deliverable**
- Deliver the third milestone.


## Class #195 — Capstone Quality and Security Review

**Status:** ⬜ Planned

**Topics**
- Tests
- performance
- security
- accessibility.

**Project/Lab Deliverable**
- Close release blockers.


## Class #196 — Capstone Deployment and Observability

**Status:** ⬜ Planned

**Topics**
- CI/CD
- production rollout
- dashboards
- runbooks.

**Project/Lab Deliverable**
- Deploy the final system.


## Class #197 — Technical Documentation and Case Study

**Status:** ⬜ Planned

**Topics**
- README
- diagrams
- ADRs
- API docs
- lessons learned.

**Project/Lab Deliverable**
- Publish a complete case study.


## Class #198 — Mock Interview Loop

**Status:** ⬜ Planned

**Topics**
- Coding
- backend
- system design
- behavioral.

**Project/Lab Deliverable**
- Complete a full interview simulation.


## Class #199 — Job Application System

**Status:** ⬜ Planned

**Topics**
- Target roles
- tracking
- networking
- iteration.

**Project/Lab Deliverable**
- Launch a structured application campaign.


## Class #200 — Engineering Journey Graduation Review

**Status:** ⬜ Planned

**Topics**
- Skills audit
- portfolio review
- growth plan.

**Project/Lab Deliverable**
- Publish the final academy retrospective.

