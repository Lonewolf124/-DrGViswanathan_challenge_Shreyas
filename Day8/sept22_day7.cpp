#include <iostream>
using namespace std;

int bit(string operation, int &x) {
    if (operation == "X++" or operation == "++X") {
        x++;
    } 
    else if (operation == "X--" or operation == "--X") {
        x--;
    }

    return x;
}

int main() {
    // Number of statements in the program
    int num;
    cin >> num;

    int x = 0;
    string operation;

    for (int i = 0; i < num; i++) {
        cin >> operation;
        bit(operation, x); // Update x in place
    }

    cout << x << endl; // Output the final result

    return 0;
}
