#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll mod = 1e9 + 7;

ll dp[10005][2][100];
ll f(int id,bool tight,ll sum,ll d,string &s){
    int syz = s.size();

    if(id == syz){
        return (sum == 0);
    }
    if(dp[id][tight][sum] != -1)return dp[id][tight][sum];

    int ub = (tight == 1) ? (s[id] - '0') : 9;

    ll ways = 0;
    for(int dig = 0;dig <= ub;dig++){
        ways += f(id + 1,(tight && (dig == ub)), (sum + dig)%d,d,s );
        ways %= mod;
    }

    return  dp[id][tight][sum] =  ways;
}

void sol(){
  memset(dp,-1,sizeof dp);

    string s; cin>>s;
    ll d; cin>>d;

    ll ans = f(0,1,0,d,s);
     ans = (ans - 1 + mod)%mod;
    cout<<ans <<"\n";
}

int main()
{
    sol();
    return 0;
}