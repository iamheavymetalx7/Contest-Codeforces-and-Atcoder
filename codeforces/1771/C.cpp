#include <bits/stdc++.h>
using namespace std;
#ifndef ONLINE_JUDGE
  #include "dbg.h"    
#endif
#define ll long long
#define int ll
#define     lcm(a, b)       (a / __gcd(a, b)) * b
const int M = 1e9+7;

const int N = 1e5 + 9;
vector <int> primes;
bool prime[N];
void sieve(){
  prime[1] = true;
  for(int i = 2; i*i <= N-9; i++) {
    if(!prime[i]) {
      for(int j = i*i; j <= N-9; j+=i) {
        prime[j] = true;
      }
    }
  }
  for(int i=2; i<=N-9; i++) {
    if(!prime[i]) {
      primes.push_back(i);
    }
  }
}

void solve () {
  int n; cin >> n;
  int cnt = 0;
  vector<int> v(n);

  for (int i = 0; i < n; i++) {
    cin >> v[i];
    if(v[i] % 2 == 0) cnt++;
  }
  if(cnt > 1) {
    cout << "YES\n";
    return;
  }
  map<int, int> mp;
  for (int i = 0; i < n; i++) {

    for (int j = 0; primes[j] * primes[j] <= v[i]; j++) {
      if(v[i] % primes[j] == 0) {
        if(mp[primes[j]]) {
          cout << "YES\n";
          return;
        }
        while(v[i] % primes[j] == 0) v[i] /= primes[j];
        mp[primes[j]]++;
      }
    }
    if(v[i] > 1) {
      if(mp[v[i]]) {
        cout << "YES\n";
        return;
      }
      mp[v[i]]++;
    }
  }
  cout << "NO\n";
}

int32_t main () {
  sieve();
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
  int tc = 1, t = 0; 
  #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
  #endif
  cin >> tc; 
  while(tc --) {
    solve();
  }       
}

