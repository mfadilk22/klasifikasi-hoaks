function toggle(){
    let r1 = document.getElementById('radio-1');
    let r2 = document.getElementById('radio-2');

    let el1 = document.getElementById('klasifikasi-teks');
    let el2 = document.getElementById('upload-file');

    el2.style.display = "none";

    if (r1.checked){
        el1.style.display = 'flex';
        el2.style.display = 'none';
        console.log( el1.style.display);
        console.log( el2.style.display);
    }
    else{
        el1.style.display = 'none';
        el2.style.display = 'flex';
        console.log( el1.style.display);
        console.log( el2.style.display);
    }
}

let submit_btn = document.querySelectorAll("button");
let txtarea = document.querySelector("textarea");

txtarea.addEventListener('keyup', function() {
    submit_btn[0].disabled = !this.value;
  });

var fileInput = document.querySelector(".file");
var the_return = document.querySelector(".doc-name");
var button = document.querySelector(".input-file-trigger");
let closebtn = document.querySelector(".close");
let filename = document.querySelector(".filename");

filename.style.display = 'none';

button.addEventListener( "click", function() {
    fileInput.focus();
    return false;
 });

fileInput.addEventListener( "change", function() {  
    filename.style.display = 'flex'
    the_return.innerHTML = this.files[0].name;  
});

closebtn.addEventListener("click", function() {
    filename.style.display = 'none';
});

