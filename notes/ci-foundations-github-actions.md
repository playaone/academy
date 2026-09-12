Explain in your own words:

    What is Continuous Integration?
        Continuous Integration (CI) is a software development practice where developers frequently merge their code changes into a central repository, usually multiple times a day, triggering automated builds and tests to detect errors early.

    What's the difference between CI and deployment?
        Continuous Integration (CI) focuses on testing and merging code changes into a shared repository, while Continuous Deployment (CD) automatically pushes those tested changes directly to production for real users.

    What is a GitHub Actions workflow?
        A GitHub Actions workflow is a configurable automated process defined in a YAML file that runs one or more jobs when triggered by specific events in your repository.

    What is an event?
        An event is a specific activity or trigger within a GitHub repository that automatically launches a workflow to run your automated tasks.

    What is a job?
        A job is a collection of steps inside a GitHub Actions workflow that execute sequentially on the same virtual machine or runner.

    What is a step?
        A step is an individual task inside a GitHub Actions job that runs commands or actions sequentially on your workflow's virtual machine.

    What is a runner?
        A runner is a server or virtual machine that actually executes the jobs and steps inside your GitHub Actions workflow when an event triggers it.

    Why does CI start from a fresh environment?
        Continuous Integration (CI) starts from a fresh, clean environment to guarantee reproducibility, reliability, and security by preventing leftover files or hidden settings from interfering with the build.

    What does working-directory do?
        In GitHub Actions, working-directory changes the default directory or folder where your terminal commands run inside a specific step or job.

    How does pytest tell GitHub Actions that tests failed?
        pytest tells GitHub Actions that tests failed by returning a non-zero exit code (specifically exit code 1), which GitHub Actions treats as a command failure and automatically marks the step as failed.

    Why must CI not use instance/project.sql?
        Continuous Integration must not use a pre-existing local instance/project.sql (or local database file) because it violates the rule of a fresh, reproducible environment, is usually untracked in version control, and introduces flaky, unreliable test results.

    Why shouldn't a coverage threshold be chosen arbitrarily?
        A code coverage threshold should never be chosen at random (like blindly picking 80% or 90%) because it encourages superficial testing, creates a false sense of security, and can block valid deployments if it does not match the actual risk profile of your codebase.

    What kinds of bugs can CI reveal that local development may hide?
        Continuous Integration (CI) catches critical bugs that stay hidden during local development because local machines suffer from a phenomenon known as "it works on my machine." Local environments naturally accumulate unique configurations, manual fixes, and leftover files that hide systemic coding issues.

## Instructor Review - Class #019 CI Foundations

Reviewed: 2026-09-04

Score:

- Technical correctness: 34/40
- Understanding: 26/30
- Completeness: 18/20
- Engineering practices: 9/10
- Overall: 87/100

What is strong:

- You correctly identify CI as an automated safety check around frequent code integration.
- You understand GitHub Actions vocabulary: workflow, event, job, step, and runner.
- You correctly explain that CI should use a fresh environment instead of local state.
- You correctly explain why CI must not depend on `instance/project.sql`.
- You connect pytest failure to process exit codes, which is an important engineering detail.

Corrections:

- CI does not literally merge code by itself. CI runs automated checks when code is pushed, a pull request is opened or updated, or another configured event fires. Merging is a developer or repository-policy decision that may depend on CI passing.
- "CI vs deployment" is mostly correct, but be precise: deployment means releasing or installing software into an environment. Continuous Deployment is only one automated deployment style.
- "pytest returns exit code 1" is a useful example, but the safer rule is: pytest returns a non-zero exit code when the test run fails, and GitHub Actions treats any non-zero command exit code as a failed step.
- "It works on my machine" is a good phrase, but the deeper reason is environment drift: different Python versions, missing dependencies, uncommitted files, hidden local databases, cached state, and operating system differences.

Improved answer:

```text
Continuous Integration is the practice of automatically running checks, such as installation, tests, linting, and coverage, whenever code changes are pushed or proposed. CI gives the team fast feedback before code is trusted or merged.

CI is not the same as deployment. CI proves that the codebase can be built and tested in a clean environment. Deployment releases the application to an environment such as staging or production.

GitHub Actions runs workflows from YAML files. A workflow starts from an event, contains one or more jobs, and each job runs ordered steps on a runner.

pytest communicates failure through its process exit code. If pytest returns any non-zero exit code, GitHub Actions marks that step and job as failed.

CI must not use `instance/project.sql` because that is local development state. CI should create its own clean test database so the result is reproducible.
```

Practice tasks:

- Add one sentence explaining why `pull_request` CI is especially useful before merging.
    Pull request CI is especially useful before merging because it automatically runs tests, linting, and builds against the proposed changes in isolation, catching bugs and failures early so broken code never reaches the main branch.

- Explain what would happen if `pip install -r requirements.txt` fails in CI.
    If `pip install -r requirements.txt` fails in CI, the step exits with a non-zero status code, the CI job (and usually the entire workflow) is marked as **failed**, subsequent steps are typically skipped, the pull request shows a failed check, and merging is blocked if branch protection requires passing CI.

- Explain why a CI workflow should run from committed files only, not files that happen to exist locally.
    A CI workflow should run only from committed files because that is the only way to guarantee the checks are reproducible, consistent, and trustworthy: CI must test exactly what is in the repository (and will be merged or deployed), not any uncommitted, untracked, or locally modified files that exist only on a developer’s machine.