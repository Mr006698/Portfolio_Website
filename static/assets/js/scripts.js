/*!
* Start Bootstrap - Resume v7.0.6 (https://startbootstrap.com/theme/resume)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-resume/blob/master/LICENSE)
*/
//
// Scripts
// 

// Toggle the menu when the user clicks the button
function openMenu() {
    menu = document.getElementById("menuDropdown");
    height = menu.offsetHeight;
    if (height == 0) {
        menu.style.height = "200px"; // This will need adjusting if menu items added.
    }
    else {
        menu.style.height = "0px";
    }
}

// Close the dropdown if the user clicks outside of it
window.addEventListener('click', function(event) {
    if (!event.target.matches(".material-symbols-rounded")) {
        var menu = document.getElementById("menuDropdown");
        menu.style.padding = "0em 0em 0em 0em";
        menu.style.height = "0px";
    }
})

// Activate menu link on scroll
let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('li a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 250;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('li a[href*=' + id + ']').classList.add('active');
            });
        };
    })
};

// Get the modal
modal = document.getElementById("message-modal");
closeModal = document.getElementById("modal-close");

// window.setTimeout(() => {
//     modal.showModal();
// }, 1000);

// Close the modal when the user clicks close
closeModal.onclick = function() {
    // modal.style.display = "none";
    modal.close();
}

// Close the modal if the user clicks outside
window.addEventListener('click', function(event) {
    if (event.target == modal) {
        // modal.style.display = "none";
        modal.close();
    }
});