What is formatting?
    Formatting is the method of writing code so it is more readable and understandable.

What is linting?
    Linting is the specified rules guiding the formation of your code to catch errors and potential bugs that otherwise may go unnoticed even after testing.

What is import sorting?
    This is process of keeping imports and dependencies organised.

What is static type checking?
    This is the process of assigning and verifying that variable maintain their types and operate accordingingly.

What's the difference between ruff format and ruff check?
    Ruff format check for formatting issues, while ruff check checks for linting issues.

Why should you inspect git diff after an automated fix?
    This is because automated fixes can break code logics or cause unexpected errors.

Why don't type hints replace Marshmallow?
    Because type hints cannot operate as input validatiors. Users can still enter wrong inputs.

Why don't linters replace tests?
    Linters can catch static bugs or potential operational errors, but tests ensure run time errors are handled.

Why don't tests replace linters?
    Tests cannot find errors they are not specifically written for.

What does Project | None communicate?
    This means a Project object or None value is expected.

Why shouldn't we immediately force strict typing over an existing Flask application?
    Forcing strict typing on an already existing application can cause unexpected bugs.

Why should CI eventually run the same checks developers run locally?
    This is because developer may have local configurations and files which helps the checks pass, but those files and configurations may not be present in the deployment enviroment.