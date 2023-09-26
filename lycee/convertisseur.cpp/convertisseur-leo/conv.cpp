// Fait pour Léo a partir d'un algorigramme
#include<iostream>
#include<string>

using namespace std;

int main() {
    float yen;
    float cad;
    float gbp;
    string choice;
    float convert;

    yen = 129.16;
    cad = 1.47;
    gbp = 0.86;

    while(true) {
        cout << "1 - Euro -> Yen" << endl;
        cout << "2 - Euro -> Canadian Dollar" << endl;
        cout << "3 - Euro -> Pound sterling" << endl;

        cin >> choice;
        
        if(choice == "1") {
            cout << "How much would you like to convert ? ";
            cin >> convert;

            cout << endl << convert * yen << endl;
        } else if(choice == "2") {
            cout << "How much would you like to convert ? ";
            cin >> convert;

            cout << endl << convert * cad << endl;
        } else if(choice == "3") {
            cout << "How much would you like to convert ? ";
            cin >> convert;

            cout << endl << convert * gbp << endl;
        }
    }
}