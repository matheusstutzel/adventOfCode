
var readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

// binary tree :eyes: 
class N {
    one = undefined
    zero = undefined
    count = 0
    v = undefined
    constructor(v) {
        this.v = v
    }

    push(p) {
        this.count++
        if (!p)
            return

        this.one = this.one || new N(1)
        this.zero = this.zero || new N(0)
        if (p[0] == 1)
            this.one.push(p.slice(1))
        else
            this.zero.push(p.slice(1))

    }
}


//root
var x = new N()

rl.on('line', function (line) {
    x.push(line)

})
rl.on('close', () => { process(x) })



process = (root) => {
    let [o, q] = solve(root, 1)
    let [c, w] = solve(root, 0)
    console.log(o * c)
}

solve = (x, m) => {
    if (!x.one) {
        //leaf
        return [x.v, 1]
    }

    var choose
    if (x.count == 1) {
        choose = x.one.count ? x.one : x.zero
    } else {
        a = x.count / 2 <= x.one.count ? x.one : x.zero
        b = x.count / 2 <= x.one.count ? x.zero : x.one

        choose = m ? a : b
    }
    [acc, pow] = solve(choose, m)
    pow *= 2
    return [(acc + ((x.v || 0) * pow)), pow]
}