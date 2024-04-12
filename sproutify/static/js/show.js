$(document).ready(function () {
  console.log("document is ready");
  $(".message-header").click(function () {
    console.log("clicked");
    $(this).next(".message-body").slideToggle();
  });

  $(".tabs ul li").click(function () {
    console.log("clicked");

    // set all tabs to inactive
    $(".tabs ul li").removeClass("is-active");

    // set the clicked tab to active
    $(this).addClass("is-active");

    var tab = $(this).text();
    console.log(tab);
    // strip whitespace
    tab = tab.replace(/\s/g, "");
    switch (tab) {
      case "All":
        $("#submission-form-all").show();
        $("#submission-form-c1").hide();
        $("#submission-form-c2").hide();
        $("#submission-form-c3").hide();
        $("#submission-form-c4").hide();
        $("#submission-form-c5").hide();
        $("#submission-form-summary").hide();
        break;
      case "C1":
        $("#submission-form-all").hide();
        $("#submission-form-c1").show();
        $("#submission-form-c2").hide();
        $("#submission-form-c3").hide();
        $("#submission-form-c4").hide();
        $("#submission-form-c5").hide();
        $("#submission-form-summary").hide();
        break;
      case "C2":
        $("#submission-form-all").hide();
        $("#submission-form-c1").hide();
        $("#submission-form-c2").show();
        $("#submission-form-c3").hide();
        $("#submission-form-c4").hide();
        $("#submission-form-c5").hide();
        $("#submission-form-summary").hide();
        break;
      case "C3":
        $("#submission-form-all").hide();
        $("#submission-form-c1").hide();
        $("#submission-form-c2").hide();
        $("#submission-form-c3").show();
        $("#submission-form-c4").hide();
        $("#submission-form-c5").hide();
        $("#submission-form-summary").hide();
        break;
      case "C4":
        $("#submission-form-all").hide();
        $("#submission-form-c1").hide();
        $("#submission-form-c2").hide();
        $("#submission-form-c3").hide();
        $("#submission-form-c4").show();
        $("#submission-form-c5").hide();
        $("#submission-form-summary").hide();
        break;
      case "C5":
        $("#submission-form-all").hide();
        $("#submission-form-c1").hide();
        $("#submission-form-c2").hide();
        $("#submission-form-c3").hide();
        $("#submission-form-c4").hide();
        $("#submission-form-c5").show();
        $("#submission-form-summary").hide();
        break;
      case "Summary":
        $("#submission-form-all").hide();
        $("#submission-form-c1").hide();
        $("#submission-form-c2").hide();
        $("#submission-form-c3").hide();
        $("#submission-form-c4").hide();
        $("#submission-form-c5").hide();
        $("#submission-form-summary").show();
        break;
    }
  });
});
