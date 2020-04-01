function open_home_content() {
    document.getElementById("about_content").style.display = "none";
    document.getElementById("contact_content").style.display = "none";
    document.getElementById("home_content").style.display = "block";
}

function open_about_content() {
    document.getElementById("home_content").style.display = "none";
    document.getElementById("contact_content").style.display = "none";
    document.getElementById("about_content").style.display = "block";
}

function open_contact_content() {
    document.getElementById("home_content").style.display = "none";
    document.getElementById("about_content").style.display = "none";
    document.getElementById("contact_content").style.display = "block";
}