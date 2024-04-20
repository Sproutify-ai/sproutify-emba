$(document).ready(function () {
  console.log("document is ready");
  $(".card-header").click(function () {
    console.log("clicked");
    $(this).next(".card-content").slideToggle();

    // toggle the chevron
    var chevron = $(this).find(".content-chevron");
    if (chevron.hasClass("fa-angle-down")) {
      chevron.removeClass("fa-angle-down");
      chevron.addClass("fa-angle-up");
    } else {
      chevron.removeClass("fa-angle-up");
      chevron.addClass("fa-angle-down");
    }
  });
});