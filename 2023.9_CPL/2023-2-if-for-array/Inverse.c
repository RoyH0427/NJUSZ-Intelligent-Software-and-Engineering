#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverseString(char *str, int start, int end)
{
    while (start < end)
    {
        char temp = str[start];
        str[start] = str[end];
        str[end] = temp;
        start++;
        end--;
    }
}

int main()
{
    int n, k;
    scanf("%d", &n);
    getchar(); // 消耗第一行末尾的换行符
    char *sequence = (char *)malloc((n + 1) * sizeof(char));
    fgets(sequence, n + 1, stdin);
    scanf("%d", &k);

    // 移除末尾的换行符
    if (sequence[strlen(sequence) - 1] == '\n')
    {
        sequence[strlen(sequence) - 1] = '\0';
    }

    // 翻转前半部分 [0, k-1]
    reverseString(sequence, 0, k - 1);
    // 翻转后半部分 [k, n-1]
    reverseString(sequence, k, n - 1);

    printf("%s\n", sequence);
    free(sequence);
    return 0;
}
