function convertImage() {
    var fileInput = $("[name=image]:visible")[0];

    var reader = new FileReader();
    reader.readAsDataURL(fileInput.files[0]);

    reader.onload = function() {
        let result = reader.result;
        if ($("#frmNewStudent").is(":visible")) {
            $("#hdnImageNew").val(result);
            $("#imgPreviewNew").attr("src", result);
            $("#imgPreviewContainerNew").fadeIn();
        } else {
            $("[name=hdnImageEdit]").val(result);
            $("[name=imgPreviewEdit]").attr("src", result);
        }
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