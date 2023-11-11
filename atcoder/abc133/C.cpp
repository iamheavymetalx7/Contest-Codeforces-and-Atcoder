#include <bits/stdc++.h>
    using namespace std;
    #define int long long
    #define pi (3.141592653589)
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
    
    void solve()
    {	int l,r;

        int mod = 2019;

        cin>>l>>r;

        if (r-l+1 >= 2019){
            cout<<0<<endl;
        }
        else{
        int ans= inf;
        r=min(r,l+2019);
        for (int i=l;i<=r;i++){
            for(int j=i+1;j<=r;j++){
                int curr =(i*j)%mod;
                ans = min(ans,curr);
            }
        }
        cout<<ans<<endl;

    }
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