# ICS 4211: Compiler Construction (Week Long Tasks)
## Contributions
- 135860 Sitati Lewis
- 135865 Omwenga Farajah
- 112473 Ogutu Tracy
- 112272 Sumlon Bahati
- 110328 Alfred Mwaniki
- 137255 Nicole Were
- 120047 Wanje Kelvin

## Logic Behind the Comments Counter
### Input
The program takes in input code either as a file or as a user input

### Lexical Analysis
The program then performs lexical analysis, breaking down the source code into tokens which are the smalles units in the source code, such as keywords, operators and identifiers.

### Parsing
The program then parses the tokens to understand the structure of the source code. While parsing, the program will look for specific comment patterns in this case, there are two types of comments: in-line comments and multi-line comments

### Identifying Single-line Comments
For single-line comments, the program searches for the specific symbol(s) used to denote comments in the given programming language. For example, in many programming languages, "//" is used for single-line comments in C-style languages, whereas "#" is used in Python.

### Identifying Multi-line Comments
Multi-line comments typically start with a specific symbol and end with another symbol. For instance, in C-style languages, multi-line comments start with "/" and end with "/". The program keeps track of whether it is inside a multi-line comment and ignores everything until it finds the closing symbol.

### Counting Comments
For every time the program identifies a comment (single-line or multi-line), it increments a comment counter. The counter keeps track of the number of comments found in the source code.

### Output
After scanning the entire source code, the program outputs the total number of comments it found.

## Importance of Lexical Analysis in Building the Comment Counter program
Lexical Analysis was vital in building the program that counts comments in input source code as it provides the foundational structure of the input source code. It allows the program to understand the input source code's syntax, identify and differentiate comments from other source code elements.