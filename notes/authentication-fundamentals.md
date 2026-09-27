Authentication
    Authentication is the process of identifying and verifying users.

Authorization
    This is the ability of identified users to perform actions or access resources.

Password hashing
    Password hashing is the process of transforming a password into a one-way hash using a password-hashing algorithm.

Password verification
    Password verification is the process of determining whether a user's supplied password matches the previously hashed password stored in the database.

Why SHA-256 isn't a password-storage solution
    SHA-256 is a fast general-purpose hashing algorithm. Its speed makes it unsuitable for securely storing passwords because attackers can perform large numbers of guesses quickly.

Why Argon2 is appropriate
    Argon2 is a password-hashing algorithm designed to make password guessing more expensive by requiring significant computational and memory resources.

Why plaintext passwords must never be stored
    Plaintext passwords must never be stored because a database breach could expose users' actual passwords.

Where password hashing belongs in our architecture
    Password hashing belongs in the security branch/package of the application.