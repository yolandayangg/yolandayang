
[link to code with video](https://user-images.githubusercontent.com/89219568/158474608-3d25b612-e40b-4b03-974f-f01a0e1748c0.mp4)

Create task idea runtime

Written Responses:

1. a.Overall purpose of the program: Our program aims to test the math skills of the user by building on their multiplication and division skills. Many students struggle with basic arithmetic and this interactive game is a great platform for them to brush up on their skills before an assessment.

b. Functionality of the program: The program includes 5 questions that the user then answers. 

c. Description of input and output of program: The inputs are given for the user to select what problem type between multiplication or division. After they select , there are multiple inputs where they provide the best answer for the question that is written on the screen. The outputs include the math problem that is displayed, results from the user’s response, and the final score based on the number correct or incorrect answers. 

2. Code Segments

a. Code Example of Data stored in list:

b. Code segment of data in list being used (creating data, accessing multiple elements in list)

c. Name of list used: first_number which stores the first number in the problem and second_number which stores the second number in the program. Both the store values used in the math problems. 

d. Benefits of using list in this program: the lists are useful because they can store all the values in one variable without needing individual variables. The loop also allows for the program to expand without having to repetitively write the same program sequence multiple times. The lists can also be easily inserted or removed without complete reorganization of the structure, unlike an array. 

3. Code segments

a. Procedure that defines procedure’s name and return type 1+ parameters with effect on functionality, algorithm with sequencing, selection, iteration

b. Where procedure called in program

c. Describe what procedure does and contribution: the function executed quiz questions and similarly returns the number of correct answers based on the user’s input. 

d. How algorithm works: the function loops through all the values present in the list which creates a problem for the user to solve. The first_number list allows for the first number of the problem to be printed. Then, based on the user’s input of choosing multiplication or division, the multiplication or division operator is printed. After the second_number list prints the next number that the user can use to solve the math problem. If the answer is correct (based on a selection statement) the tracker variable keeps track of the number of correct answers. Once all responses are completed, the function terminates and the number of correct answers is displayed. 

4. Written response

a. 2 calls to procedure that cause segments of code to execute

b. Describe conditions tested by each call

c. Result of calls
The two calls are M and D; the first being M and the second being D, because D is the else statement. M executes the if statement of the loop, and selects 5 multiplication problems to print out. The selection statement inside the loop will print a problem with the multiply (*) operator. The answer will be calculated by multiplying a value from the first_number list and a value from the second_number list. At the end of the five problems, the program will print the number of answers the user got correct as well as the percentage it corresponds to.

The second call passes the letter D. It essentially works the same as M, but the selection statement will execute the else clause because D is not M. The code will print a divide (/) operator and calculate the answer by dividing a value from the first_number list and a value from the second_number list. At the end of the five problems, the program will print the number of answers the user got correct as well as the percentage it corresponds to.


