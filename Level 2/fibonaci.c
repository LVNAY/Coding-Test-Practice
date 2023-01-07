#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int a = 0;
    int b = 1;
    int c = 0;
    int answer = 0;
    int i;
    for (i = 0; i < n; i++)
    {
        if (i % 2 == 0)
        {
            b = (a + b) % 1234567;
            answer = b;
        }
        else
        {
            a = (a + b) % 1234567;
            answer = a;
        }
    }

    return answer;
}