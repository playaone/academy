What happens between writing code and seeing output?
    The language processor takes the code and converts it to something the machine can understand.

Difference between compiled and interpreted languages?
    A compiled language compiles human readable code to executable files.

Why might a backend engineer choose Go instead of Python?
    A backend engineer may choose Go instead of Python when execution speed matters more.

Explain variables using memory.
    A variable is a representation of a memory address that holds a particular value.

---

## Academy Review

Score:

- Technical correctness: 23/40
- Understanding: 18/30
- Completeness: 11/20
- Engineering practices: 7/10
- Overall: 59/100

What is correct:

- You correctly identify that code must be converted into something the machine can execute.
- You correctly identify execution speed as one reason to choose Go.
- Your memory explanation is directionally useful.

Corrections:

- "Language processor" is vague. Depending on the language, code may be compiled, interpreted, or run by a virtual machine.
- A compiled language usually translates source code into machine code or bytecode before execution. It is not only "human readable code to executable files"; there can be build steps, linking, and platform-specific output.
- Interpreted languages execute source code through an interpreter or runtime, often line by line or via bytecode.
- Go is chosen not only for speed, but also for concurrency, static binaries, strong typing, simple deployment, and predictable performance.
- A variable is a named reference to a value; the exact memory behavior depends on the language and runtime.

Improved answer:

```text
Between writing code and seeing output, the language runtime or compiler reads the source code, checks it, translates it into instructions the computer can execute, runs those instructions, and produces output.

Compiled languages translate code before execution, often into machine code or bytecode. Interpreted languages run through an interpreter or runtime while the program executes.

A backend engineer may choose Go for speed, concurrency, static binaries, strong typing, and easy deployment.

A variable is a name that lets a program refer to a value. That value is stored somewhere in memory, but the language controls the exact memory details.
```

Additional practice:

- Compare how `hello.py` and `hello.go` run on your machine.
- Explain stack vs heap at a beginner level.
