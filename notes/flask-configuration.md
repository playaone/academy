Answer the following questions:

Why is storing secrets in source code a bad idea?
    Storing secrets in source code exposes the secret when it is uploaded to github.
    Also will require developers to edit source code when deploying/making changes
    Makes it harder to control the enviroment.

What is the purpose of a .env file?
    The .env file holds key value pairs that the python app can read through the operating system.

Why should .env be listed in .gitignore?
    So it doesn't end up in git and expose app sensitive secrets.

What is the responsibility of the Config class?
    This class is used to initialize the app configurations

What is the difference between:
os.getenv("KEY")
os.getenv("KEY", "default")
    os.getenv("KEY") has no default/fallback value and will raise execptions if "KEY" was not found
    os.getenv("KEY", "DEFAULT") has a fallback value to use in case "KEY" was not found

---

## Academy Review

Score:

- Technical correctness: 29/40
- Understanding: 23/30
- Completeness: 16/20
- Engineering practices: 8/10
- Overall: 76/100

What is correct:

- You understand that secrets should not be committed to Git.
- You understand that `.env` stores environment-style key/value configuration.
- You correctly say `.env` belongs in `.gitignore`.

Corrections:

- `os.getenv("KEY")` does not raise an exception when the key is missing. It returns `None`.
- A `.env` file is commonly loaded by `python-dotenv`, which places values into environment variables that your app can read.
- The `Config` class is not only for "initializing" config; it centralizes named configuration values used by the app and extensions.

Improved answer:

```text
Secrets should not be stored in source code because source code is shared, committed, reviewed, and often pushed to remote repositories. A leaked secret can expose databases, APIs, and user data.

A `.env` file stores local environment variables for development. `python-dotenv` can load those values so the app can read them with `os.getenv`.

`.env` should be in `.gitignore` because it may contain private secrets.

The `Config` class centralizes app settings such as `SECRET_KEY`, database URI, debug mode, and SQLAlchemy options.

`os.getenv("KEY")` returns the environment value or `None` if missing. `os.getenv("KEY", "default")` returns the value or the provided fallback.
```

Additional practice:

- Write down which config values are safe to commit and which must stay private.
- Explain the difference between `.env`, `.env.example`, and `Config`.
