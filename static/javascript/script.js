// var currentPage=location.href.substring(location.href.lastIndexOf("/"),-500); //example_output= http://127.0.0.1:8000/contact-us

// currentPage=currentPage.substring(currentPage.lastIndexOf('/'),500) //example_output= /contact-us
var currentPage=location.href.split("/")[3]
if(currentPage==""){
    document.getElementById("home").style.color="green";
}else if (currentPage=="about-us"){
    document.getElementById("about-us").style.color="green";
}else if (currentPage=="contact-us"){
    document.getElementById("contact-us").style.color="green";
}else if (currentPage=="FAQs"){
    document.getElementById("faqs").style.color="green";
}else if (currentPage=="talents"){
    document.getElementById("talents").style.color="green";
}