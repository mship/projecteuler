// going through first 100 problems of Project Euler in Python
// by Michael Shippee
// Here is the problem:

// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

// What is the 10 001st prime number?


// I will use the sieve of Eratosthenes to find prime numbers and store them until I have 10,001

#include <stdio.h>

#define BUFSIZE 150000

int main(void){
    int allnums[BUFSIZE];
    int primes[10000]; // starts at 0, so this is 10,001 entries
    int primes_tracker = 0; // used as an index to enter prime numbers into list

    // quick loop to fill out the array so that the Sieve has bits to turn off
    for(int l = 0; l<BUFSIZE; l++){ 
        allnums[l] = 1;
    }

    // iterate through, setting values to 0 if they are multiples of lower numbers
    for(int i = 2; i<BUFSIZE; i++){
        if(allnums[i] == 0){
            continue;
        }
        primes[primes_tracker] = i;
        primes_tracker++;
        for(int j = 0; j<BUFSIZE; j++){
            if(j%i == 0){
                allnums[j] = 0;
            }
        }
    }
    printf("%d\n", primes[10000]); // returns 104743
    return 0;
}