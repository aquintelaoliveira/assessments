Write a function: class Solution { public int solution(int[] A); } that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].


```c#
using System;

class Solution {
    public int solution(int[] A) {
        // write your code in C# 6.0 with .NET 4.5 (Mono)
        var arr = A.Where(e => e > 0).ToArray();
        Array.Sort(arr);

        if (arr.Length == 0) return 1;

        for (var i = 1; i < arr.Length; i++) {
            if (arr[i] > arr[i - 1] + 1) return arr[i - 1] + 1;
        }
        
        return arr[arr.Length - 1] + 1;
    }

}
```

```javascript
function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    var sa = A.sort();
    var spa = sa.filter(e => { return e > 0 });
    
    if (spa.length === 0) return 1

    for (let i = 1; i < spa.length; i++) {
        if (spa[i] > spa[i - 1] + 1) return spa[i - 1] + 1;
    }

    return spa[spa.length - 1] + 1;
}
```