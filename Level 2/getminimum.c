#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int static compare(const void* first, const void* second)
{
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}

int solution(int A[], size_t A_len, int B[], size_t B_len) {
    int answer = 0;
    int C = 0;
    qsort(A, A_len, sizeof(A[0]), compare);
    qsort(B, B_len, sizeof(B[0]), compare);
    int i;

    for (i = 0; i < A_len; i++) {
        C = A_len - i - 1;
        answer += A[i] * B[C];
    }

    return answer;
}