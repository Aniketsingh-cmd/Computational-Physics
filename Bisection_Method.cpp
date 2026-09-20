#include <iostream>
#include <cmath>
/*
   TRANSPARENCY:
   Handwritten Approach is Shared. Code Is Not Generated With AI
   But Beautified With Gemini 
*/
using namespace std;

double f(double x) { //x^3 - x - 1
    return (x * x * x) - x - 1; 
}

double bisection_root(double a, double b, double error_percent) {
    double c = a; 
    double previous_c = 0; //Consider this As P.I 
    double current_error_percent = 100;
    while (current_error_percent >= error_percent) {
        previous_c = c; 
        c = (a + b) / 2.0; //C.I
        if (previous_c != 0.0 && c != 0.0) { 
            current_error_percent = abs((previous_c - c) / c) * 100.0;
            //Formula is ((P.I -C.I)/C.I ) x 100
            //abs is absolute value , |a| where result is positive
        }
        if (f(c) == 0.0) {
            return c;
        }
        else if (f(c) * f(a) < 0) {
            b = c;
        }
        else {
            a = c;
        }
    }
    cout << "Closest Error " <<current_error_percent  << "% \n";
    return c;
}

int main() {
    double a = 0.0;
    double b = 1.0;
    double error_percent = 0.5; 
    double root = 0.0;
    
    while (true) {
        double val1 = f(a);
        double val2 = f(b);
        
        if (val1 * val2 < 0) {
            cout << "Root lies between " << a << " and " << b << " \n";
            
            root = bisection_root(a, b, error_percent);
            break; 
        }
        

        a = b;
        b = b + 1.0;
    }
    
    cout << "The calculated root is: " << root << "\n";
    
    return 0;
}