const arr = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];

for (var i = 1; i < arr.length; i++)
    for (var j = 0; j < i; j++)
        if (arr[i] > arr[j]) {
            var x = arr[i];
            arr[i] = arr[j];
            arr[j] = x;
        }

console.log(arr);