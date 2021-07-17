function convertImage() {
    var fileInput = $("[name=image]:visible")[0];

    var reader = new FileReader();
    reader.readAsDataURL(fileInput.files[0]);

    reader.onload = function() {
        let result = reader.result;
        $("[id=hdnImage]:visible").val(result);
        $("[id=imgPreview]:visible").attr("src", result);
        $("[id=imgPreviewContainer]:visible").fadeIn();
    };
}

function hideAlert() {
    setTimeout(function() {
        $(".alert").fadeOut();
    }, 3000);
}