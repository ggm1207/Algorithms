// 예제코드만 실행시켜봄

class bugpower{
    constructor(arr,n,m){
        this.arr = arr;
        this.n = n;
        this.m = m;
        this.count = 0;
    }

    check(){
        var i, j;
        for(i=0; i<this.n; i++){
            for(j=0; j<this.m; j++){
                if(this.arr[i][j]===1){
                    // console.log(i, j);
                    var a = setTimeout(this.ext(i,j),1000);
                }
            }
        }
        return this.count
    }
    async ext(i,j){
        if(i >= this.n || i < 0 || j >= this.m || j < 0){
            return;
        }
        if(this.arr[i][j]==1){
            console.log(i,j)
            this.arr[i][j] = 0;
            this.count = this.count + 1;
            await this.ext(i+1,j);
            await this.ext(i-1,j);
            await this.ext(i,j+1);
            await this.ext(i,j-1);
        } else {
            return;
        }
    }

    async show(){
        await this.check()
        console.log(this.count)
    }
}

function make_arr(n,m){
    var arr;
    var arrs = [];
    var i,j;
    for(i=0; i<n; i++){
        arr = [];
        for(j=0; j<m; j++){
            arr.push(0);
        }
        arrs.push(arr);
    }
    return arrs;
}

var arr = make_arr(4,5)
arr[0][0] = 1;
arr[0][1] = 1;
arr[2][2] = 1;
arr[3][3] = 1;
console.log(arr);
// console.log(arr[1][3]);
let a = new bugpower(arr,4,5);
// a.check()
a.show()
