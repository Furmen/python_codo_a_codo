function convertImage() {
    var fileInput = $("[name=image]:visible")[0];

    var reader = new FileReader();
    reader.readAsDataURL(fileInput.files[0]);

    reader.onload = function() {
        let result = reader.result;
        $("#hdnImage").val(result);
        $("#imgPreview").attr("src", result);
        $("#imgPreviewContainer").fadeIn();
    };
}

function hideAlert() {
    setInterval(function() {
        if ($(".alert")) {
            setTimeout(function() {
                $(".alert").fadeOut();
            }, 3000);
        }
    }, 500);
}

hideAlert();