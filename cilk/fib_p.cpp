//g++ -fcilkplus -lcilkrts fib_p.cpp -o out
#include<cilk/cilk_api.h>
#include<cilk/cilk.h>
#include<stdio.h>
#include<stdlib.h>
#include<iostream>

int fib(int n)
{
    if (n < 2) 
        return n;
    else 
    {
        int rst = 0;
        int x = cilk_spawn fib(n-1);
        int y = cilk_spawn fib(n-2);
        cilk_sync;
        return x + y;
    }
}

int main(int argc, char **argv)
{
    std::cout<<fib(atoi(argv[1]))<<std::endl;
    return 0;
}
