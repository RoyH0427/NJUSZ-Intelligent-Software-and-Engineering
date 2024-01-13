#include <iostream>
#include <windows.h>
using namespace std;

void assign_array_cols(int M, int N)
{
    int i, j, a[M][N];
    double time = 0;
    LARGE_INTEGER nBeginTIME, nEndTIME, nFreq;
    QueryPerformanceFrequency(&nFreq);
    QueryPerformanceCounter(&nBeginTIME);
    for (j = 0; j < N; j++)
    {
        for (i = 0; i < M; i++)
        {
            a[i][j] = i + j;
        }
    }
    QueryPerformanceCounter(&nEndTIME);
    time = (double)(nEndTIME.QuadPart - nBeginTIME.QuadPart) / (double)nFreq.QuadPart;
    cout << "Time spent for M = " << M << ", N = " << N << " is " << time << "s" << endl;
}

int main()
{
    assign_array_cols(1000, 10);
    assign_array_cols(100, 100);
    assign_array_cols(10, 1000);
    return 0;
}