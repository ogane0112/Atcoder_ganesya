#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int n;
  cin >> n;
  int a,b,check,ans;
  check = n/5;
  
  
  a = abs(n-(check*5));
  b = abs(n-((check+1)*5));
  
  ans = min(a,b);
  if (ans == a){
    cout << check*5 << endl;
  }else{
    cout << (check+1)*5 << endl;
  }
  
}