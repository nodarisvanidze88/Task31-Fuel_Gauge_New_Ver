# Fuel Gauge New Version
## Questions:
    1. If empty what is the minimal percentage
    2. If Full what is the maximal percentage
    3. what to do if the user will add a string
    4. what to do if the user will add float numbers
    5. what to do if the user will add math operations except for division
    6. what to do if the user will add multiple divisions

## The Task
Write the program which prompts from user numbers with a division like "x/y" where x and y are integers and return "E" if the result is
equal or less than 1, it also returns "F" if the result is equal or greater than 99. otherwise, return the division result percentage

### Inputs, Processes, Outputs
Noun
- User Input of division
- Result
Verbs
- Check user information as operation
- Display Result

Inputs
- User Input
Processes
- check and validate user input
- calculate user input and round with 0 digit after decimal
Output
- Display result as Percentage or "E" or "F"


### tests
#### Test convert function
1. case
    input: 4/5 && Expected Result: 80%
2. case
    input: 5/4 &&  Expected Result: ValueError("Result percentage must be between 0 and 100")
3. case
    input: Cat/Dog &&  Expected Result: ValueError("Division should be between integers")
4. case
    input: 10/0 && Expected Result: ZeroDivisionError("Division by 0 is impossible")
5. case
    input: 10.5/20.5 && Expected Result: ValueError("Division should be between integers")
6. case
    input: 12345 && Expected Result: ValueError("Need use division "\"")
7. case
    input: 5+5 && Expected Result: ValueError("Need use division "\"")
8. case
    input: -10/-5 && Result: 200
9. case
    input: 1/100 Expected Result: 1
10. Case
    input: 4/4 Expected Result: 100

#### Test gauge function
1. case
    input: 1 && result: "E"
2. case
    input: 0 && result: "E"
3. case
    input: -1 && result: "E"
4. case
    input: 75 && result: "75%"
5. case
    input: 99 && result: "F"
6. case
    input: 100 && result: "F"

### Pesudocode
main function
    initialize user input
    call with print converter and gauge function and input user prompt
converter function(user prompt)
    spllit prompt as list
    check if there is "/"
        if not rise error
    check number of "/"
        if it is more then 1 rise ValueError
    initialize z and y numbers
        from prompt x = left side from "/"
        from prompt y = right side from "/"
    check both of them are integers
        if not rise ValueError
    check if y is 0
        if yes rise ZeroDivisionError
    check x grater then Y
        if yes rise ValueError
    if everithing is OK calculate prompt*100
gauge function(percentage)
    if percentage <= 1 return "E"
    if percentage >=99 retunr "F"
    else return formated sting with % without numbers after decimal


