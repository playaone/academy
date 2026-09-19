Authentication
    This is the process of Identifying users.

Authorization
    This is the ability of identified users to perform actions or access resources.

Password hashing
    This is the encryption of user passwords.

Password verification
    This is the process of assertaining that a user's password matches the previously hashed password stored in the database.

Why SHA-256 isn't a password-storage solution
    SHA-256 is a quick hashing algorithm that is highly guessable.

Why Argon2 is appropriate
    Argon2 is a more complex algorithm that is not guessable.

Why plaintext passwords must never be stored
    Plaintext passwords must be never stored because any leak can expose users passwords.

Where password hashing belongs in our architecture
    Password hashing belongs to the security branch.