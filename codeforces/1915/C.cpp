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

    bool isSquare(int x){
        int n = sqrt(x);
        if (n*n ==x){
            return true;
        }
        return false;
    }
    
    void solve()
    {
        int k;
        cin>>k;
        vector<int> arr(k);
        int sum =0;
        for(int i=0;i<k;i++){
            cin>>arr[i];
            sum+=arr[i];

        }
        // cout<<sum<<endl;

        if(isSquare(sum)){
            cout<<"Yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }
        


    
    
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