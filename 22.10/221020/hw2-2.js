s = ''

for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 9; j++) {
        if (4- i <= j && j <= 4 + i){
            s+='*'
        }
        else{
            s+=' '
        }
    }
    s+='\n'
}
s=s.trimEnd()
console.log(s);