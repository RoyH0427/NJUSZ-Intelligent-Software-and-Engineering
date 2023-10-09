#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    // Initialize an array to store the count of each number
    int count[100001] = {0}; // Using an array to count the occurrences of numbers

    // Read and process the input numbers
    for (int i = 0; i < 2 * n - 1; i++)
    {
        int num;
        scanf("%d", &num);
        count[num]++; // Increment the count for the current number
    }

    // Find the single number by looking for the number with a count of 1
    for (int i = 1; i <= n * 10; i++)
    {
        if (count[i] == 1)
        {
            printf("%d\n", i);
            break;
        }
    }

    return 0;
}
