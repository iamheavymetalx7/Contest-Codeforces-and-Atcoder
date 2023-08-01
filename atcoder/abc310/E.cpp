//author: sushmanth
 
#include <bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);
#define inf 10000000000000LL
#define mod 1000000007
#define sz 1000001
#define pb push_back
#define nline '\n'
typedef long long int ll;

ll n;
ll dp[1000001][2];
string a;


ll solve(ll i , ll j){
     
    if(i == n) return 0;
    if(dp[i][j] != -1) return dp[i][j];
    
    ll nand = (j & (a[i] - '0')) ^ 1;
    ll ans = solve(i + 1 , nand) + nand;
    
    dp[i][j] = ans;
    return ans;
}

void answer(){
    
    cin >> n;
    for(ll i = 0;i < n;++i){
        dp[i][0] = -1;
        dp[i][1] = -1;
    }
    
    cin >> a;
    
    
    ll ans = 0;
    for(ll i = 0;i < n;++i){
        ans += (solve(i + 1 , a[i] - '0') + (a[i] - '0'));
    }
    
    
    cout << ans << nline;
    

}
 
int main(){
    
    
    fastio
    ll T = 1;
    while(T--){
        answer();
    }
    
    return 0;
}