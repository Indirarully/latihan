latihan 1.1

#include<iostream.h>
#include<conio.h>

/**
* bundet.com
* Menentukan Nilai terbesar dari 2 input bilangan
*/

void main() {
    int a, b;
    cout << "Menentukan Nilai terbesar 2 buah input \n";
    cout << "masukkan nilai 1 : "; cin >> a;
    cout << "masukkan nilai 2 : "; cin >> b;

    if ( a > b )
        cout << "nilai terbesar  : " << a << endl;
    else
        cout << "nilai terbesar  : " << b << endl;

    getch();
}
