document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("upload-form");

    form.addEventListener("submit", function (e) {
        const csvFile = document.getElementById("data_file").files[0];
        const jsonFile = document.getElementById("json_file").files[0];

        if (!csvFile || !jsonFile) {
            alert("Please select both a CSV file and a JSON file.");
            e.preventDefault();
        }
    });
});
