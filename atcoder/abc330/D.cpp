// #include <bits/stdc++.h>
//     using namespace std;
//     #define int long long
//     #define pi (3.141592653589)
//     #define mod 1000000007
//     #define float double
//     #define ff first
//     #define ss second
//     #define mk make_pair
//     #define pb push_back
//     #define rep(i, start, end) for (int i = start; i < end; i++)
//     #define ld long double
//     #define fast ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
//     int inf = 1000000000000000000;
//     using ii = pair<int, int>;
    
//     void solve()
//     {
//         int n;
//         cin>>n;
//         vector<vector<char>> mat(n,vector<char>(n));

//         for(int i=0;i<n;i++){
//             for(int j=0;j<n;j++){
//                 cin>>mat[i][j];
//             }
//         }

//         // for each row and column, 
//         //count kitna unke upar and neeche hai

//         // same for kitna left and right hai

//         vector<vector<int>> up(n,vector<int>(n,0));
//         vector<vector<int>> down(n,vector<int>(n,0));
//         vector<vector<int>> left(n,vector<int>(n,0));
//         vector<vector<int>> right(n,vector<int>(n,0));

//         // for(int i=0;i<n;i++){
//         //     int cnter = 0;
//         //     for(int j=0;j<n;j++){
//         //         if (mat[i][j]=='o'){
//         //             left[i][j]=cnter;
//         //             cnter++;

//         //         }

//         //     }
//         // }

//         for(int i=0;i<n;i++){
//             int cnter = 0;
//             for(int j=0;j<n;j++){
//                 if (mat[i][j]=='o'){
//                     cnter++;
//                     right[i][j]=cnter;

//                 }
//                 else{
//                     if (j>0) right[i][j] = right[i][j-1];
//                 }

//             }
//         }

//         for(int i=0;i<n;i++){
//             int cnter = 0;
//             for(int j=n-1;j>=0;j--){
//                 if (mat[i][j]=='o'){
//                     cnter++;

//                     left[i][j]=cnter;
//                     // cnter++;

//                 }
//                 else{
//                     if (j<n-1) left[i][j] = left[i][j+1];
//                 }

//             }
//         }

      

//         for(int i=0;i<n;i++){
//             int cnter = 0;
//             for(int j=0;j<n;j++){
//                 if (mat[j][i]=='o'){
//                     cnter++;

//                     down[j][i]=cnter;
//                     // cnter++;

//                 }
//                 else{
//                     if (j>0) down[j][i] = down[j-1][i];

//                 }

//             }
//         }

//         for(int i=0;i<n;i++){
//             int cnter = 0;
//             for(int j=n-1;j>=0;j--){
//                 if (mat[j][i]=='o'){
//                     cnter++;

//                     up[j][i]=cnter;
//                     // cnter++;

//                 }
//                 else{
//                     if (j<n-1) up[j][i] = up[j+1][i];

//                 }

//             }
//         }


//         cout<<"up: \n";
//         for(int i=0;i<n;i++){
//             for(int j=0;j<n;j++){
//                 cout<<up[i][j];
//             }
//             cout<<endl;
//         }
//         cout<<"down: \n";
//         for(int i=0;i<n;i++){
//             for(int j=0;j<n;j++){
//                 cout<<down[i][j];
//             }
//             cout<<endl;
//         }


//         cout<<"left: \n";
//         for(int i=0;i<n;i++){
//             for(int j=0;j<n;j++){
//                 cout<<left[i][j];
//             }
//             cout<<endl;
//         }

//         cout<<"right: \n";
//         for(int i=0;i<n;i++){
//             for(int j=0;j<n;j++){
//                 cout<<right[i][j];
//             }
//             cout<<endl;
//         }


//         // for(int i=0;i<n;i++){
//         //     for(int j=0;j<n;j++){
//         //         cout<<mat[i][j];
//         //     }
//         //     cout<<endl;
//         // }


//         int ans = 0;
//         for(int i=0;i<n;i++){
//             for(int j=0;j<n;j++){
//                 int left_o=0,up_o=0,down_o=0,right_o=0;
//                 // cout<<i<<" "<<j<<endl;
//                 if (mat[i][j]=='x'){
//                     continue;
//                 }
                
//                 if (i>0){
//                     up_o = up[0][j]-up[i][j];
//                     // cout<<"up: "<<up[i][0]<<" "<<up[i][j]<<endl;
//                 }
//                 if (j>0){
//                     left_o = left[i][0]-left[i][j];
//                     // cout<<"left: "<<left[0][j]<<" "<<left[i][j]<<endl;

//                 }
//                 if (j<n-1){

//                     right_o = right[i][n-1]-right[i][j];
//                     // cout<<"right: "<<right[i][n-1]<<" "<<right[i][j]<<endl;


//                 }
//                 if (i<n-1){
//                     down_o  = down[n-1][j]-down[i][j]; 
//                     // cout<<"down: "<<down[i][n-1]<<" "<<down[i][j]<<endl;
// // 
//                 }
//                 cout<<i<<" "<<j<<": left and right "<<left_o<<" "<<right_o<<endl;

//                 cout<<i<<" "<<j<<": up and down "<<up_o<<" "<<down_o<<endl;
//                 cout<<"this will be added: "<<(left_o*down_o)+(right_o*down_o)<<"*********************"<<endl;
//                 ans+=  (left_o*down_o)+(right_o*down_o);

//             }
            
//         }
//         cout<<ans<<endl;
    
//     }
    
//     signed main()
//     {
//         fast
//         // int t; cin>>t; while(t--)
    
//         #ifndef ONLINE_JUDGE
//         freopen("input.txt","r",stdin);
//         freopen("output.txt","w",stdout);
//         #endif
//         solve();
//         return 0;
//     }



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
    {   int n;
        cin>>n;
        vector<vector<char>> mat(n,vector<char>(n,0));

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                cin>>mat[i][j];
            }
        }

        vector<int> bi(n,0), bj(n,0);

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if (mat[i][j]=='o'){
                    bi[i]++;
                    bj[j]++;
                }
            }
        }
        int res= 0;


        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if (mat[i][j]=='o'){
                res +=  (bi[i]-1)*(bj[j]-1);

                }

            }}

        cout<<res<<endl;
    
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