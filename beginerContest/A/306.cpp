#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int n;
    string s;
    cin >> n;
    cin >> s;
    string result;
    for(char c :s){
        result += c;
        result += c;
    }
    cout <<  result <<endl;
    
}