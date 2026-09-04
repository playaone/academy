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