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
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        vector<int> mx(26);

        int l=0;

        while(l<n){
            int r=l+1;
            while(r<n && s[r]==s[l]){
                r++;
            }
            int c = s[l]-'a';
            mx[c]=max(r-l,mx[c]);
            l=r;

        }
        int ans =0;
        for(int i=0;i<26;i++){
            ans+=mx[i];
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