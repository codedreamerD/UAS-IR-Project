document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const queryInput = document.querySelector("#query");

    form.addEventListener("submit", function(event) {
        if (queryInput.value.trim() === "") {
            event.preventDefault();
            alert("Harap masukkan query sebelum mencari!");
        }
    });
});
