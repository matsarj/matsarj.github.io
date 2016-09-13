---
layout: post
title: "Predicting Run or Pass on Second Down"
icon: "/projects/PredictingRunOrPass/football.jpg"
mainpic: "/projects/PredictingRunOrPass/RunOrPass.jpg"
name: "1_PredictingRunOrPass"
excerpt: "The purpose of this project is to implement some machine learning algorithms to try and predict whether a team will run or pass on second down, using the 2015 NFL Play-By-Play dataset."
---

<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.6 (http://getbootstrap.com)
 * Copyright 2011-2015 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    color: #000 !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.2.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.2.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.2.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.2.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.2.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.2.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1);
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
@media (max-width: 991px) {
  #ipython_notebook {
    margin-left: 10px;
  }
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#login_widget {
  float: right;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  text-align: center;
  vertical-align: middle;
  display: inline;
  opacity: 0;
  z-index: 2;
  width: 12ex;
  margin-right: -12ex;
}
.alternate_upload .btn-upload {
  height: 22px;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: baseline;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI colors. */
.ansibold {
  font-weight: bold;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  border-left-width: 1px;
  padding-left: 5px;
  background: linear-gradient(to right, transparent -40px, transparent 1px, transparent 1px, transparent 100%);
}
div.cell.jupyter-soft-selected {
  border-left-color: #90CAF9;
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected {
  border-color: #ababab;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 5px, transparent 5px, transparent 100%);
}
@media print {
  div.cell.selected {
    border-color: transparent;
  }
}
div.cell.selected.jupyter-soft-selected {
  border-left-width: 0;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 7px, #E3F2FD 7px, #E3F2FD 100%);
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #66BB6A -40px, #66BB6A 5px, transparent 5px, transparent 100%);
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
@-moz-document url-prefix() {
  div.inner_cell {
    overflow-x: hidden;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  padding: 0.4em;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. We need the 0 value because of how we size */
  /* .CodeMirror-lines */
  padding: 0;
  border: 0;
  border-radius: 0;
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul {
  list-style: disc;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ul ul {
  list-style: square;
  margin: 0em 2em;
}
.rendered_html ul ul ul {
  list-style: circle;
  margin: 0em 2em;
}
.rendered_html ol {
  list-style: decimal;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
  margin: 0em 2em;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  background-color: #fff;
  color: #000;
  font-size: 100%;
  padding: 0px;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: 1px solid black;
  border-collapse: collapse;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  border: 1px solid black;
  border-collapse: collapse;
  margin: 1em 2em;
}
.rendered_html td,
.rendered_html th {
  text-align: left;
  vertical-align: middle;
  padding: 4px;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget {
  float: right !important;
  float: right;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 20ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  margin-top: 6px;
}
span.save_widget span.filename {
  height: 1em;
  line-height: 1em;
  padding: 3px;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  display: none;
}
.command-shortcut:before {
  content: "(command)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}

@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Predicting-Second-Down">Predicting Second Down<a class="anchor-link" href="#Predicting-Second-Down">&#182;</a></h1><h3 id="The-purpose-of-this-notebook-is-to-implement-some-machine-learning-algorithms-to-try-and-predict-whether-a-team-will-run-or-pass-on-second-down,-using-the-2015-NFL-Play-By-Play-dataset.">The purpose of this notebook is to implement some machine learning algorithms to try and predict whether a team will run or pass on second down, using the 2015 NFL Play-By-Play dataset.<a class="anchor-link" href="#The-purpose-of-this-notebook-is-to-implement-some-machine-learning-algorithms-to-try-and-predict-whether-a-team-will-run-or-pass-on-second-down,-using-the-2015-NFL-Play-By-Play-dataset.">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># First Let&#39;s import the necessary packages</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span> <span class="c1"># Package used for working with dataframes</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span> <span class="c1"># Package used for working with arrays</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span> <span class="c1">#Package used visualizing our data</span>
<span class="o">%</span><span class="k">matplotlib</span> inline 
<span class="c1">#This command causes plots to show up in notebook</span>

<span class="c1">#sklearn is the machine learning package</span>
<span class="c1">#First we load in the instances to preprocess our data</span>
<span class="kn">from</span> <span class="nn">sklearn</span> <span class="k">import</span> <span class="n">preprocessing</span>
<span class="kn">from</span> <span class="nn">sklearn.feature_selection</span> <span class="k">import</span> <span class="n">SelectKBest</span><span class="p">,</span> <span class="n">f_classif</span>
<span class="kn">from</span> <span class="nn">sklearn</span> <span class="k">import</span> <span class="n">cross_validation</span>

<span class="c1">#Next we load the various algorithms we will be using:</span>
<span class="c1">#logistic regression, k-nearest neighbors, support vector machines, random trees and random forests</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="k">import</span> <span class="n">LogisticRegression</span>
<span class="kn">from</span> <span class="nn">sklearn.neighbors</span> <span class="k">import</span> <span class="n">KNeighborsClassifier</span>
<span class="kn">from</span> <span class="nn">sklearn</span> <span class="k">import</span> <span class="n">svm</span>
<span class="kn">from</span> <span class="nn">sklearn</span> <span class="k">import</span> <span class="n">tree</span>
<span class="kn">from</span> <span class="nn">sklearn.ensemble</span> <span class="k">import</span> <span class="n">RandomForestClassifier</span>

<span class="c1">#Finally, the gridsearch instance will allow us to fine-tune our algorithms</span>
<span class="kn">from</span> <span class="nn">sklearn.grid_search</span> <span class="k">import</span> <span class="n">GridSearchCV</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Now we will read in the data pick out the second down plays which resulted in a run or a pass</span>

<span class="n">file_loc</span> <span class="o">=</span> <span class="s2">&quot;/home/matt/Downloads/nfl.csv&quot;</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">file_loc</span><span class="p">)</span>

<span class="n">second</span> <span class="o">=</span> <span class="n">data</span><span class="p">[(</span><span class="n">data</span><span class="p">[</span><span class="s1">&#39;down&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="mi">2</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">((</span><span class="n">data</span><span class="p">[</span><span class="s1">&#39;PlayType&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;Pass&#39;</span><span class="p">)</span> <span class="o">|</span> <span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s1">&#39;PlayType&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;Run&#39;</span><span class="p">))]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>/home/matt/anaconda3/lib/python3.5/site-packages/IPython/core/interactiveshell.py:2723: DtypeWarning: Columns (26) have mixed types. Specify dtype option on import or set low_memory=False.
  interactivity=interactivity, compiler=compiler, result=result)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Before-running-any-algorithms,-let's-do-some-naive-predictions.-A-very-basic-prediction-is-to-always-choose-the-most-frequent-play-type.">Before running any algorithms, let's do some naive predictions. A very basic prediction is to always choose the most frequent play type.<a class="anchor-link" href="#Before-running-any-algorithms,-let's-do-some-naive-predictions.-A-very-basic-prediction-is-to-always-choose-the-most-frequent-play-type.">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">breakdown</span> <span class="o">=</span> <span class="n">second</span><span class="p">[</span><span class="s1">&#39;PlayType&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
<span class="n">breakdown</span><span class="p">[</span><span class="s1">&#39;Pass&#39;</span><span class="p">]</span><span class="o">/</span> <span class="p">(</span><span class="n">breakdown</span><span class="p">[</span><span class="s1">&#39;Pass&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="n">breakdown</span><span class="p">[</span><span class="s1">&#39;Run&#39;</span><span class="p">])</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[4]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>0.58024926267719534</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="This-tells-us-that-we-can-guess-correctly-58%-of-the-time-just-by-always-choosing-pass.-On-the-other-hand,-if-it-is-second-and-short-a-run-is-more-likely-than-a-pass,-as-the-following-plots-illustrate.">This tells us that we can guess correctly 58% of the time just by always choosing pass. On the other hand, if it is second and short a run is more likely than a pass, as the following plots illustrate.<a class="anchor-link" href="#This-tells-us-that-we-can-guess-correctly-58%-of-the-time-just-by-always-choosing-pass.-On-the-other-hand,-if-it-is-second-and-short-a-run-is-more-likely-than-a-pass,-as-the-following-plots-illustrate.">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">passing</span> <span class="o">=</span> <span class="n">second</span><span class="p">[</span><span class="n">second</span><span class="p">[</span><span class="s1">&#39;PlayType&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;Pass&#39;</span><span class="p">]</span>
<span class="n">running</span> <span class="o">=</span> <span class="n">second</span><span class="p">[</span><span class="n">second</span><span class="p">[</span><span class="s1">&#39;PlayType&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;Run&#39;</span><span class="p">]</span>

<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">5</span><span class="p">))</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">11</span><span class="p">):</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="n">i</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">pie</span><span class="p">([</span><span class="n">second</span><span class="p">[</span><span class="n">second</span><span class="p">[</span><span class="s1">&#39;ydstogo&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="n">i</span><span class="p">][</span><span class="s1">&#39;PlayType&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()[</span><span class="s1">&#39;Pass&#39;</span><span class="p">],</span>
           <span class="n">second</span><span class="p">[</span><span class="n">second</span><span class="p">[</span><span class="s1">&#39;ydstogo&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="n">i</span><span class="p">][</span><span class="s1">&#39;PlayType&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()[</span><span class="s1">&#39;Run&#39;</span><span class="p">]],</span> <span class="n">colors</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Blue&#39;</span><span class="p">,</span> <span class="s1">&#39;Red&#39;</span><span class="p">])</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Second and </span><span class="si">%i</span><span class="s1">&#39;</span> <span class="o">%</span><span class="k">i</span>)
    <span class="n">plt</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">([</span><span class="s1">&#39;Pass&#39;</span><span class="p">,</span><span class="s1">&#39;Run&#39;</span><span class="p">],</span> <span class="n">bbox_to_anchor</span> <span class="o">=</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mf">1.5</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[5]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.legend.Legend at 0x7f31e122d240&gt;</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
VwAAAABJRU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="As-we-can-see,-it-is-reasonable-to-predict-run-if-it-is-second-down-with-five-or-fewer-yards-to-go,-and-pass-otherwise.-Let's-see-how-good-this-simple-strategy-is.">As we can see, it is reasonable to predict run if it is second down with five or fewer yards to go, and pass otherwise. Let's see how good this simple strategy is.<a class="anchor-link" href="#As-we-can-see,-it-is-reasonable-to-predict-run-if-it-is-second-down-with-five-or-fewer-yards-to-go,-and-pass-otherwise.-Let's-see-how-good-this-simple-strategy-is.">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">second</span><span class="p">[</span><span class="s1">&#39;Prediction&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">second</span><span class="p">[</span><span class="s1">&#39;ydstogo&#39;</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="mi">5</span>
<span class="n">second</span><span class="p">[</span><span class="s1">&#39;Ran&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">second</span><span class="p">[</span><span class="s1">&#39;PlayType&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;Run&#39;</span>

<span class="n">check</span> <span class="o">=</span> <span class="n">second</span><span class="p">[</span><span class="s1">&#39;Prediction&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="n">second</span><span class="p">[</span><span class="s1">&#39;Ran&#39;</span><span class="p">]</span>
<span class="n">check</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>/home/matt/anaconda3/lib/python3.5/site-packages/ipykernel/__main__.py:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  if __name__ == &#39;__main__&#39;:
/home/matt/anaconda3/lib/python3.5/site-packages/ipykernel/__main__.py:2: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  from ipykernel import kernelapp as app
</pre>
</div>
</div>

<div class="output_area"><div class="prompt output_prompt">Out[5]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>0.62553515364855861</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="So-we-have-a-62.6%-chance-of-predicting-correctly-if-we-choose-run-when-it-is-second-down-with-five-or-fewer-yards-to-go,-and-choose-pass-otherwise.-Let's-see-if-we-can-beat-this-by-applying-some-common-classification-algorithms.-First-let's-single-out-some-columns-which-we-believe-will-make-the-best-predictors,-and-separate-our-data-into-training-and-testing-subsets.">So we have a 62.6% chance of predicting correctly if we choose run when it is second down with five or fewer yards to go, and choose pass otherwise. Let's see if we can beat this by applying some common classification algorithms. First let's single out some columns which we believe will make the best predictors, and separate our data into training and testing subsets.<a class="anchor-link" href="#So-we-have-a-62.6%-chance-of-predicting-correctly-if-we-choose-run-when-it-is-second-down-with-five-or-fewer-yards-to-go,-and-choose-pass-otherwise.-Let's-see-if-we-can-beat-this-by-applying-some-common-classification-algorithms.-First-let's-single-out-some-columns-which-we-believe-will-make-the-best-predictors,-and-separate-our-data-into-training-and-testing-subsets.">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#TimeInHalf will contain seconds left in the half</span>
<span class="n">second</span><span class="p">[</span><span class="s1">&#39;TimeInHalf&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">second</span><span class="p">[</span><span class="s1">&#39;TimeSecs&#39;</span><span class="p">]</span><span class="o">%</span><span class="p">(</span><span class="mi">60</span><span class="o">*</span><span class="mi">30</span><span class="p">)</span>

<span class="c1">#Normalize data for better results</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">preprocessing</span><span class="o">.</span><span class="n">scale</span><span class="p">(</span><span class="n">second</span><span class="p">[[</span><span class="s1">&#39;ydstogo&#39;</span><span class="p">,</span> <span class="s1">&#39;yrdline100&#39;</span><span class="p">,</span> <span class="s1">&#39;TimeInHalf&#39;</span><span class="p">,</span> <span class="s1">&#39;ScoreDiff&#39;</span><span class="p">]])</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">preprocessing</span><span class="o">.</span><span class="n">normalize</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">norm</span> <span class="o">=</span> <span class="s1">&#39;l2&#39;</span><span class="p">)</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">second</span><span class="p">[</span><span class="s1">&#39;PlayType&#39;</span><span class="p">]</span>

<span class="c1">#Separate 20% of the data for testing</span>
<span class="n">X_train</span><span class="p">,</span> <span class="n">X_test</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">cross_validation</span><span class="o">.</span><span class="n">train_test_split</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">test_size</span> <span class="o">=</span> <span class="o">.</span><span class="mi">2</span><span class="p">,</span> <span class="n">random_state</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>/home/matt/anaconda3/lib/python3.5/site-packages/ipykernel/__main__.py:2: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  from ipykernel import kernelapp as app
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="It-will-be-easier-to-visualize-things-with-two-predictors,-so-we-can-plot-them-on-a-plane.-Fortunately,-sklearn-has-an-instance-which-chooses-the-two-best-predictors.-It-turns-out-that-this-is-the-number-of-yards-to-go-and-the-score-differential.">It will be easier to visualize things with two predictors, so we can plot them on a plane. Fortunately, sklearn has an instance which chooses the two best predictors. It turns out that this is the number of yards to go and the score differential.<a class="anchor-link" href="#It-will-be-easier-to-visualize-things-with-two-predictors,-so-we-can-plot-them-on-a-plane.-Fortunately,-sklearn-has-an-instance-which-chooses-the-two-best-predictors.-It-turns-out-that-this-is-the-number-of-yards-to-go-and-the-score-differential.">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Choose the 2 best features</span>
<span class="n">selector</span> <span class="o">=</span> <span class="n">SelectKBest</span><span class="p">(</span><span class="n">f_classif</span><span class="p">,</span> <span class="n">k</span> <span class="o">=</span> <span class="mi">2</span><span class="p">)</span>
<span class="n">selector</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
<span class="n">scores</span> <span class="o">=</span> <span class="o">-</span><span class="n">np</span><span class="o">.</span><span class="n">log10</span><span class="p">(</span><span class="n">selector</span><span class="o">.</span><span class="n">pvalues_</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">],</span><span class="n">scores</span><span class="p">,</span> <span class="n">align</span> <span class="o">=</span> <span class="s1">&#39;center&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Feature Selection&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;Features&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;Score&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">],[</span><span class="s1">&#39;Yards to Go&#39;</span><span class="p">,</span><span class="s1">&#39;Yard Line&#39;</span><span class="p">,</span> <span class="s1">&#39;Time in Half&#39;</span><span class="p">,</span> <span class="s1">&#39;Score Differential&#39;</span><span class="p">])</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[20]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>([&lt;matplotlib.axis.XTick at 0x7f31dc72bdd8&gt;,
  &lt;matplotlib.axis.XTick at 0x7f31dc988240&gt;,
  &lt;matplotlib.axis.XTick at 0x7f31dc98db00&gt;,
  &lt;matplotlib.axis.XTick at 0x7f31dca7d1d0&gt;],
 &lt;a list of 4 Text xticklabel objects&gt;)</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
AABJRU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Pick the first and fourth columns, which contain the best predictors</span>
<span class="n">X_train</span> <span class="o">=</span> <span class="n">X_train</span><span class="p">[:,</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">3</span><span class="p">]]</span>
<span class="n">X_test</span> <span class="o">=</span> <span class="n">X_test</span><span class="p">[:,</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">3</span><span class="p">]]</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[33]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">second</span><span class="p">[</span><span class="s1">&#39;color&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">repeat</span><span class="p">(</span><span class="s1">&#39;Blue&#39;</span><span class="p">,</span> <span class="n">second</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
<span class="n">second</span><span class="o">.</span><span class="n">ix</span><span class="p">[</span><span class="n">second</span><span class="o">.</span><span class="n">Ran</span> <span class="o">==</span> <span class="kc">True</span><span class="p">,</span><span class="s1">&#39;color&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s1">&#39;Red&#39;</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">second</span><span class="p">[</span><span class="s1">&#39;ydstogo&#39;</span><span class="p">],</span> <span class="n">second</span><span class="p">[</span><span class="s1">&#39;ScoreDiff&#39;</span><span class="p">],</span> <span class="n">color</span> <span class="o">=</span> <span class="n">second</span><span class="p">[</span><span class="s1">&#39;color&#39;</span><span class="p">],</span> <span class="n">label</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Run&#39;</span><span class="p">,</span> <span class="s1">&#39;Pass&#39;</span><span class="p">])</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Yards To Go&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Score Differential&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Original Data, with Run in Red and Pass in Blue&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>/home/matt/anaconda3/lib/python3.5/site-packages/ipykernel/__main__.py:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  if __name__ == &#39;__main__&#39;:
/home/matt/anaconda3/lib/python3.5/site-packages/pandas/core/indexing.py:465: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  self.obj[item] = s
</pre>
</div>
</div>

<div class="output_area"><div class="prompt output_prompt">Out[33]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.text.Text at 0x7fb211320fd0&gt;</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
/wMa3X6ihRSoRwAAAABJRU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[36]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">121</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Original Data, Normalized&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span> <span class="o">=</span> <span class="s2">&quot;Yards To Go&quot;</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span> <span class="o">=</span> <span class="s2">&quot;Score Differential&quot;</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">X</span><span class="p">[:,</span><span class="mi">0</span><span class="p">],</span> <span class="n">X</span><span class="p">[:,</span><span class="mi">1</span><span class="p">],</span> <span class="n">color</span> <span class="o">=</span> <span class="n">second</span><span class="p">[</span><span class="s1">&#39;color&#39;</span><span class="p">])</span>
<span class="n">color</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">second</span><span class="p">[</span><span class="s1">&#39;Prediction&#39;</span><span class="p">]:</span>
    <span class="k">if</span> <span class="n">value</span> <span class="o">==</span> <span class="kc">True</span><span class="p">:</span>
        <span class="n">color</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;Red&#39;</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">color</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;Blue&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">122</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">X</span><span class="p">[:,</span><span class="mi">0</span><span class="p">],</span> <span class="n">X</span><span class="p">[:,</span><span class="mi">1</span><span class="p">],</span> <span class="n">color</span> <span class="o">=</span> <span class="n">color</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Naive Prediction&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[36]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.text.Text at 0x7fb211139400&gt;</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
TsAwDCOJ+Sc4mqiaiEqAjAAAAABJRU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Now-we-will-apply-a-few-classification-algorithms:-logistic-regression,-k-nearest-neighbors,-support-vector-machine,-decision-tree,-and-random-forest.">Now we will apply a few classification algorithms: logistic regression, k-nearest neighbors, support vector machine, decision tree, and random forest.<a class="anchor-link" href="#Now-we-will-apply-a-few-classification-algorithms:-logistic-regression,-k-nearest-neighbors,-support-vector-machine,-decision-tree,-and-random-forest.">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Run logistic regression on our training data</span>

<span class="n">logistic</span> <span class="o">=</span> <span class="n">LogisticRegression</span><span class="p">()</span>
<span class="n">logistic</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[38]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class=&#39;ovr&#39;, n_jobs=1,
          penalty=&#39;l2&#39;, random_state=None, solver=&#39;liblinear&#39;, tol=0.0001,
          verbose=0, warm_start=False)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[39]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Use logistic regression model to predict pass or run on our test data</span>

<span class="n">check</span> <span class="o">=</span> <span class="n">logistic</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span> <span class="o">==</span> <span class="n">y_test</span>
<span class="n">check</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[39]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>0.63670946267237283</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[40]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">color</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">logistic</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">value</span> <span class="o">==</span> <span class="s1">&#39;Run&#39;</span><span class="p">:</span>
        <span class="n">color</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;Red&#39;</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">color</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;Blue&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">X_test</span><span class="p">[:,</span><span class="mi">0</span><span class="p">],</span> <span class="n">X_test</span><span class="p">[:,</span><span class="mi">1</span><span class="p">],</span> <span class="n">color</span> <span class="o">=</span> <span class="n">color</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Logistic Regression Prediction&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[40]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.text.Text at 0x7fb21105d358&gt;</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[123]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Use k-nearest neighbors algorithm. I chose 61 through trial and error, but there&#39;s</span>
<span class="c1"># a way to have sklearn optimize paramters. I need to look into that more.</span>

<span class="n">neighbors</span> <span class="o">=</span> <span class="n">KNeighborsClassifier</span><span class="p">(</span><span class="n">n_neighbors</span> <span class="o">=</span> <span class="mi">61</span><span class="p">)</span>
<span class="n">neighbors</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span><span class="n">y_train</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[123]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>KNeighborsClassifier(algorithm=&#39;auto&#39;, leaf_size=30, metric=&#39;minkowski&#39;,
           metric_params=None, n_jobs=1, n_neighbors=61, p=2,
           weights=&#39;uniform&#39;)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[124]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">check</span> <span class="o">=</span> <span class="n">neighbors</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span> <span class="o">==</span> <span class="n">y_test</span>
<span class="n">check</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[124]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>0.64574417498811221</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[125]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">color</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">neighbors</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">value</span> <span class="o">==</span> <span class="s1">&#39;Run&#39;</span><span class="p">:</span>
        <span class="n">color</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;Red&#39;</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">color</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;Blue&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">X_test</span><span class="p">[:,</span><span class="mi">0</span><span class="p">],</span> <span class="n">X_test</span><span class="p">[:,</span><span class="mi">1</span><span class="p">],</span> <span class="n">color</span> <span class="o">=</span> <span class="n">color</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[125]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.collections.PathCollection at 0x7fb210ebb748&gt;</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[133]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Run support vector machine with a linear kernel. Again, it may be</span>
<span class="c1"># possible to do better by tweaking some parameters.</span>
<span class="n">support</span> <span class="o">=</span> <span class="n">svm</span><span class="o">.</span><span class="n">SVC</span><span class="p">(</span><span class="n">kernel</span> <span class="o">=</span> <span class="s2">&quot;linear&quot;</span><span class="p">)</span>
<span class="n">support</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[133]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma=&#39;auto&#39;, kernel=&#39;linear&#39;,
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[134]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">check</span> <span class="o">=</span> <span class="n">support</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span> <span class="o">==</span> <span class="n">y_test</span>
<span class="n">check</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[134]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>0.63766048502139805</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[135]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">color</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">support</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">value</span> <span class="o">==</span> <span class="s1">&#39;Run&#39;</span><span class="p">:</span>
        <span class="n">color</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;Red&#39;</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">color</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;Blue&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">X_test</span><span class="p">[:,</span><span class="mi">0</span><span class="p">],</span> <span class="n">X_test</span><span class="p">[:,</span><span class="mi">1</span><span class="p">],</span> <span class="n">color</span> <span class="o">=</span> <span class="n">color</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[135]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.collections.PathCollection at 0x7fb210da0550&gt;</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[136]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dectree</span> <span class="o">=</span> <span class="n">tree</span><span class="o">.</span><span class="n">DecisionTreeClassifier</span><span class="p">()</span>
<span class="n">dectree</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[136]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>DecisionTreeClassifier(class_weight=None, criterion=&#39;gini&#39;, max_depth=None,
            max_features=None, max_leaf_nodes=None, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            presort=False, random_state=None, splitter=&#39;best&#39;)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[137]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">check</span> <span class="o">=</span> <span class="n">dectree</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span> <span class="o">==</span> <span class="n">y_test</span>
<span class="n">check</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[137]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>0.56918687589158345</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[138]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">color</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">dectree</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">value</span> <span class="o">==</span> <span class="s1">&#39;Run&#39;</span><span class="p">:</span>
        <span class="n">color</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;Red&#39;</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">color</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;Blue&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">X_test</span><span class="p">[:,</span><span class="mi">0</span><span class="p">],</span> <span class="n">X_test</span><span class="p">[:,</span><span class="mi">1</span><span class="p">],</span> <span class="n">color</span> <span class="o">=</span> <span class="n">color</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[138]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.collections.PathCollection at 0x7fb210d7dcc0&gt;</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[154]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Rfor</span> <span class="o">=</span> <span class="n">RandomForestClassifier</span><span class="p">(</span><span class="n">n_estimators</span> <span class="o">=</span> <span class="mi">10</span><span class="p">)</span>
<span class="n">Rfor</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[154]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>RandomForestClassifier(bootstrap=True, class_weight=None, criterion=&#39;gini&#39;,
            max_depth=None, max_features=&#39;auto&#39;, max_leaf_nodes=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
            oob_score=False, random_state=None, verbose=0,
            warm_start=False)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[153]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">check</span> <span class="o">=</span> <span class="n">Rfor</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span> <span class="o">==</span> <span class="n">y_test</span>
<span class="n">check</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[153]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>0.57822158820732283</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[155]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">color</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">Rfor</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">value</span> <span class="o">==</span> <span class="s1">&#39;Run&#39;</span><span class="p">:</span>
        <span class="n">color</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;Red&#39;</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">color</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;Blue&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">X_test</span><span class="p">[:,</span><span class="mi">0</span><span class="p">],</span> <span class="n">X_test</span><span class="p">[:,</span><span class="mi">1</span><span class="p">],</span> <span class="n">color</span> <span class="o">=</span> <span class="n">color</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[155]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.collections.PathCollection at 0x7fb21166fb00&gt;</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
huN32ltsWgAAAABJRU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="In-conclusion,-we-were-able-to-do-better-(though-not-a-whole-lot-better)-than-the-naive-prediction-using-logistic-regression,-k-nearest-neighbors,-and-the-support-vector-machine-algorithms.-It-should-be-possible-to-do-even-better-by-using-grid-searching-techniques-to-optimize-our-parameters.">In conclusion, we were able to do better (though not a whole lot better) than the naive prediction using logistic regression, k-nearest neighbors, and the support vector machine algorithms. It should be possible to do even better by using grid-searching techniques to optimize our parameters.<a class="anchor-link" href="#In-conclusion,-we-were-able-to-do-better-(though-not-a-whole-lot-better)-than-the-naive-prediction-using-logistic-regression,-k-nearest-neighbors,-and-the-support-vector-machine-algorithms.-It-should-be-possible-to-do-even-better-by-using-grid-searching-techniques-to-optimize-our-parameters.">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-cyan-intense-fg ansi-bold">  File </span><span class="ansi-green-intense-fg ansi-bold">&#34;&lt;ipython-input-10-7849c0c5f9a7&gt;&#34;</span><span class="ansi-cyan-intense-fg ansi-bold">, line </span><span class="ansi-green-intense-fg ansi-bold">1</span>
<span class="ansi-yellow-intense-fg ansi-bold">    jupyter nbconvert --to FORMAT notebook.ipynb</span>
<span class="ansi-white-intense-fg ansi-bold">                    ^</span>
<span class="ansi-red-intense-fg ansi-bold">SyntaxError</span><span class="ansi-red-intense-fg ansi-bold">:</span> invalid syntax
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

</div>
</div>
</div>

</div>
    </div>
  </div>
</body>
