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
    
    void solve()
    {	int n;
        cin>>n;
        vector<int> p(n);
        for(int i=0;i<n;i++) cin>>p[i];


        vector<long double> p9(n+1,1);

        for(int i=2;i<=n;i++){
            p9[i]=0.9*p9[i-1];
        }

        for(int i=2;i<=n;i++){
            p9[i]+=p9[i-1];
        }

        // for(int i=0;i<=n;i++){
        //     cout<< p9[i]<<" ";
        // }
        // cout<<endl;

        vector<long double> dp(n+1, -1e18);
        dp[0]=0;

        for(int i=0;i<n;i++){
            auto ndp = dp;
            for(int j=0;j<=i;j++){
                if(j+1<=n){
                    ndp[j+1]=max(ndp[j+1],dp[j]*0.9+p[i]);
                }
            }
            dp = ndp;
        }

        long double ans = -1e18;

        for(int i=1;i<=n;i++){
            long double rem = 1200.0/(sqrt(1.0*i));
            ans = max(ans,(dp[i]/p9[i])-rem);
        }

        cout<<fixed<<setprecision(15);cout<<ans<<endl;
     
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