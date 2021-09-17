#include <iostream>

using namespace std;

int main() {
    int num; // declares a variable that will hold the number for testing

    // Outputs a message to the user and instructs the user on what to do.
    cout << "Enter a number to check whether it's a prime number: ";
    // Makes the user enter an integer.
    cin >> num;

    // 2, 3 and 5 are the first prime numbers so the program sorts these numbers out first
    if(num == 2 || num == 3 || num == 5)
    {
        cout << "The number " << num << " is a prime number." << endl;
    }
    /* 1 is automatically excluded but by the rules I am using the program includes it as a prime number.
     So this prevents that from happening. */
    else if (num == 1)
    {
        cout << "The number " << num << " is not a prime number." << endl;
    }

    /* For a number to be a prime number, it should not be a multiple of 2, 3 or 5.
    This program checks whether a program is not divisible by 2, 3 or 5.*/
    else if (num % 2 != 0 && num % 3 != 0 and num % 5 != 0)
    {
        cout << "The number " << num << " is a prime number." << endl;
    }
    // Any other number is treat as not a prime number.
    else
    {
        cout << "The number " << num << " is not a prime number." << endl;
    }
    return 0;
}
