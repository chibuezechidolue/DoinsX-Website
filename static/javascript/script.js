
var slideLeft = {
    distance: '100%',
    origin: 'up',
    opacity: null,
    duration: '2500',
    delay:100,
    reset: true,
};

var slideUp = {
    distance: '100%',
    origin: 'down',
    opacity: null,
    duration: '2500',
    delay:100,
    reset: true,
};

// let img1=document.querySelector('.reveal1')
// ScrollReveal().reveal('.reveal2', slideLeft);
// ScrollReveal().reveal('.reveal3', slideLeft);



// Scroll reveal
const sr = ScrollReveal({
    origin: 'top',
    distance: '40px',
    duration: '2500',
    reset: true
  })
  
  
  // sr.reveal ('.about-container',{beforeReset: function(){sr.sync()},delay:100});
  // sr.reveal ('.product-top',{beforeReset: function(){sr.sync()},delay:200});
  // sr.reveal ('.carousel-inner',{beforeReset: function(){sr.sync()},delay:100});
  // sr.reveal ('.promotion-image',{beforeReset: function(){sr.sync()},delay:100});
  // sr.reveal ('.main-advert',{beforeReset: function(){sr.sync()},delay:100});


  sr.reveal('.reveal1',{delay:100});
  sr.reveal('.reveal3', {delay:100});
  
//   window.addEventListener('load', function() {
//   sr.reveal ('.reveal1',{delay:100});
//   })


// var currentPage=location.href.substring(location.href.lastIndexOf("/"),-500); //example_output= http://127.0.0.1:8000/contact-us

// currentPage=currentPage.substring(currentPage.lastIndexOf('/'),500) //example_output= /contact-us
var currentPage=location.href.split("/")[3]
if(currentPage==""){
    document.getElementById("home").style.color="#230dcc";
}else if (currentPage=="about-us"){
    document.getElementById("about-us").style.color="#230dcc";
}else if (currentPage=="contact-us"){
    document.getElementById("contact-us").style.color="#230dcc";
}else if (currentPage=="FAQs"){
    document.getElementById("faqs").style.color="#230dcc";
}else if (currentPage=="talents"){
    document.getElementById("talents").style.color="#230dcc";
}


// image change //

var imgs=document.querySelectorAll(".imgChange");

imgs.forEach(img => {
    img.addEventListener("click",()=>{
        let imgSrc= img.getAttribute('src')
        document.querySelector(".showImg").setAttribute('src',imgSrc);
    })
});









// Pulse animation button

let anims = [...document.querySelectorAll("[anim]")];
console.log(anims);
let click = (el, cb) => el.addEventListener("click", cb);
let toggle = (el) => el.classList.toggle("toggled");
let clickTog = (el) => click(el, () => toggle(el));
anims.map(clickTog);