# latihan
# Program perulangan Indira Rully 312110354

### Berikut algoritma latihan 1.1 (Menentukan nilai terbesar dari 2 input bilangan)

#include<iostream.h>
#include<conio.h>

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

### Berikut algoritma latihan 1.2 (Perulangan / nested dengan for)

for i in range(3):
  print('Perulangan luar [i] = ', i)

for j in range(5):
  print('Perulangan dalam [i, j] = ', str(i) + ', ' + str(j))

### Berikut algoritma latihan 2.1 (Mengurutkan 3 inputan dari yang terkecil)

#include <iostream>
using namespace std;

int main(){
    int a, b, c;

    cout << "Masukkan nilai A : "; cin >> a;
    cout << "Masukkan nilai B : "; cin >> b;
    cout << "Masukkan nilai C : "; cin >> c;

    if(a<b && a<c){
        if(b<c){
            cout << a << ' ' << b << ' ' << c << endl;
        }else{
            cout << a << ' ' << c << ' ' << b << endl;
        }
    }else if(b<a && b<c){
        if(a<c){
            cout << b << ' ' << a << ' ' << c << endl;
        }else{
            cout << b << ' ' << c << ' ' << a << endl;
        }
    }else{
        if(b<a){
            cout << c << ' ' << b << ' ' << a << endl;
        }else{
            cout << c << ' ' << a << ' ' << b << endl;
        }
    }

    return 0;
}
