#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int n;
vector<int> arr;
vector<vector<int>> blocks;
int blk_sz; 

void update(int idx, int val) {
    int old_val = arr[idx];
    int b_idx = idx / blk_sz;
    
    arr[idx] = val;
    
    auto it = lower_bound(blocks[b_idx].begin(), blocks[b_idx].end(), old_val);
    blocks[b_idx].erase(it);
    
    auto pos = lower_bound(blocks[b_idx].begin(), blocks[b_idx].end(), val);
    blocks[b_idx].insert(pos, val);
}

int query(int l, int r, int c) {
    int count = 0;
    int lb = l / blk_sz;
    int rb = r / blk_sz;
    
    if (lb == rb) {
        for (int i = l; i <= r; ++i) {
            if (arr[i] >= c) count++;
        }
    } else {
        for (int i = l; i < (lb + 1) * blk_sz; ++i) {
            if (arr[i] >= c) count++;
        }
        
        for (int i = lb + 1; i < rb; ++i) {
            count += blocks[i].end() - lower_bound(blocks[i].begin(), blocks[i].end(), c);
        }
        
        for (int i = rb * blk_sz; i <= r; ++i) {
            if (arr[i] >= c) count++;
        }
    }
    return count;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    if (!(cin >> n)) return 0;
    
    arr.resize(n);
    blk_sz = sqrt(n);

    
    blocks.resize((n + blk_sz - 1) / blk_sz);
    
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        blocks[i / blk_sz].push_back(arr[i]);
    }
    
    for (int i = 0; i < blocks.size(); ++i) {
        sort(blocks[i].begin(), blocks[i].end());
    }
    
    int q;
    cin >> q;
    
    while (q--) {
        int type;
        cin >> type;
        if (type == 0) {
            int a, b, c;
            cin >> a >> b >> c;
            cout << query(a - 1, b - 1, c) << "\n";
        } else {
            int a, b;
            cin >> a >> b;
            update(a - 1, b);
        }
    }
    
    return 0;
}