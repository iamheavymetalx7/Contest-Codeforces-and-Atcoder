#include <bits/stdc++.h>
using namespace std;
#define int long long
#define pi (3.141592653589)
#define mod 998244353
#define float double
#define ff first
#define ss second
#define mk make_pair
#define pb push_back
#define rep(i, start, end) for (int i = start; i < end; i++)
#define ld long double
#define fast ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
int inf = 1000000000000000000;
using ii = pair<int, int>;

int power(int a,int b){
  int x=1,y=a;
  while(b>0){
    if(b&1ll){
      x=(x*y)%mod;
    }
    y=(y*y)%mod;
    b>>=1;
  }
  return x%mod;
}
int modular_inverse(int n){
  return power(n,mod-2);
}

// const int mod = 998244353;
void solve()
{ int n;
cin>>n;

vector<int> vec(n+1);
for(int i=1;i<=n;i++){
    cin>>vec[i];
}


int inv = modular_inverse(n);
vector<int> dp(n+1,0);
vector<int> summ(n+1,0);

for(int i=0;i<n;i++){
    dp[i+1] = (summ[i]*inv+inv)%mod;
    summ[i+1] = (summ[i]+dp[i+1])%mod;
}

int ans =0;

// for(int i=0;i<=n;i++){
//     cout<<vec[i]<<" ";
// }
// cout<<endl;

// for(int i=0;i<=n;i++){
//     cout<<dp[i]<<" ";
// }
// cout<<endl;

// for(int i=0;i<=n;i++){
//     cout<<summ[i]<<" ";
// }
// cout<<endl;

for(int i=1;i<=n;i++){
    ans=(ans+ dp[i]*vec[i])%mod;
}

cout<<ans<<endl;


}

signed main()
{
    fast
    // int t; cin>>t; while(t--)

    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    solve();
    return 0;
}