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

// Scroll to the section when the user clicks the link
function gotoByScroll(id) {
    let element = document.getElementById(id);
    element.scrollIntoView({behavior: "smooth"});
}

// Get the modal
modal = document.getElementById("message-modal");
closeModal = document.getElementById("modal-close");

// Close the modal when the user clicks close
closeModal.onclick = function() {
    modal.close();
}

// Close the modal if the user clicks outside
window.addEventListener('click', function(event) {
    if (event.target == modal) {
        modal.close();
    }
});

// Process the form submission and prevent default behaviour
form = document.getElementById("contact-form")
form.addEventListener("submit", function(event) {
    event.preventDefault();
    const formData = new FormData(form);
    fetch('/submit', {
        method: 'POST',
        body: formData
    }).then(function(response) {
        if (response.ok) {
            form.reset();
            modal.showModal();
        }
    });
})