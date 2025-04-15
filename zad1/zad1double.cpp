#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

double f(double x) {
    return sin(pow(x,3));
}

double dxdf(double x) {
    return 3*pow(x,2)*cos(pow(x,3));
}

double Dh1 (double x, double h) {
    return (f(x+h) -f(x)) / h;
}

double Dh2 (double x, double h) {
    return (f(x+h) -f(x-h)) / (2*h);
}

double EDh1 (double x, double h) {
    return fabs(Dh1(x,h) - dxdf(x));
}

double EDh2 (double x, double h) {
    return fabs(Dh2(x,h) - dxdf(x));
}

int main () {
    std::ofstream outfile("double.txt");
    double x=0.2;
    for (double h = 0.9; h >= 1e-10; h *= 0.9) {
        double blad1 = EDh1(x,h);
        double blad2 = EDh2(x,h);
        outfile << h << "\t" << blad1 << "\t" << blad2 << "\n";
    }
    outfile.close();
}