#include <bits/stdc++.h>
using namespace std;
#define int long long
#define pi (3.141592653589)
#define mod 1000000007
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
vector<int> fac;
vector<int> inv(2001, 1);



int poww(int a, int b) {
    int val = 1;
    while (b > 0) {
        if (b & 1) {
            val = val * a;
            val %= mod;
        }
        b = b >> 1;
        a = a * a;
        a %= mod;
    }
    return val;
}

void modfac() {
    int f = 1;
    fac.pb(f);
    for (int i = 1; i <= 2000; i++) {
        f *= i;
        f %= mod;
        fac.pb(f);
    }

    int modinv = poww(f, mod - 2);
    inv[2000] = modinv;
    for (int i = 2000; i >= 2; i--) {
        modinv *= i;
        modinv %= mod;
        inv[i - 1] = modinv;
    }
}

int nCr(int n, int r) {

    if (n-r>=0&& r>=0){
    return 1LL * fac[n] * inv[r] % mod * inv[n - r] % mod;
    }
    else{
        return 0;
    }
}



void solve() {

    // for(int i=0;i<=2000;i++){
    //     cout<<inv[i]<<" ";
    // }
    // cout<<endl;

    // for(int i=0;i<=2000;i++){
    //     cout<<fac[i]<<" ";
    // }
    // cout<<endl;
    int m, k;
    cin >> m >> k;
    //m-k red balls and k blue balls
    int r = m - k;
    int b = k;

    for (int j = 1; j <= k; j++) {
        int x = nCr(r + 1, j);
        int y = nCr(b - 1, j - 1);
        int ans =x*y;
        ans=((ans%mod)+mod)%mod;
        cout<<ans<<endl;
    }
}

signed main() {
    fast
    // int t; cin>>t; while(t--)
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    modfac();
    solve();
    return 0;
}
