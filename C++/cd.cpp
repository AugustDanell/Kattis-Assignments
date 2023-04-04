#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    while(true){
        unordered_map<long, long> umap;
        long N, M;
        
        scanf("%ld %ld", &N, &M);
        if(N == 0 && M == 0){
            break;
        }
        else{
            long a;
            for(long i = 0; i < N; i++){
                scanf("%ld", &a);
                umap[a] = 1;
            }
            
            long b;
            long count = 0;
            for(long i = 0; i < M; i++){
                scanf("%ld", &b);
                if(!(umap.find(b) == umap.end())){
                    count ++;
                }
            }
            cout << count << endl;
        }
    }
    return 0;
}
