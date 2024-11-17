#include <iostream>

using namespace std;

int main() {
    int a, b;

    // Ask the user for two integers
    cout << "Enter first integer: ";
    cin>>a;

    cout << "Enter second integer: ";
    cin >> b;

    // Calculate the sum
    int sum = a + b;

    // Output the result
    cout << "The sum of " << a << " and " << b << " is " << sum << endl;

    return 0;
}
