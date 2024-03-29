const navlinks = document.querySelectorAll(".nav-link");
const brand = document.querySelector(".navbar-brand");
const navlink_signup=document.querySelector("#nav-link-signup");
var navbarfeather = document.querySelector("#navbar-feather-container");

if (navlinks) {
    for (navlink of navlinks){
        if (navlink) {
            navlink.addEventListener("mouseenter",function (event) {
                this.classList.toggle('hovered-link')
            });
            
            navlink.addEventListener("mouseleave",function (event) {
                this.classList.toggle('hovered-link');
            });
        }
    }
}

if (navlink_signup){
    navlink_signup.addEventListener('click',function (event) {
        console.log(event);
        navlink.load(location.href+' #login-form');
    })
}

if (brand) {
    brand.addEventListener("mouseenter",function (event) {
        navbarfeather.classList.toggle('hovered')
    });
    
    brand.addEventListener("mouseleave",function (event) {
        setTimeout(function(){
            navbarfeather.classList.toggle('hovered');
         }.bind(navbarfeather),1000)
    });
}
