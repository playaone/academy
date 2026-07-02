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