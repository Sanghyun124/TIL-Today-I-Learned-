let board=[0,0,0,0,0,0,0,0,0,0]
let answer=0
function promising(cdx) {
    for (let i = 0; i < cdx; i++) {
        if (board[cdx] == board[i] || cdx - i == Math.abs(board[cdx] - board[i])) {
            return 0;
        }
    }
    return 1;
}


function nqueen(cdx,n) {
	if (cdx == n) {
        answer++
		return;
	}

	for (let i = 0; i < n; i++) {
		board[cdx] = i;	
		if (promising(cdx)) {
			nqueen(cdx + 1,n);
		}
	}
}

function findQueens(n) {
    nqueen(0,n)
    
    return answer
}

console.log(findQueens(4)) // 2
