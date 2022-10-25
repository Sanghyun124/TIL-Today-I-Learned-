// 코드를 작성해 주세요
const s_btn = document.querySelector('#scissors-button')
const r_btn = document.querySelector('#rock-button')
const p_btn = document.querySelector('#paper-button')
const sectionTag = document.querySelector('section')
const countA = document.querySelector('.countA')
const countB = document.querySelector('.countB')
const p1_img = document.querySelector('#player1-img')
const modalTag = document.querySelector('.modal')
const modalcontentTag = document.querySelector('.modal-content')

let p1_win=0
let p2_win=0

s_btn.setAttribute('value', 'scissors')
r_btn.setAttribute('value', 'rock')
p_btn.setAttribute('value', 'paper')

const playGame = (p1_choice, p2_choice) => {
    if (p1_choice == p2_choice) {
        return 0
    }
    else if ((p1_choice == 'rock' && p2_choice == 'scissors') || (p1_choice == 'scissors' && p2_choice == 'paper') || (p1_choice == 'paper' && p2_choice == 'rock')) {
        return 1
    }

    else if ((p2_choice == 'rock' && p1_choice == 'scissors') || (p2_choice == 'scissors' && p1_choice == 'paper') || (p2_choice == 'paper' && p1_choice == 'rock')) {
        return 2
    }
}

function game(event) {
    s_btn.setAttribute('disabled', true)
    r_btn.setAttribute('disabled', true)
    p_btn.setAttribute('disabled', true)

    const p1_value = this.value
    
    let p1_img = document.querySelector('#player1-img')
    let p2_img = document.querySelector('#player2-img')
    p1_img.setAttribute('src', event.target.getAttribute('src'))

    const cases = [s_btn, r_btn, p_btn]
    let count = 0
    const pick = setInterval(function () {
        p2_img.setAttribute('src', cases[count % 3].firstElementChild.getAttribute('src'))
        count++
    }, 100)
    setTimeout(function () {
        clearInterval(pick)
        const p2_pick = cases[parseInt(Math.random() * 10) % 3]
        const p2_value = p2_pick.value
        p2_img.setAttribute('src', p2_pick.firstElementChild.getAttribute('src'))


        const result = playGame(p1_value, p2_value)
        modalTag.style.display='flex'
        if (result === 0) {
            modalcontentTag.innerText = '무승부입니다'
        }
        else if (result === 1) {
            modalcontentTag.innerText = 'Player1의 승리입니다'
            p1_win+=1
            countA.innerText=p1_win
        }
        else {
            modalcontentTag.innerText = 'Player2의 승리입니다'
            p2_win+=1
            countB.innerText=p2_win
        }

        modalTag.addEventListener('click',function(){
            modalTag.style.display='none'
        })

        s_btn.disabled=false
        r_btn.disabled=false
        p_btn.disabled=false

    }, 3000);

}

s_btn.addEventListener('click', game)
r_btn.addEventListener('click', game)
p_btn.addEventListener('click', game)

// //정해진 시간마다 주어진 콜백함수를 실행
// // setInterval(function(){},time(ms))
// const timer = setInterval(function () { }, 100)
// //정해진 시간 후에 콜백함수를 한번 실행
// // setTimeout(function(){},time(ms))
// setTimeout(() => { }, 3000);
// //반복을 멈추고 싶으면
// clearInterval(timer)