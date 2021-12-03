$(function () {
    var nickname = localStorage.getItem("nickname");
    if (nickname) {
        $("input[name=author]").val(nickname);
    }

    if (window.location.hash) {
        showAllInlineComments();
    }

    $("#comments-form").submit(function() {
        $("#comments-form input[type=submit]").attr("disabled", "disabled");
    });

    $(".inline-comments input, .inline-comments textarea").on("focus", function() {
        $(this).parents(".inline-comments-form").addClass("inline-comments-form_is_visible");
    });

    $("a[href^='http']").each(function() {
        if (this.getAttribute("href").indexOf("://" + document.domain) === -1) {
            $(this).attr("target", "_blank");
        }
    });

    $(".inline-comments-form__author").each(function() {
        $(this).attr("size", $(this).val().length + 1);
    }).bind("change", function () {
        $(this).attr("size", $(this).val().length + 1);
    });

    $("input[name=author]").bind("keyup", function () {
        var newAuthor = $(this).val();
        $("input[name=author]").val(newAuthor).attr("size", newAuthor.length + 1);
        localStorage.setItem("nickname", newAuthor);
    });

    $(".inline-comments-form__text > textarea").bind("keyup", function(e) {
        if ((e.ctrlKey || e.metaKey) && (e.keyCode == 13 || e.which == 13 || e.keyCode == 10 || e.which == 10)) {
           return ajax_inline_comment_with_form(this.form);
        }

        this.style.height = "auto";
        if (this.scrollHeight > 20) {
            this.style.height = (this.scrollHeight)+"px";
        }

        $(this.form).addClass("inline-comments-form__submit_active");
    });

    $(".menu-item__search").bind("click", function(e) {
        $(".menu-search").show();
        $(".menu-search input[type=text]").focus();
    });

    $(".header").bind("click", function(e) {
        if ($(event.target).hasClass("menu")) {
            $(".menu-search").hide();
        }
    });

    $(".block-spoiler").click(function() {
        $(this).find(".block-spoiler-text").toggle();
        $(this).find(".block-spoiler-button").toggle();
    });
});

function nick(nick, target) {
    var cursorPosition = $(target).prop("selectionStart");
    var currentText = $(target).val();
    var textBefore = currentText.substring(0, cursorPosition);
    var textAfter  = currentText.substring(cursorPosition, currentText.length);
    $(target).val(textBefore + "**" + nick + "**, " + textAfter).focus();
}

var is_ajax_in_progress = false;
function ajax_inline_comment(event) {
    return ajax_inline_comment_with_form(event.target);
}

function ajax_inline_comment_with_form(form) {
    var $form = $(form);
    var $error = $form.find(".inline-comments-form__error");
    $error.html("");

    var $text = $form.find(".inline-comments-form__text > textarea");
    if ($text.val().length < 1) {
        $error.html("Надо написать комментарий перед отправкой. Да, такие вот у нас жестокие правила.").show();
        return false;
    }

    if (is_ajax_in_progress) {
        $error.html("Отправка еще в процессе. Если кажется всё сломалось, скопируйте свой комментарий и обновите страницу. Сорян :(").show();
        return false;
    }

    is_ajax_in_progress = true;
    $.ajax({
        type: $form.attr("method"),
        url: $form.attr("action"),
        data: $form.serialize(),
        success: function (data) {
            is_ajax_in_progress = false;
            $error.html("").hide();
            if (data.status == "success") {
                $text.val("");
                $form.before(
                    '<div class="inline-comment">' +
                        '<span class="inline-comment__text">' +
                            '<span class="inline-comment__author">' +
                                data.comment.author +
                            '</span> ' + data.comment.text +
                        '</span>' +
                    '</div>'
                );
            } else {
                $error.html("Ошибка: " + data.reason).show();
                console.error(data);
            }
        },
        error: function (data) {
            is_ajax_in_progress = false;
            $error.html("Что-то пошло не так. Скопируйте свой комментарий чтобы не " +
                "потерять и обновите страницу. Вполне вероятно, что он уже запостился, но если нет — попробуйте еще раз " +
                "и напишите мне в личку. Сорян :(").show();
            console.error(data);
        }
    });
    return false;
}

function ajax_click(event) {
    var form = $(event.target);
    $.ajax({
        type: form.attr("method"),
        url: form.attr("action"),
        data: form.serialize(),
        success: function (data) {
            if (data.status === "success") {
                form.find(".count-updater").html(data.click.total);
                form.parent(".clicker-updater").addClass("status_voted");
            } else {
                form.parent(".clicker-updater").addClass("status_error");
                form.find(".count-updater").html("x");
                alert("Error: " + data.reason);
            }
        },
        error: function (data) {
            form.find(".count-updater").html("x");
            form.parent(".clicker-updater").addClass("status_error");
        }
    });
    return false;
}

function goal(name) {
    try {
        yaCounter1670427.reachGoal(name);
    } catch (err) {
        console.error("YaMetrika is blocked :(", err);
    }
    return true;
}

function toggleInlineCommentsBlock(block) {
    var $block = $('#block-' + block);
    var $comments = $block.find(".inline-comments");
    if ($comments.is(':visible')) {
        $comments.hide();
        $block.find(".inline-comments-placeholder__hideall").show();
        $block.find(".inline-comments-placeholder__showall").hide();
    } else {
        $comments.show();
        $block.find(".inline-comments-placeholder__hideall").hide();
        $block.find(".inline-comments-placeholder__showall").show();
    }
    $comments.scrollTop($comments[0].scrollHeight);
    return false;
}

function showAllInlineComments() {
    $(".inline-comments").show();
    $(".inline-comments-placeholder__showall").hide();
    localStorage.setItem("isInlineCommentsShown", "true");

    $(".inline-comments").each(function() {
       $(this).scrollTop($(this)[0].scrollHeight);
    });
    return true;
}

function hideAllInlineComments() {
    $(".inline-comments").hide();
    $(".inline-comments-placeholder__hideall").hide();
    localStorage.setItem("isInlineCommentsShown", "false");
    return true;
}
