#include <iostream>
using namespace std;

string encrypt(string plaintext, int key) {
    string ciphertext = "";
    for (int i = 0; i < plaintext.length(); i++) {
        if (isalpha(plaintext[i])) {
            char shifted = (toupper(plaintext[i]) - 'A' + key) % 26 + 'A';
            ciphertext += shifted;
        } else {
            ciphertext += plaintext[i];
        }
    }
    return ciphertext;
}

string decrypt(string ciphertext, int key) {
    string plaintext = "";
    for (int i = 0; i < ciphertext.length(); i++) {
        if (isalpha(ciphertext[i])) {
            char shifted = (toupper(ciphertext[i]) - 'A' - key + 26) % 26 + 'A';
            plaintext += shifted;
        } else {
            plaintext += ciphertext[i];
        }
    }
    return plaintext;
}

int main() {
    string plaintext;
    int key;

    cout << "Enter the plaintext: ";
    getline(cin, plaintext);

    cout << "Enter the key (a number between 1 and 25): ";
    cin >> key;

    string ciphertext = encrypt(plaintext, key);
    string decryptedText = decrypt(ciphertext, key);
    cout<<"-----------------------------------"<<endl;

    cout << "Ciphertext: " << ciphertext << endl;
    cout << "Decrypted text: " << decryptedText << endl;

    return 0;
}
