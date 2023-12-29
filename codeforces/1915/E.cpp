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
        vector<int> a(n);
        for(int i=0;i<n;i++){
            cin>>a[i];
            if(i%2==1){
                a[i]*=-1;
            }
        }

        // for(int i=0;i<n;i++){
        //     cout<<a[i]<<" ";
        // }
        // // cout<<endl;


        map<int,int> mp;
        mp[0]=-1;

        int cur_sum =0;
        for(int i=0;i<n;i++){
            cur_sum+=a[i];
            if (mp.count(cur_sum)>0){
                cout<<"YES"<<endl;
                return;
            }
            mp[cur_sum]=i;
        }

        cout<<"NO"<<endl;

    
    
    }
    
    signed main()
    {
        fast
        #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
        #endif

    

        int t; cin>>t; 
        while(t--) solve();
        return 0;        

    }