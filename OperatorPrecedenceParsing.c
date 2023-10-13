#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define operator precedence and associativity
#define MAX_STACK_SIZE 100
#define MAX_EXPRESSION_SIZE 100

int precedence(char operator) {
    switch (operator) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        default:
            return 0;
    }
}

// Function to apply an operator
void applyOperator(char operator, int* operandStack, int* top) {
    int rightOperand = operandStack[(*top)--];
    int leftOperand = operandStack[(*top)--];

    switch (operator) {
        case '+':
            operandStack[++(*top)] = leftOperand + rightOperand;
            break;
        case '-':
            operandStack[++(*top)] = leftOperand - rightOperand;
            break;
        case '*':
            operandStack[++(*top)] = leftOperand * rightOperand;
            break;
        case '/':
            operandStack[++(*top)] = leftOperand / rightOperand;
            break;
    }
}

// Operator precedence parsing function
int operatorPrecedenceParse(char* expression) {
    int operatorStack[MAX_STACK_SIZE];
    int operandStack[MAX_STACK_SIZE];
    int operatorTop = -1;
    int operandTop = -1;
    
    int i;
    for (i = 0; i < strlen(expression); i++) {
        char token = expression[i];
        
        if (token == ' ')
            continue; // Skip whitespace

        if (token >= '0' && token <= '9') {
            // Read and push the number
            int num = 0;
            while (i < strlen(expression) && expression[i] >= '0' && expression[i] <= '9') {
                num = num * 10 + (expression[i] - '0');
                i++;
            }
            operandStack[++operandTop] = num;
            i--; // Adjust index to the last digit of the number
        } else if (token == '(') {
            // Push open parenthesis
            operatorStack[++operatorTop] = token;
        } else if (token == ')') {
            // Evaluate operators inside parentheses
            while (operatorTop >= 0 && operatorStack[operatorTop] != '(') {
                applyOperator(operatorStack[operatorTop], operandStack, &operandTop);
                operatorTop--;
            }
            operatorTop--; // Remove the open parenthesis
        } else if (token == '+' || token == '-' || token == '*' || token == '/') {
            // Handle operators
            while (operatorTop >= 0 && precedence(token) <= precedence(operatorStack[operatorTop])) {
                applyOperator(operatorStack[operatorTop], operandStack, &operandTop);
                operatorTop--;
            }
            operatorStack[++operatorTop] = token;
        } else {
            printf("Invalid character in the expression: %c\n", token);
            exit(1);
        }
    }
    
    // Process remaining operators
    while (operatorTop >= 0) {
        applyOperator(operatorStack[operatorTop], operandStack, &operandTop);
        operatorTop--;
    }
    
    // The result should be at the top of the operand stack
    return operandStack[operandTop];
}

int main() {
    char expression[MAX_EXPRESSION_SIZE];
    printf("Enter an expression: ");
    fgets(expression, sizeof(expression), stdin);
    expression[strcspn(expression, "\n")] = '\0'; // Remove newline character
    
    int result = operatorPrecedenceParse(expression);
    printf("Result: %d\n", result);
    
    return 0;
}
