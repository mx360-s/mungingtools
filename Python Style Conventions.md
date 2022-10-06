# Python Style Conventions #

## Big 3 ##

 - Name things well
 - Be consistent.
 - Format continually, and re-format whenever necessary.

## Style ##

### Names ###

Names must be meaningful within their given context, except:

 - use of single-letter loop control variables such as i
 - ¿?

Variables and value-returning functions are generally noun-like, as in:

 - Length
 - Number_Of_Students
 - Average_Score()

Boolean variables and functions, however, are usually adjective-like, as in:

 - Valid
 - IsFinished()

Task functions (void) performs a task, doesn't return a value, are verbs-like, as in:

 - GetInputFromUser()
 - DisplayOutput()
 - Time.IncrementHours()

### Capitalization ###

Functions and Variables use 'PascalCase', multi-word names aren't separated:

 - GetInputFromUser()
 - DisplayOutput()
 - Cost = [];
 - Number_Of_Guesses = {};

Constants, tuples & Syntactic Macros use all uppercase letters (SCREAMING SNAKE CASE), multi-word names are separated by underscores:

 - SIZE = 100;
 - double TAX_RATE = 0.15;

### whitespacing ###

 - Use vertical spacing to enhance readability. For example, use one or more blank lines to separate logically distinct parts of a program.

 - Use horizontal spacing to enhance readability. For example, it is usually a good idea to place a blank space on each side of an operator such as << or +

## File Structure ##

### Comments ###

At the beginning of a file, always:

 - comment containing the name of the file
 - and a comment containing the purpose of the code in that file.

These two comments can often be one line each

For each function, include the following information, in this order:

 - One or more comment statements describing in summary form what the function does.
 - The return value of the function
 - A list of the function's parameters in the same order as they appear in the parameter list
 - The function's pre-conditions and post-conditions

### Program Structure ###

When your entire program is contained in a single source code file:

 - The necessary "import" for the required process
 - Definitions for any constant, and declarations
 - Definitions for each of the functions

### Miscellaneous ###

 - Maximum Length of Source Code Lines: whatever value you choose must be stricly less than 80.
 - Only TAB Characters in Source Code
 - Each script should at a minimum describe briefly what it does when it runs
 - Always delete unused variables: *del VarName*
## Sources ##

 - https://cs.smu.ca/~porter/csc/ref/cpp_style.html
 - https://www.geeksforgeeks.org/return-from-void-functions-in-cpp/
 - https://en.wikipedia.org/wiki/Naming_convention_(programming)
 - https://dart.dev/guides/language/effective-dart/style
 - https://www.geeksforgeeks.org/naming-conventions-in-lisp/
