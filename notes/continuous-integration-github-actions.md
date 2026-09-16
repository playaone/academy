What Continuous Integration means.
    Continuous Integration (CI) is a software development practice in which developers frequently merge their code changes into a shared main branch (often multiple times a day).

Why CI is useful even for a solo developer.
    CI gives a solo developer automatic, reliable feedback on every change so mistakes are caught immediately instead of later.

What a GitHub Actions workflow is.
    A GitHub Actions workflow is a configurable automated process defined in a YAML file (usually stored in .github/workflows/) that runs in response to events in a GitHub repository — such as a push, pull request, or schedule — and executes a series of jobs and steps to build, test, or deploy your code.

What a job is.
    A job is a set of steps that run on the same runner (virtual machine) and form a single unit of work — such as building the code or running tests.

What a step is.
    A step is a single task — such as checking out code, running a command, or using a pre-built action — that executes sequentially within that job.

What a runner is.
    A runner is the virtual machine or server that executes the jobs and steps defined in a workflow.

Why actions/checkout is necessary.
    `actions/checkout` is necessary because GitHub Actions runners start with an empty workspace — without it, your repository’s code is not present, so later steps cannot build, test, or work with your files.

Why working-directory is necessary for this project.
    Every step runs from the root of the checked-out repository. Setting working-directory tells the runner to change into the correct subdirectory first so that commands like npm install, npm test, or dotnet build find the right files and configuration.

Why CI should start from a clean environment.
    CI should start from a clean environment so that every build and test run is fully reproducible and independent of leftover files, cached dependencies, or previous state — ensuring the result reflects only what’s in the repository and the explicit pipeline steps.

Why CI should not use instance/project.sql.
    CI should not use `instance/project.sql` because that file is typically local or environment-specific (containing machine-dependent paths, connection details, or instance-only configuration). Using it would make the pipeline non-reproducible and likely to fail on clean runners that do not have the same local state.

How pytest communicates failure to GitHub Actions.
    pytest communicates failure to GitHub Actions by exiting with a non-zero exit code when any tests fail or errors occur. GitHub Actions automatically marks the step (and usually the job) as failed whenever a command returns a non-zero exit code.

Difference between CI and branch protection.
    CI runs the checks; branch protection makes those checks mandatory before merging.

Difference between line/terminal coverage and a coverage artifact.
    Line/terminal coverage is the human-readable summary (percentages and line-by-line results) that the coverage tool prints directly in the CI logs or terminal during the run.
    A coverage artifact is a saved file (HTML report, XML, or .coverage data) that the CI pipeline uploads and stores so you can download and inspect the detailed report later.

Why dependencies must be declared in the repository rather than installed manually on your machine.
    Dependencies must be declared in the repository so that any machine — including a clean CI runner — can automatically install the exact same packages.  

    Installing them only on your local machine makes the project non-reproducible.