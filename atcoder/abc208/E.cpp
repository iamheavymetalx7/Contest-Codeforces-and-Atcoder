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
    int n,k;
    map<pair<pair<int,int>,pair<bool,bool> >,int>dp ;
    vector<int> v;

    int recur(bool tight,bool l_zero,int pdt,int idx){
        if (idx>=v.size()){
            if (pdt<=k){
                return 1;
            }
            return 0;
        }
        if(dp.find({{idx,pdt},{tight,l_zero}})!=dp.end())return dp[{{idx,pdt},{tight,l_zero}}];
        int ans =0;

        int ub = tight?v[idx]:9;
        for(int dig=0;dig<=ub;dig++){
            bool isleading = (dig==0)&&(l_zero);
            
            if(!isleading){
                ans+=recur(tight&(dig==ub),isleading,pdt*dig,idx+1);
            }
            else{
                ans+=recur(tight&(dig==ub),isleading,pdt,idx+1);
            }
        }
        return dp[{{idx,pdt},{tight,l_zero}}] =ans;

    }
    
    void solve()
    {
        cin>>n>>k;

        while(n){
            v.pb(n%10);
            n/=10;
            }
        reverse(v.begin(),v.end());        
        int val = recur(1,1,1,0);
        cout<<val-1<<endl;
    
    
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