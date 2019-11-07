$(document).ready(function() {
  $(".container").css(
    "background-image",
    "url(static/musicpage/11.jpeg)"
  );
  $(".text-1").css({
    "background-color": "rgba(72, 72, 72, 1)",
    color: "white"
  });

  $(".text-1").hover(function() {
    $(".container").css(
      "background-image",
      "url(static/musicpage/1.jpg)"
    );
    $(".text-1").css({
      "background-color": "rgba(72, 72, 72, 1)",
      color: "white"
    });
    $(".text-2, .text-3, .text-4").css({
      "background-color": "rgba(255,255,255,0.6)",
      color: "black"
    });
  });

  $(".text-2").hover(function() {
    $(".container").css(
      "background-image",
      "url(static/musicpage/2.jpg)"
    );
    $(".text-2").css({
      "background-color": "rgba(72, 72, 72, 1)",
      color: "white"
    });
    $(".text-1, .text-3, .text-4").css({
      "background-color": "rgba(255,255,255,0.6)",
      color: "black"
    });
  });

  $(".text-3").hover(function() {
    $(".container").css(
      "background-image",
      "url(static/musicpage/3.jpg)"
    );
    $(".text-3").css({
      "background-color": "rgba(72, 72, 72, 1)",
      color: "white"
    });
    $(".text-1, .text-2, .text-4").css({
      "background-color": "rgba(255,255,255,0.6)",
      color: "black"
    });
  });

  $(".text-4").hover(function() {
    $(".container").css(
      "background-image",
      "url(static/musicpage/4.jpg)"
    );
    $(".text-4").css({
      "background-color": "rgba(72, 72, 72, 1)",
      color: "white"
    });
    $(".text-1, .text-2, .text-3").css({
      "background-color": "rgba(255,255,255,0.6)",
      color: "black"
    });
  });
});