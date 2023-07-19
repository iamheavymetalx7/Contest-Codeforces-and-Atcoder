#include <bits/stdc++.h>
using namespace std;

#define ll int

vector<vector<ll>> vec(31 , vector<ll> (31));
// coopied from shivrendra2003
//20 * 2 ^ 20

ll dp[22][(1 << 21)];

ll MOD = 1e9 + 7;

ll solve(ll i , ll f , ll n){
    if(f == 0) return 1;

    if(dp[i][f] != -1){
        return dp[i][f];
    }

    ll ans = 0;

    for(int j=0;j<n;j++){
        if(f & (1 << j)){
            if(vec[i][j]){
                ans = (ans + solve(i-1 , f ^ (1 << j) , n)) % MOD;
            }
        }
    }

    return dp[i][f] = ans;
}

int main(){
    ll n;
    cin>>n;

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>vec[i][j];
        }
    }

    memset(dp , -1 , sizeof(dp));

    ll f = (1 << n) - 1;

    ll ans = solve(n-1 , f , n);

    cout << ans << "\n";
return 0;
}
