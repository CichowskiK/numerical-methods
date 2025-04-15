#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

float f(float x) {
    return sin(pow(x,3));
}

float dxdf(float x) {
    return 1/(pow(cos(x),2));
}

float Dh1 (float x, float h) {
    return (f(x+h) -f(x)) / h;
}

float Dh2 (float x, float h) {
    return (f(x+h) -f(x-h)) / (2*h);
}

float EDh1 (float x, float h) {
    return fabs(Dh1(x,h) - dxdf(x));
}

float EDh2 (float x, float h) {
    return fabs(Dh2(x,h) - dxdf(x));
}

int main () {
    std::ofstream outfile("float.txt");
    float x=0.2;
    for (float h = 0.9; h >= 1e-10; h *= 0.9) {
        float blad1 = EDh1(x,h);
        float blad2 = EDh2(x,h);
        outfile << h << "\t" << blad1 << "\t" << blad2 << "\n";
    }
    outfile.close();
}