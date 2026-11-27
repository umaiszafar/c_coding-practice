#include<stdio.h>
int main()
{
    float a,b;
    char operator;
    printf("Enter first number: ");
    scanf("%f", &a);
    printf("Enter an operator (+, -, *, /): ");
    scanf(" %c", &operator);
    printf("Enter second number: ");
    scanf("%f", &b);
    switch(operator)
    {
        case '+':
            printf("%.2f + %.2f = %.2f\n", a, b, a + b);
            break;
        case '-':
            printf("%.2f - %.2f = %.2f\n", a, b, a - b);
            break;
        case '*':
            printf("%.2f * %.2f = %.2f\n", a, b, a * b);
            break;
        case '/':
            if(b != 0)
                printf("%.2f / %.2f = %.2f\n", a, b, a / b);
            else
                printf("Error! Division by zero.\n");
            break;
        default:
            printf("Invalid operator!\n");
    }

}