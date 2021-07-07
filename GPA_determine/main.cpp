#include <iostream>

using namespace std;

int main()
{
    string program;
    double gpa;
    cout << "Hello, welcome. This program will help you to know the class you will get depending on your GPA." << endl;
    cout << "Please enter the program you are offering in the University of Ghana: " << endl;
    getline(cin, program);
    cout << "Wow!!! You offer " << program << " that's a really good program. You must be very smart ;)" << endl;

    cout << "Please enter your GPA:";
    cin >> gpa;

    if(gpa >= 3.60 && gpa <= 4.00)
    {
        cout << "Congratulation you will have a First Class when you graduate." << endl;
    }

    else if(gpa >= 3.00 && gpa <= 3.59)
    {
        cout << "Oh okay a GPA of " << gpa << " will get you a Second Class(Upper). That's not bad" << endl;
    }

    else if( gpa >= 2.00 && gpa <= 2.99)
    {
        cout << "When you graduate you will get a Second Class(Lower)" << endl;
    }
    else if(gpa >= 1.50 && gpa <= 1.99)
    {
        cout << "You will have a Third Class when you graduate, that's not very good." << endl;
    }
    else if(gpa >= 1.00 && gpa <= 1.49)
    {
        cout << "That's just a Pass, it nothing special." << endl;
    }
    else if(gpa >= 0.00 && gpa <= 0.99)
    {
        cout << "So you came to the university to come and fail? " << endl;
        cout << "You have wasted four years of education for nothing to show for it :( "<< endl;
    }
    else
    {
        cout << "Please " << gpa << " is not a valid GPA." << endl;
    }
    return 0;
}
