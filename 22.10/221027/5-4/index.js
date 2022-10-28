/* 
  아래에 코드를 작성해주세요.
*/
const inputTag=document.querySelector('.search-box__input')

const buttonTag=document.querySelector('.search-box__button')
buttonTag.addEventListener('click',fetchAlbums)

const result=document.querySelector('.search-result')

function fetchAlbums (event) {
  event.preventDefault()
  const keyword = inputTag.value
  
  const page=1
  const limit = 10

  const api_url=`http://ws.audioscrobbler.com/2.0/?method=album.search&album=${keyword}&api_key=914d24165d1f5e8936e9d65f11aa89fb&format=json`



  axios({
    method:'get',
    url: api_url,
    page:page,
    limit:limit,
  })
  .then(function(response){
    albums=response.data.results.albummatches.album
    result.innerHTML=''

    console.log(albums);

    for(let i=0;i<albums.length;i++){
      const card=document.createElement('div')
      card.classList.add('search-result__card')
  
      const cardImg = document.createElement('img')
      cardImg.src=albums[i].image[1]['#text']
  
      card.append(cardImg)
  
      const cardText=document.createElement('div')
      cardText.classList.add('search-result__text')
  
      const name=document.createElement('h2')
      name.innerText=albums[i].artist
      const albumName=document.createElement('p')
      albumName.innerText=albums[i].name
  
      cardText.appendChild(name)
      cardText.appendChild(albumName)
      card.appendChild(cardImg)
      card.appendChild(cardText)
  
      result.appendChild(card)
  
    }
  }
  )
  .catch((error)=>{
    alert('잠시 후 다시 시도해주세요')
  })

}
