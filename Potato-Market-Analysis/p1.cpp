#include<bits/stdc++.h>
using namespace std;

#define V vector
typedef long long int LL;
typedef V<int> vi;
typedef V<LL> vl;
typedef V<pair<int ,int>> vpii;

#define rep(i,a) for(int i = 0; i<a ; i++)
#define fov(i,v) rep(i,v.size())
#define fs first
#define sc second
#define mp make_pair
#define pb push_back

#define el cout<<endl

const int inf = numeric_limits<int>::max();
const LL linf = numeric_limits<LL>::max();

int main(){
	int t;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		int arr[n+1];
		int mult[n+1];
		int add[n+1];
		add[0] = 0;
		mult[0] = 1; 
		rep(i,n){
			cin>>arr[i+1];
			add[i+1] = add[i] + arr[i+1];
			mult[i+1] = mult[i]*arr[i+1];
		}
		int count = n;
		for(int i = 1; i<n+1 ; i++){
			for(int j = i+1; j<n+1; j++){
				int adds = add[j] - add[i-1];
				int mults = mult[j]/mult[i-1];
				if(add==mults)count++;
			}
		}
		cout<<count<<endl;
	}	
	return 0;
}
