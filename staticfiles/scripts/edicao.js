$(document).ready(function () {
    $('input[required]').next('label').append('<span> *</span>');

    $('.summernote.editavel').summernote({
        toolbar: [
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['font', ['strikethrough', 'superscript', 'subscript']],
            ['fontsize', ['fontsize']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['height', ['height']]
        ],
        height: 300
    });

    $('.summernote.listagem').summernote({
        disableDragAndDrop: true,
        airMode: true
    });

    $('.summernote.listagem').summernote('disable');

    // verificação de caracteres válidos
    $('.decimal').keypress(function (event) {
        if (event.which !== 8 && event.which !== 0 && event.which < 48 || event.which > 57) {
            event.preventDefault();
        }
    });

    $('.data').keypress(function (event) {
        if ((event.which < 48 || event.which > 57) && event.which !== 47 && event.which !== 45 && event.which !== 46) {
            event.preventDefault();
        }
    });

    $('.cpf_cnpj').keypress(function (event) {
        var tecla = event.which;
        if (tecla != 8 && tecla != 0 && tecla != 45 && tecla != 47 && (tecla < 48 || tecla > 57)) {
            event.preventDefault();
        }
    });

    $('.cep').keypress(function (event) {
        var tecla = event.which;
        if (tecla != 45 && (tecla < 48 || tecla > 57)) {
            event.preventDefault();
        }
    });

    // formatadores
    $('.decimal').blur(function () {
        if ($(this).val() == '') {
            return
        }
        var valor = parseFloat($(this).val()).toLocaleString('pt-BR', { minimumFractionDigits: 2 });
        $(this).val(valor);
    });

    $('.data').blur(function () {
        var valor = $(this).val();
        var data = moment(valor, ['DD/MM/YYYY', 'D/M/YYYY', 'DDMMYYYY', 'DD.MM.YYYY', 'DD-MM-YYYY'], true);
        if (data.isValid()) {
            $(this).val(data.format('DD/MM/YYYY'));
        } else {
            $(this).val('');
        }
    });

    $(".cpf_cnpj").blur(function () {
        var value = $(this).val();
        value = value.replace(/[^0-9]/g, "");
        if (value == '') {
            return
        }
        var length = value.length;
        var formatted_value = "";

        if (length == 11) {
            formatted_value = value.replace(/(\d{3})(\d{3})(\d{3})/, "$1.$2.$3-");
        }
        else if (length == 14) {
            formatted_value = value.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, "$1.$2.$3/$4-$5");
        }
        else {
            $(this).val("");
        }
    });

    $(".cep").blur(function () {
        var cep = $(this).val().replace(/\D/g, '');

        if (cep != "") {
            var validacep = /^[0-9]{8}$/;
            if (validacep.test(cep)) {
                $("#rua").val("...");
                $("#bairro").val("...");
                $("#cidade").val("...");
                $("#uf").val("...");
                $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function (dados) {
                    if (!("erro" in dados)) {
                        $("#rua").val(dados.logradouro);
                        $("#bairro").val(dados.bairro);
                        $("#cidade").val(dados.localidade);
                        $("#uf").val(dados.uf);
                    }
                    else {
                        $("#rua").val("");
                        $("#bairro").val("");
                        $("#cidade").val("");
                        $("#uf").val("");
                        alert("CEP não encontrado.");
                    }
                });
            }
            else {
                $("#rua").val("");
                $("#bairro").val("");
                $("#cidade").val("");
                $("#uf").val("");
                alert("Formato de CEP inválido.");
            }
        }
        else {
            $("#rua").val("");
            $("#bairro").val("");
            $("#cidade").val("");
            $("#uf").val("");
        }
    });
});

function DefinirCampoComoObrigatorio(campo) {
    campo.next('label').append('<span> *</span>')
}

function DefinirCampoComoOpcional(campo) {
    campo.removeAttr('required');
    campo.next('label').find('span').remove();
}

