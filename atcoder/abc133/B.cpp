// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;
bool isSqrtint(vector<int>&arr, vector<int>&brr){
        int d = arr.size();

        int sum=0;
        for (int i=0;i<d;i++){
            sum+=(arr[i]-brr[i])*(arr[i]-brr[i]);
        }
        int sr = sqrt(sum);
        // cout<<sr<<endl;

        return (sr*sr==sum);
    }
int main() {
	// int a, b, c; cin >> a >> b >> c;
	// cout << "The sum of these three numbers is " << a + b + c << "\n";

	int n,d;
	cin>>n>>d;
	vector<vector<int>> vec;
	for(int i=0;i<n;i++){
		vector<int> arr(d);
		for(int j=0;j<d;j++){
			cin>>arr[j];
			// cout<<arr[j]<<" ";
		}
		// cout<<endl;
		vec.push_back(arr);
	}
	int cnt=0;
	for(int i=0;i<n;i++){
		auto x = vec[i];
		for(int j=i+1;j<n;j++){
			// cout<<i<<" "/<<j<<endl;
			auto y = vec[j];
			if (isSqrtint(x,y)){
                    cnt+=1;
                }

		}
	}
	cout<<cnt<<endl;

	return 0;
}
