#include<stdio.h>
int main()
{
    int num, reverse =0;
    printf("Enter a number: ");
    scanf("%d",&num);
    while(num != 0)
    {
        reverse = reverse * 10;
        reverse = reverse + num%10;
        num = num/10;
    }
    printf("Reverse of the number is: %d", reverse);
    return 0;
}