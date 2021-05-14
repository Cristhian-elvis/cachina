const arrLabel = document.querySelectorAll(".label-issuing");
arrLabel.forEach((label) => {
    label.addEventListener("blur", (e) => {
        if (e.target.value.length > 0) {
            label.setAttribute("badinput", "true");
        } else {
            label.setAttribute("badinput", "false");
        }
    });
});

/*
text_input.addEventListener("blur", (e) => {
    if (e.target.value.length > 0) {
        text_input.setAttribute("badinput", "true");
    } else {
        text_input.setAttribute("badinput", "false");
    }
});*/
