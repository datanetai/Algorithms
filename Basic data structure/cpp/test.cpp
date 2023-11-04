#include <iostream>

int x = 0;

int B(int &y);

int A(int &y)
{
    int x = 2; // 2
    y = y + 1; // 1
    return B(y) + x;
}

int C(int &y) // 1
{
    int x = 3;
    return A(y) + x + y;
}

int B(int &y) // 1
{
    if (y == 1)
        return C(x) + y; //
    else
        return x + y;
}

int main()
{
    std::cout << A(x) << std::endl;
    return 0;
}
