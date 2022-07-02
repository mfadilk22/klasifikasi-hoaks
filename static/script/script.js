// import swal from 'sweetalert';

// el2.style.display = "none";
let r1 = document.getElementById('radio-1');
let r2 = document.getElementById('radio-2');

let el1 = document.getElementById('klasifikasi-teks');
let el2 = document.getElementById('upload-file');

// const radioButtons = document.querySelectorAll('input[name="radio"]');
// for(const radioButton of radioButtons){
//     radioButton.addEventListener('change', showSelected);
// }

// function showSelected(e) {
//     console.log(e);
//     if (this.checked) {
//         el2.style.display = 'flex';
//     }
// }

function toggle(){    
    if (r1.checked){
        el1.style.display = 'flex';
        el2.style.display = 'none';
    }
    else{
        el1.style.display = 'none';
        el2.style.display = 'flex';
    }
}

// r1.addEventListener ( "click", function(){
//     el1.style.display = 'flex';
//     el2.style.display = 'none';
// });

// r2.addEventListener( "click", function() {
//     el1.style.display = 'none';
//     el2.style.display = 'flex';
// });



let submit_btn = document.querySelectorAll("button");
let txtarea = document.querySelector("textarea");
let submit_btn_value = submit_btn.value;

if (submit_btn_value === "checked"){
    el1.style.display = 'none';
    el2.style.display = 'flex';
}

txtarea.addEventListener('keyup', function() {
    submit_btn[0].disabled = !this.value;
  });

var fileInput = document.querySelector(".file");
var the_return = document.querySelector(".doc-name");
var button = document.querySelector(".input-file-trigger");
let closebtn = document.querySelector(".close");
let filename = document.querySelector(".filename");
let submit_file_btn = document.getElementById("upload-file").getElementsByClassName("submit")[0];
let hoaks_file = document.getElementById("myStrong");
let input = document.getElementById("input");

// input.onchange = () => {
//     submit_btn[1].disabled = !this.value;
// }

filename.style.display = 'flex';
// function checkFile(form_2){   
//     var fileVal = form_2.elements['file'].value;

//     if (fileVal == ""){
//         // submit_btn[0].disabled = !this.value;
//         swal ("Oops", "File tidak boleh kosong","error" );
        
//     }else{
//         form_2.submit();
//     }
// }

button.addEventListener( "click", function() {
    fileInput.focus();
    return false;
});

// submit_file_btn.addEventListener( "click", function() {
//     r2.checked=true;
//     return false;
// });

fileInput.addEventListener( "change", function() {  
    submit_btn[1].disabled = false;
    filename.style.display = 'flex'
    the_return.innerHTML = this.files[0].name;  
});

closebtn.addEventListener("click", function() {
    filename.style.display = 'none';
});



// submit_file_btn.addEventListener("click", function() {
//     el2.style.display = 'none';
// });

