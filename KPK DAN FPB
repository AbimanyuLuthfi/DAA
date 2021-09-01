Menghitung FPB

Algoritma
Step 1 Jika n = 0, return nilai m sebagai hasil dan stop. Jika tidak, kemabli ke step 2
Step 2 Bagi nilai m dengan n, masukkan nilai sisanya ke r.
Step 3 Masukkan nilai n ke m dan nilai r ke n. Kembali ke Step 1

Pseudocode:
While n ≠ 0 do
r  ← m mod n
m  ← n
n  ← r
return m

Menghitung KPK DENGAN FPB

Algoritma
Step 1 Jika nilai ((n ≠ m) && (n > m)), maka step 2 akan dilakukan
Step 2 Bagi nilai m dengan n, masukkan nilai sisanya ke r.
Step 3 Masukkan nilai n ke m dan nilai r ke n.
Step 4 Kalikan nilai n dan m lalu bagi hasil nya dengan nilai r, kemudian masukan nilainya ke dalam z.

Pseudocode:
While ((n ≠ m) && (n > m)) do
r  = m mod n
m  = n
n  = r
z = (n * m / r)

#include <stdio.h>

int FPB(int a, int b){
int r = 0;
    while(b!=0){
        r = a % b;
        a = b;
        b = r;
    }

    return a;
}


int KPK(int a, int b){
    return a*b / FPB(a, b);
}

int main(){
int a=120;
int b=90;
    printf("%d", KPK(KPK(120, 88),36));
    return 0;
}
