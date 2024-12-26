#include <bits/stdc++.h>
// clang-format off
#ifdef _MSC_VER
#if __has_include(<__msvc_int128.hpp>)
#include <__msvc_int128.hpp>
using i128=std::_Signed128;using u128=std::_Unsigned128;
#endif
#else
using i128=__int128_t;using u128=__uint128_t;
#endif
#define rep(i, s, e) for (auto i = (s); i <= (e); ++i)
#define per(i, e, s) for (auto i = (s); i >= (e); --i)
#define dop(i, s, e) for (auto i = (s); i >= (e); --i)
using namespace std;
using ll=int64_t;using ull=uint64_t;using PI=pair<int,int>;using PL=pair<ll,ll>;using PIL=pair<int,ll>;using PLI=
pair<ll,int>;using VI=vector<int>;using VL=vector<ll>;using VVI=vector<VI>;using VVL=vector<VL>;template<class T,
class U>void chkmin(T&a,U b){if(a>b)a=b;}template<class T,class U>void chkmax(T&a,U b){if(a<b)a=b;}
#if 1
char nc(){constexpr int NCBUF=1<<21;static char b[NCBUF],*x=b,*y=b;return x==y&&(y=(x=b)+fread(b,1,NCBUF,stdin),x==y
)?EOF:*x++;}template<class T>bool input(T&x){x=0;char c=nc();bool f=0;while(c<'0'||c>'9'){if(c==EOF)return 0;f=c=='-'
,c=nc();}while(c>='0'&&c<='9')x=x*10+(c^48),c=nc();if(f)x=-x;return 1;}bool input(char&x){for(;;){x=nc();if(x==EOF)
return 0;if(!isspace(x))return 1;}}template<int p=0>bool input(string&s){s.resize(p+1);if(!input(s.back()))return 0;
do s.push_back(nc());while(!(s.back()==EOF||isspace(s.back())));s.pop_back();return 1;}bool input(char*p){if(!input(
*p))return 0;do*++p=nc();while(!(*p==EOF||isspace(*p)));*p=0;return 1;}template<class T,class...S>bool input(T&x,S&
...y){return input(x)&&input(y...);}
#else
template<class...T>bool input(T&...x){return(bool)(cin>>...>>x);}
#endif
template<class T>T input(){T x;input(x);return x;}template<class...T>enable_if_t<1<sizeof...(T),tuple<T...>>input()
{return{input<T>()...};}template<class T,int N>auto input(){array<T,N>a;for(T&x:a)input(x);return a;}template<class
...T>void print(T...y){bool f=0;(((f?((cout<<' '),0):f=1),cout<<y),...);}template<class...T>void println(T...y){
print(y...);cout<<'\n';}
// clang-format on

// constexpr ll MOD = 998244353;
constexpr ll MOD = int(1e9) + 7;
constexpr auto INF = numeric_limits<ll>::max();

ll solve() {
    auto N = input<int>();
    VI a(N + 1);
    rep(i, 1, N) input(a[i]);

    return 0;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(0);
    for (auto T = input<int>(); T--;) {
        // solve();
        println(solve());
        // println(solve() ? "YES" : "NO");
    }
}
