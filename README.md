# 206Neutrinos 👁

Welcome to **206neutrinos**.

This project involves calculating updated statistical measures for a series of neutrino observations.

## Language and Tools 🛠️

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

- **Language:** Python
- **Compilation:** Via Makefile, including `re`, `clean`, and `fclean` rules.
- **Binary Name:** 206neutrinos

## Project Overview 🔎

The goal of 206neutrinos is to create a program that updates statistical measures, such as arithmetic mean, harmonic mean, and standard deviation, as new neutrino observation values are entered.

### Key Features

- **Dynamic Calculation:** Update statistical measures upon the entry of each new observation value.
- **Interactive Interface:** Allow users to enter new values interactively.
- **Statistical Measures:** Calculate the arithmetic mean, harmonic mean, root mean square, and standard deviation.

### Usage

```
∼> ./206neutrinos -h
USAGE
    ./206neutrinos n a h sd
DESCRIPTION
    n   number of values
    a   arithmetic mean
    h   harmonic mean
    sd  standard deviation
```

### Exemple

```
∼> ./206neutrinos 12000 297514 297912 4363
Enter next value: 299042
    Number of values:   12001
    Standard deviation: 4362.84
    Arithmetic mean:    297514.13
    Root mean square:   297546.11
    Harmonic mean:      297912.09

Enter next value: 302420
    Number of values:   12002
    Standard deviation: 4362.89
    Arithmetic mean:    297514.54
    Root mean square:   297546.52
    Harmonic mean:      297912.46

Enter next value: END
```

Clone the repository.
Compile the project using the provided Makefile.
Run the program with the initial statistics.
Interactively enter new observation values to update and display statistics.
Exit the program by entering END.
For detailed usage instructions, refer to 206neutrinos.pdf.

## Installation and Usage 💾

1. Clone the repository.
2. Compile the project using the provided Makefile.
3. Run the program: `./206neutrinos n a h sd`.
4. Exit the program by entering `END`.
5. For detailed usage instructions, refer to `206neutrinos.pdf`.

## License ⚖️

This project is released under the MIT License. See `LICENSE` for more details.
