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
        int n,m;
        cin>>n>>m;
        vector<int> arr(m);
        int sum=0;
        for(int i=0;i<m;i++){
            cin>>arr[i];
            sum+=arr[i];
            // cout<<arr[i]<<endl;
        }

        if (sum<n){
            cout<<-1<<endl;
            return;
        }

        int i=0;
        int cnt=0;

        vector<int> c(32);

        for(int i=0;i<m;i++){
            c[log2(arr[i])]+=1;
        }

        // for(int i=0;i<61;i++){
        //     cout<<c[i]<<" ";
        // }
        // cout<<endl;

        while(i<32){

            if ((n & (1<<i))){
                // cout<<i<<" "<<(1<<i)<<" "<<c[i]<<endl;
                if (c[i]>0){
                    c[i]-=1;
                }
                else{
                    while(c[i]==0){
                        i+=1;
                        cnt+=1;
                    }
                    c[i]-=1;
                    continue;
                }
            }
            c[i+1]+=(c[i]/2);
            i+=1;
        }

        cout<<cnt<<endl;
        // cout<<"**************"<<endl;
    
    
    }
    
    signed main()
    {
        fast

    
        #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
        #endif
        int t; cin>>t; 
        while(t--)
        solve();
        return 0;
    }