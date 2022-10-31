const participantNums = [[1, 3, 2, 2, 1],
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

participantNums.forEach(
    (nums) => {
        max_num = Math.max.apply(null,nums)

        let a_count = []

        for (let i = 0; i < max_num + 1; i++) {
            a_count.push(0)
        }

        for (let num of nums) {
            a_count[num]+=1
        }

        for (let count in a_count){
            if (a_count[count] % 2==1){
                console.log(count)
            }
        }

    }
)


// 3
// 100
// 62


// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2
