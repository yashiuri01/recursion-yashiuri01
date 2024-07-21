
class SpeechWallpaper {
  constructor (word, color, wallpaper, vt, hn) {
    this.word = word;
    this.color = color;
    this.wallpaper = wallpaper;
    this.vt = vt;
    this.hn = hn;
  }
}

function createSpeechWallpaper(speechObject){
  // innerFlex
  //  speechCard
  //    wordDiv
  //      wordH3

  //壁紙全体の定義
  let innerFlex = document.createElement("div");
  innerFlex.classList.add("d-flex", "align-items-center", "justify-content-center");

  //壁外単体の定義
  let speechCard = document.createElement("div");
  speechCard.classList.add("vh-75", "col-md-7", "col-10", "m-1", "d-flex", "justify-content-end", "profile-card");
  //vh-75 p-md-5 p-3 my-5 col-md-8 col-12 d-flex imgBackground justify-content-end align-items-start

  // 背景画像
  speechCard.style.backgroundImage = `url(${speechObject.wallpaper})`;
  speechCard.style.backgroundSize = 'cover';
  speechCard.style.backgroundRepeat = 'no-repeat';

  //文字配置
  switch (speechObject.vt) {
    case 'top': speechCard.classList.add("align-top"); break;
    case 'middle': speechCard.classList.add("align-middle"); break;
    case 'bottom': speechCard.classList.add("align-bottom"); break;
  }
  switch (speechObject.hn) {
    case 'left': speechCard.classList.add("align-items-start");  break;
    case 'center': speechCard.classList.add("align-items-center");  break;
    case 'right': speechCard.classList.add("align-items-end");  break;
  }
  innerFlex.append(speechCard);

  //add speech
  let wordDiv = document.createElement("div");
  wordDiv.classList.add("d-flex", "h-100", "align-items-center");
  wordDiv.style.color = `#${speechObject.color}`;

  let wordP = document.createElement("p");
  wordP.innerHTML = speechObject.word;
  wordDiv.append(wordP);

  speechCard.append(wordDiv);

  return innerFlex;
}

let speechesContainer = document.getElementById("speeches");
let speech1 = new SpeechWallpaper(
  "Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away. - Antoine de Saint",
  "1B4F72",
  "https://cdn.pixabay.com/photo/2020/06/12/03/06/magnifying-glass-5288877__340.jpg",
  "top",
  "right"
);
//let speeches = [speech1];

// Speechの表示
speechesContainer.append(createSpeechWallpaper(speech1));
//speeches.map(speech => speechesContainer.append(createSpeechWallpaper(speech)));