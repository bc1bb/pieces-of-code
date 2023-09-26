#include<iostream>
#include<string>

using namespace std;

string currency_string(string currency) { // this function is used to standardize the different ways to write currencies
    if(currency == "euro" || currency == "euros" || currency == "eur" || currency == "Eur" || currency == "EUR") {
        currency = "EUR";
    } else if(currency == "dollar" || currency == "dollars" || currency == "usd" || currency == "Usd" || currency == "USD") {
        currency = "USD";
    } else if(currency == "pound" || currency == "pounds" || currency == "pound sterling" || currency == "gbp") {
        currency = "GBP";
    } else {
        currency="ERR";
    }

    return currency;
}

float to_eur(float base, const string& base_currency) { // this function is used to convert from any currency to EUR
    float result;

    if(base_currency == "GBP") result = base * 1.19;
    if(base_currency == "USD") result = base * 0.86; 

    return result;
}

float to_gbp(float base, const string& base_currency) { // this function is used to convert from any currency to GBP
    float result;

    if(base_currency == "EUR") result = base * 0.84;
    if(base_currency == "USD") result = base * 0.73;

    return result;
}

float to_usd(float base, const string& base_currency) { // this function is used to convert from any currency to USD
    float result;

    if(base_currency == "GBP") result = base * 1.37;
    if(base_currency == "EUR") result = base * 1.16;

    return result;
}

int main() {
    float base;
    float result = 0;

    string currency;
    string final_currency;

    while(true) { // we want our program to be an infinite loop until user asks to stop it (see first if statement)
        cout << "Type base currency (USD, EUR, GBP): "; // `cout` gives input to user
        cin >> currency; // `cin` puts user input (until enter) in a variable

        if(currency == "stop") return 0;

        cout << "How much " + currency + " would you like to convert: ";
        cin >> base;

        cout << "In which currency should I convert (USD, EUR, GBP): ";
        cin >> final_currency;

        currency = currency_string(currency);
        final_currency = currency_string(final_currency);

        if(currency == "ERR" || final_currency == "ERR") {
            cout << "Unable to recognize one or more currency." << endl; // in case the user asks for an unknown currency
        } else if(currency == final_currency) {
            cout << endl << base << " " << currency << " = " << base << " " << final_currency << endl; // in case the user asks to convert a currency into itself, no calculation needed
        }

        if(final_currency == "EUR") result = to_eur(base, currency);
        if(final_currency == "USD") result = to_usd(base, currency);
        if(final_currency == "GBP") result = to_gbp(base, currency);

        cout << endl << base << " " << currency << " = " << result << " " << final_currency << endl;
        // Output should look like: 25 EUR = 21 GBP
    }
}