function palindrome(str) {
    let flag = 0
    for (let i = 0; i < parseInt(str.length / 2); i++) {
        if (str[i] != str[str.length - i - 1]) {
            flag = 1
        }
    }
    if (flag == 1) {
        console.log('false')
    }
    else {
        console.log('true')
    }
}
  
  // 출력
  // palindrome('level') => true
  // palindrome('hi') => false
