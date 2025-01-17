<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />
<title>Explore_bikeshare_data</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
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
[dir="rtl"] #ipython_notebook {
  float: right !important;
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
[dir="rtl"] #tabs li {
  float: right;
}
ul#tabs {
  margin-bottom: 4px;
}
[dir="rtl"] ul#tabs {
  margin-right: 0px;
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
[dir="rtl"] .list_toolbar .tree-buttons {
  float: left !important;
}
[dir="rtl"] .list_toolbar .pull-right {
  padding-top: 1px;
  float: left !important;
}
[dir="rtl"] .list_toolbar .pull-left {
  float: right !important;
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
[dir="rtl"] #tree-selector a {
  float: right;
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
[dir="rtl"] #new-menu {
  text-align: right;
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
[dir="rtl"] #running .col-sm-8 {
  float: right !important;
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
  min-width: 0;
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
  width: 21ex;
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
  width: 100%;
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
.terminal-app .terminal .xterm-rows {
  padding: 10px;
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
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
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
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
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
    body[data-notebook-name] > #header #header-container:not(.show-panel), /* body has data-notebook-name attribute when 
a notebook is open. this rule won't be applied when the notebook is not open (in 404 view for example) */
body[data-notebook-name] #menubar-container #maintoolbar:not(.show-panel),
body[data-notebook-name] #menubar-container ul.navbar-nav:not(.show-panel) {
  display: none;
}

#menubar.only-panel #menus.navbar-default {
    background: #fff;
    border-color: #fff;
}

.toolbar.with-statusbar{
    margin-top: 3px;
    margin-bottom: 0;
}

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
}@media print {
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
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML"></script>
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

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Explore-Bike-Share-Data">Explore Bike Share Data<a class="anchor-link" href="#Explore-Bike-Share-Data">&#182;</a></h3><p>For this project, your goal is to ask and answer three questions about the available bikeshare data from Washington, Chicago, and New York.  This notebook can be submitted directly through the workspace when you are confident in your results.</p>
<p>You will be graded against the project <a href="https://review.udacity.com/#!/rubrics/2508/view">Rubric</a> by a mentor after you have submitted.  To get you started, you can use the template below, but feel free to be creative in your solutions!</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="n">ny</span> <span class="o">=</span> <span class="nf">read.csv</span><span class="p">(</span><span class="s">&#39;new_york_city.csv&#39;</span><span class="p">)</span>
<span class="n">wash</span> <span class="o">=</span> <span class="nf">read.csv</span><span class="p">(</span><span class="s">&#39;washington.csv&#39;</span><span class="p">)</span>
<span class="n">chi</span> <span class="o">=</span> <span class="nf">read.csv</span><span class="p">(</span><span class="s">&#39;chicago.csv&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="nf">head</span><span class="p">(</span><span class="n">ny</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<table>
<thead><tr><th scope=col>X</th><th scope=col>Start.Time</th><th scope=col>End.Time</th><th scope=col>Trip.Duration</th><th scope=col>Start.Station</th><th scope=col>End.Station</th><th scope=col>User.Type</th><th scope=col>Gender</th><th scope=col>Birth.Year</th></tr></thead>
<tbody>
	<tr><td>5688089                                       </td><td>2017-06-11 14:55:05                           </td><td>2017-06-11 15:08:21                           </td><td> 795                                          </td><td>Suffolk St &amp; Stanton St                   </td><td>W Broadway &amp; Spring St                    </td><td>Subscriber                                    </td><td><span style=white-space:pre-wrap>Male  </span></td><td>1998                                          </td></tr>
	<tr><td>4096714                                                           </td><td>2017-05-11 15:30:11                                               </td><td>2017-05-11 15:41:43                                               </td><td> 692                                                              </td><td>Lexington Ave &amp; E 63 St                                       </td><td><span style=white-space:pre-wrap>1 Ave &amp; E 78 St       </span></td><td>Subscriber                                                        </td><td><span style=white-space:pre-wrap>Male  </span>                    </td><td>1981                                                              </td></tr>
	<tr><td>2173887                                                            </td><td>2017-03-29 13:26:26                                                </td><td>2017-03-29 13:48:31                                                </td><td>1325                                                               </td><td><span style=white-space:pre-wrap>1 Pl &amp; Clinton St      </span></td><td><span style=white-space:pre-wrap>Henry St &amp; Degraw St  </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1987                                                               </td></tr>
	<tr><td>3945638                                                            </td><td>2017-05-08 19:47:18                                                </td><td>2017-05-08 19:59:01                                                </td><td> 703                                                               </td><td><span style=white-space:pre-wrap>Barrow St &amp; Hudson St  </span></td><td><span style=white-space:pre-wrap>W 20 St &amp; 8 Ave       </span> </td><td>Subscriber                                                         </td><td>Female                                                             </td><td>1986                                                               </td></tr>
	<tr><td>6208972                                                            </td><td>2017-06-21 07:49:16                                                </td><td>2017-06-21 07:54:46                                                </td><td> 329                                                               </td><td><span style=white-space:pre-wrap>1 Ave &amp; E 44 St        </span></td><td><span style=white-space:pre-wrap>E 53 St &amp; 3 Ave       </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1992                                                               </td></tr>
	<tr><td>1285652                                                            </td><td>2017-02-22 18:55:24                                                </td><td>2017-02-22 19:12:03                                                </td><td> 998                                                               </td><td><span style=white-space:pre-wrap>State St &amp; Smith St    </span></td><td><span style=white-space:pre-wrap>Bond St &amp; Fulton St   </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1986                                                               </td></tr>
</tbody>
</table>

</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="nf">head</span><span class="p">(</span><span class="n">wash</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<table>
<thead><tr><th scope=col>X</th><th scope=col>Start.Time</th><th scope=col>End.Time</th><th scope=col>Trip.Duration</th><th scope=col>Start.Station</th><th scope=col>End.Station</th><th scope=col>User.Type</th></tr></thead>
<tbody>
	<tr><td>1621326                                                                                        </td><td>2017-06-21 08:36:34                                                                            </td><td>2017-06-21 08:44:43                                                                            </td><td> 489.066                                                                                       </td><td><span style=white-space:pre-wrap>14th &amp; Belmont St NW                       </span>        </td><td><span style=white-space:pre-wrap>15th &amp; K St NW                                     </span></td><td>Subscriber                                                                                     </td></tr>
	<tr><td> 482740                                                                                        </td><td>2017-03-11 10:40:00                                                                            </td><td>2017-03-11 10:46:00                                                                            </td><td> 402.549                                                                                       </td><td><span style=white-space:pre-wrap>Yuma St &amp; Tenley Circle NW                 </span>        </td><td><span style=white-space:pre-wrap>Connecticut Ave &amp; Yuma St NW                       </span></td><td>Subscriber                                                                                     </td></tr>
	<tr><td>1330037                                                                                        </td><td>2017-05-30 01:02:59                                                                            </td><td>2017-05-30 01:13:37                                                                            </td><td> 637.251                                                                                       </td><td><span style=white-space:pre-wrap>17th St &amp; Massachusetts Ave NW             </span>        </td><td><span style=white-space:pre-wrap>5th &amp; K St NW                                      </span></td><td>Subscriber                                                                                     </td></tr>
	<tr><td> 665458                                                                                        </td><td>2017-04-02 07:48:35                                                                            </td><td>2017-04-02 08:19:03                                                                            </td><td>1827.341                                                                                       </td><td><span style=white-space:pre-wrap>Constitution Ave &amp; 2nd St NW/DOL           </span>        </td><td><span style=white-space:pre-wrap>M St &amp; Pennsylvania Ave NW                         </span></td><td><span style=white-space:pre-wrap>Customer  </span>                                             </td></tr>
	<tr><td>1481135                                                                                        </td><td>2017-06-10 08:36:28                                                                            </td><td>2017-06-10 09:02:17                                                                            </td><td>1549.427                                                                                       </td><td>Henry Bacon Dr &amp; Lincoln Memorial Circle NW                                                </td><td><span style=white-space:pre-wrap>Maine Ave &amp; 7th St SW                              </span></td><td>Subscriber                                                                                     </td></tr>
	<tr><td>1148202                                                                                </td><td>2017-05-14 07:18:18                                                                    </td><td>2017-05-14 07:24:56                                                                    </td><td> 398.000                                                                               </td><td><span style=white-space:pre-wrap>1st &amp; K St SE                              </span></td><td>Eastern Market Metro / Pennsylvania Ave &amp; 7th St SE                                </td><td>Subscriber                                                                             </td></tr>
</tbody>
</table>

</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="nf">head</span><span class="p">(</span><span class="n">chi</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<table>
<thead><tr><th scope=col>X</th><th scope=col>Start.Time</th><th scope=col>End.Time</th><th scope=col>Trip.Duration</th><th scope=col>Start.Station</th><th scope=col>End.Station</th><th scope=col>User.Type</th><th scope=col>Gender</th><th scope=col>Birth.Year</th></tr></thead>
<tbody>
	<tr><td>1423854                                                                  </td><td>2017-06-23 15:09:32                                                      </td><td>2017-06-23 15:14:53                                                      </td><td> 321                                                                     </td><td><span style=white-space:pre-wrap>Wood St &amp; Hubbard St         </span></td><td><span style=white-space:pre-wrap>Damen Ave &amp; Chicago Ave     </span> </td><td>Subscriber                                                               </td><td><span style=white-space:pre-wrap>Male  </span>                           </td><td>1992                                                                     </td></tr>
	<tr><td> 955915                                                              </td><td>2017-05-25 18:19:03                                                  </td><td>2017-05-25 18:45:53                                                  </td><td>1610                                                                 </td><td><span style=white-space:pre-wrap>Theater on the Lake          </span></td><td>Sheffield Ave &amp; Waveland Ave                                     </td><td>Subscriber                                                           </td><td>Female                                                               </td><td>1992                                                                 </td></tr>
	<tr><td><span style=white-space:pre-wrap>   9031</span>                          </td><td>2017-01-04 08:27:49                                                      </td><td>2017-01-04 08:34:45                                                      </td><td> 416                                                                     </td><td><span style=white-space:pre-wrap>May St &amp; Taylor St           </span></td><td><span style=white-space:pre-wrap>Wood St &amp; Taylor St         </span> </td><td>Subscriber                                                               </td><td><span style=white-space:pre-wrap>Male  </span>                           </td><td>1981                                                                     </td></tr>
	<tr><td> 304487                                       </td><td>2017-03-06 13:49:38                           </td><td>2017-03-06 13:55:28                           </td><td> 350                                          </td><td>Christiana Ave &amp; Lawrence Ave             </td><td>St. Louis Ave &amp; Balmoral Ave              </td><td>Subscriber                                    </td><td><span style=white-space:pre-wrap>Male  </span></td><td>1986                                          </td></tr>
	<tr><td><span style=white-space:pre-wrap>  45207</span>                          </td><td>2017-01-17 14:53:07                                                      </td><td>2017-01-17 15:02:01                                                      </td><td> 534                                                                     </td><td><span style=white-space:pre-wrap>Clark St &amp; Randolph St       </span></td><td>Desplaines St &amp; Jackson Blvd                                         </td><td>Subscriber                                                               </td><td><span style=white-space:pre-wrap>Male  </span>                           </td><td>1975                                                                     </td></tr>
	<tr><td>1473887                                                                 </td><td>2017-06-26 09:01:20                                                     </td><td>2017-06-26 09:11:06                                                     </td><td> 586                                                                    </td><td>Clinton St &amp; Washington Blvd                                        </td><td><span style=white-space:pre-wrap>Canal St &amp; Taylor St        </span></td><td>Subscriber                                                              </td><td><span style=white-space:pre-wrap>Male  </span>                          </td><td>1990                                                                    </td></tr>
</tbody>
</table>

</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># modifying wash to concat</span>
<span class="n">wash</span><span class="o">$</span><span class="n">Gender</span> <span class="o">&lt;-</span> <span class="kc">NA</span>
<span class="n">wash</span><span class="o">$</span><span class="n">Birth.Year</span> <span class="o">&lt;-</span><span class="kc">NA</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Adding a new column &#39;City&#39; to each dataset to retain info about city after concatenation</span>
<span class="n">ny</span><span class="o">$</span><span class="n">City</span> <span class="o">&lt;-</span> <span class="s">&#39;New York City&#39;</span>
<span class="n">wash</span><span class="o">$</span><span class="n">City</span> <span class="o">&lt;-</span> <span class="s">&#39;Washington&#39;</span>
<span class="n">chi</span><span class="o">$</span><span class="n">City</span> <span class="o">&lt;-</span> <span class="s">&#39;Chicago&#39;</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1">#Creating a function for concatenation</span>
<span class="n">concatenation</span> <span class="o">&lt;-</span> <span class="nf">function</span><span class="p">(</span><span class="n">d1</span><span class="p">,</span> <span class="n">d2</span><span class="p">)</span> <span class="p">{</span>
  <span class="nf">return</span><span class="p">(</span><span class="nf">rbind</span><span class="p">(</span><span class="n">d1</span><span class="p">,</span> <span class="n">d2</span><span class="p">))</span>
<span class="p">}</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Concatenating all three datasets together as &quot;city&quot;</span>
<span class="n">city</span> <span class="o">&lt;-</span> <span class="nf">concatenation</span><span class="p">(</span><span class="n">ny</span><span class="p">,</span><span class="n">wash</span><span class="p">)</span>     <span class="c1">#city &lt;- rbind(ny, wash)</span>
<span class="n">city</span> <span class="o">&lt;-</span> <span class="nf">concatenation</span><span class="p">(</span><span class="n">city</span><span class="p">,</span><span class="n">chi</span><span class="p">)</span>    <span class="c1">#city &lt;- rbind(city, chi)</span>
<span class="nf">head</span><span class="p">(</span><span class="n">city</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<table>
<thead><tr><th scope=col>X</th><th scope=col>Start.Time</th><th scope=col>End.Time</th><th scope=col>Trip.Duration</th><th scope=col>Start.Station</th><th scope=col>End.Station</th><th scope=col>User.Type</th><th scope=col>Gender</th><th scope=col>Birth.Year</th><th scope=col>City</th></tr></thead>
<tbody>
	<tr><td>5688089                                       </td><td>2017-06-11 14:55:05                           </td><td>2017-06-11 15:08:21                           </td><td> 795                                          </td><td>Suffolk St &amp; Stanton St                   </td><td>W Broadway &amp; Spring St                    </td><td>Subscriber                                    </td><td><span style=white-space:pre-wrap>Male  </span></td><td>1998                                          </td><td>New York City                                 </td></tr>
	<tr><td>4096714                                                           </td><td>2017-05-11 15:30:11                                               </td><td>2017-05-11 15:41:43                                               </td><td> 692                                                              </td><td>Lexington Ave &amp; E 63 St                                       </td><td><span style=white-space:pre-wrap>1 Ave &amp; E 78 St       </span></td><td>Subscriber                                                        </td><td><span style=white-space:pre-wrap>Male  </span>                    </td><td>1981                                                              </td><td>New York City                                                     </td></tr>
	<tr><td>2173887                                                            </td><td>2017-03-29 13:26:26                                                </td><td>2017-03-29 13:48:31                                                </td><td>1325                                                               </td><td><span style=white-space:pre-wrap>1 Pl &amp; Clinton St      </span></td><td><span style=white-space:pre-wrap>Henry St &amp; Degraw St  </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1987                                                               </td><td>New York City                                                      </td></tr>
	<tr><td>3945638                                                            </td><td>2017-05-08 19:47:18                                                </td><td>2017-05-08 19:59:01                                                </td><td> 703                                                               </td><td><span style=white-space:pre-wrap>Barrow St &amp; Hudson St  </span></td><td><span style=white-space:pre-wrap>W 20 St &amp; 8 Ave       </span> </td><td>Subscriber                                                         </td><td>Female                                                             </td><td>1986                                                               </td><td>New York City                                                      </td></tr>
	<tr><td>6208972                                                            </td><td>2017-06-21 07:49:16                                                </td><td>2017-06-21 07:54:46                                                </td><td> 329                                                               </td><td><span style=white-space:pre-wrap>1 Ave &amp; E 44 St        </span></td><td><span style=white-space:pre-wrap>E 53 St &amp; 3 Ave       </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1992                                                               </td><td>New York City                                                      </td></tr>
	<tr><td>1285652                                                            </td><td>2017-02-22 18:55:24                                                </td><td>2017-02-22 19:12:03                                                </td><td> 998                                                               </td><td><span style=white-space:pre-wrap>State St &amp; Smith St    </span></td><td><span style=white-space:pre-wrap>Bond St &amp; Fulton St   </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1986                                                               </td><td>New York City                                                      </td></tr>
</tbody>
</table>

</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Question-1">Question 1<a class="anchor-link" href="#Question-1">&#182;</a></h3><p><strong>What is the average travel time for users in different cities?</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Count of users in City</span>
<span class="n">total_city</span> <span class="o">=</span> <span class="nf">sort</span><span class="p">(</span><span class="nf">table</span><span class="p">(</span><span class="n">city</span><span class="o">$</span><span class="n">City</span><span class="p">))</span>
<span class="nf">print</span><span class="p">(</span><span class="n">total_city</span><span class="p">)</span>

<span class="c1"># percentage of users in City</span>
<span class="nf">round</span><span class="p">((</span><span class="n">total_city</span> <span class="o">/</span> <span class="nf">sum</span><span class="p">(</span><span class="n">total_city</span><span class="p">)</span> <span class="o">*</span> <span class="m">100</span><span class="p">),</span> <span class="n">digits</span> <span class="o">=</span> <span class="m">2</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>
      Chicago New York City    Washington 
         8630         54770         89051 
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_text output_subarea ">
<pre>
      Chicago New York City    Washington 
         5.66         35.93         58.41 </pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Visualizing data with ggplot to show clear picture</span>
<span class="nf">library</span><span class="p">(</span><span class="n">ggplot2</span><span class="p">)</span>
<span class="nf">ggplot</span><span class="p">(</span><span class="nf">aes</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="n">City</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">Trip.Duration</span><span class="p">),</span> <span class="n">data</span> <span class="o">=</span> <span class="n">city</span><span class="p">)</span> <span class="o">+</span>
    <span class="nf">geom_bar</span><span class="p">(</span><span class="n">position</span> <span class="o">=</span> <span class="s">&#39;dodge&#39;</span><span class="p">,</span> <span class="n">stat</span> <span class="o">=</span> <span class="s">&quot;summary&quot;</span><span class="p">,</span> <span class="n">fun.y</span> <span class="o">=</span> <span class="s">&quot;mean&quot;</span><span class="p">,</span> <span class="n">fill</span> <span class="o">=</span> <span class="s">&quot;blue&quot;</span><span class="p">,</span> <span class="n">colour</span><span class="o">=</span><span class="s">&quot;black&quot;</span><span class="p">)</span> <span class="o">+</span> 
    <span class="nf">ggtitle</span><span class="p">(</span><span class="s">&#39;The average travel time for users in different cities&#39;</span><span class="p">)</span> <span class="o">+</span>
    <span class="nf">labs</span><span class="p">(</span><span class="n">y</span> <span class="o">=</span> <span class="s">&#39;Average Trip Duration&#39;</span><span class="p">,</span> <span class="n">x</span> <span class="o">=</span> <span class="s">&#39;City&#39;</span><span class="p">)</span> <span class="o">+</span>
    <span class="nf">coord_flip</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>Warning message:
“Removed 2 rows containing non-finite values (stat_summary).”</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA0gAAANICAIAAAByhViMAAAACXBIWXMAABJ0AAASdAHeZh94
AAAgAElEQVR4nOzda3xU9b3o/zW5khAIYQNCCpWLChEQUFG0KoK1Clop2noBvCBWLcLGrcVq
0aNuRXmJFYtFWlFELS3i5QCi0q3V4uWotRQVqIiIG1G5ykVICAnJ/B/M/+RkJxBCIA78eL8f
JWtm1vrOmhXyYWbNJBaPxyMAAA5+KckeAACA/UPYAQAEQtgBAARC2AEABELYAQAEQtgBAARC
2AEABELYHZTGjRsXi8Xuv//+ZA9CPbr11ltjsdjvfve72t/k5ptvjsViv//97+tvqhp88MEH
J5xwQkZGRk5OzsqVK5MywwGi/h6IDz74IBaLnX766bvbUPVHIcjHZY97OLk/C5BEwu4Acscd
d8T2pEmTJskeM2RPPfXUnDlzkj3FXqgycF5e3uGHH96oUaOkDHPppZe+//77p5xyytVXX52d
nZ2UGQ4Q39kDUX1D1R+FA/Bx2fcftOp3/ID6WYAkivnLEweOGTNmzJgxo+Lb1atX//3vf2/e
vPnJJ59csbBhw4bTp08fN27cLbfcMn78+F/+8pfJmDRYrVq1Oueccx599NFkDxJFUXTrrbeO
HTv2oYceGjFixO6uc+AMvGPHjgYNGjRu3Pibb75JS0tL9jjB+uCDD3r06NG7d++//e1v1S+t
/igcmI9LfRy3B87PAiTXgfJzThRFF1988cUXX1zx7axZswYOHHjMMcfMmjUriVMdOlasWLFm
zZpkT7EXDqiBt2/fHkVRXl7egVMPh6Dqj8IB+LjUx3F7QP0sQHJ5KfYglpqa+q9//evcc8/N
y8vLysrq3r37008/XfkK8Xj80UcfPemkkxo1apSVlVVQUHDbbbcVFhbWvNpvv/32lltuKSgo
yMrKyszMPPLII0ePHv3tt98mLj399NNjsdgLL7xQ5VZz586NxWJnnHFGLTc9ZsyYWCw2Z86c
hx9++Hvf+17FS8w1bz3hiy++GDRoUPPmzbOzs3v27Pn8889v3LgxFoudeOKJdb7vP/3pTzt0
6BBF0WOPPRaLxU455ZQ6D7m/dlHNdjlwlfOKbrvttsT877zzzumnn96oUaPmzZtfccUVW7du
jcfjDz74YKdOnbKzs48++uh777238pP3ezvbT37yk7y8vCiKVq5cmThnYPny5VEUlZaW/va3
v+3Zs2ejRo0aNGhwxBFHjBgx4uuvv6644e72cBUjRoyIxWLTpk2rvPDdd9+NxWLnnntuxZJn
n322b9++TZs2zcjIyM/P79ev38svv1z5JnU+LPe45ip290AsWbJk4MCBLVq0aNCgQffu3f/8
5z/XsJLE/rz44oubNWuWnZ3dvXv3qVOn1rCh6o9Cly5ddvm41Hk/7PGGe7ynuzxud6m8vPzh
hx/u2bNnTk5Oo0aNzjjjjDfeeGOXd7w2Pwu1GT7a+wcaDkAHyv/hqIOvvvrqBz/4wQknnDBs
2LBPP/10zpw5l1xySbNmzSrS4bLLLvvjH//YqlWra665JjMz87XXXrv77rvnzp37xhtv7O7U
k9LS0nPPPffNN9887rjjRowYUVpaOm/evPvvv3/+/PnvvPNOamrqoEGD5s+f/9xzz/34xz+u
fMOZM2dGUXTppZfWctMZGRlRFM2fP//3v//9gAEDcnJyarP1KIq++eabU045ZdWqVT/4wQ9+
+MMffvnll4MHD7711lujKGrQoEHFPHt734cOHdqoUaNp06b16tXroosu+t73vlfnIffXLqrZ
LgeuIjH/u+++O3ny5LPOOuvyyy+fPXv2E088UV5enp+f/6c//emcc84pKiqaMWPGr3/969at
W9d5tmHDhp144om//vWv8/Ly/tf/+l9RFDVv3ry8vHzAgAEvv/xyp06dhg0b1rhx43/84x+T
Jk16/vnn33nnncMPP3x3e7hupkyZcvXVVzdv3vzCCy9s0aLFV199NWvWrHPOOeeJJ57Yx8Oy
NmuuWWK1CxcuvOyyy0488cQhQ4YsW7bsxRdfHDRo0GGHHda3b99d3mrTpk2nnnrqqlWrTjvt
tNNOO239+vVjxozp16/f7rZS/VFo1qzZqlWrqjwudd4Ptb9hDfe0NsdtwkUXXfTss88effTR
l19++ZYtW2bPnt27d+8nn3yy+j6v5Tr3OPy+P9BwQIhzoPrf//t/R1F0xhlnVL/o3nvvjaIo
IyPjqaeeqlh40003RVF02WWXJb5NPHt33HHHffvtt4kl5eXlibO1br755t1t9LnnnouiqFev
Xjt37kws2bFjR6dOnaIomjNnTjwe37hxY0ZGRl5eXklJScWtiouLc3Nzs7KyEtuqzabvueee
KIpyc3P/8pe/1H7r8Xh8zJgxURT97Gc/q7jV22+/nZWVFUVR79699+W+P/PMM1EUDRs2rGJJ
3YbcX7socU8feuih2g/8q1/9KoqiyZMnJ75NHCeZmZmvv/56YsnKlStTU1PT09M7der0zTff
JBYmTks699xz92Xvbdq0KYqiww8/vGLJI488EkXRSSedVFxcXLEwkeAXXnhhDXu4uuuuuy6K
oscff7zywnfeeSeKonPOOSfxbdeuXaMoWr58ecUVVq1a1ahRo169etX+fu1ynj2uubpdPhBV
fmATJ8hefvnlu1tJIsUuuuiiiiWrV69u2bJl5UO9yoaqPwrVl9R5P9TmhrW5p9WP2+oSz/D1
69ev4qds6dKl2dnZDRs2TDzfXOWO7/FnoTbD1+GBhgOQl2IPYr169RoyZEjFtwMHDoyiqOLj
DKZMmRJF0b333lvxFEssFrvrrrvS09OfeOKJ3a3z2GOPff755x966KHE02NRFGVkZAwYMCCK
oo8++iiKory8vLPOOmvTpk2vvfZaxa3mzZu3ZcuWAQMGVPzHd4+bjsViURQVFBT86Ec/qv3W
oyhKvMQ5evToiludfPLJlc9NrPN9r65uQ+6vXbS/nH766RWfjvH973+/a9eupaWlI0eObNq0
aWJh4tXMzz77LPHt/potceXbbrstMzOzYuHo0aMzMjJmzZqVOPdrl3u4bjZv3hyLxRo2bFix
pHXr1hs2bEj0Xy3v1y7n2eOaa6lnz56Vf2B/9rOfRVG0bNmy3V1/9uzZURRdf/31FUtatmz5
i1/8Yq82Wl2d90PtD4y9vafVPf7441EU/frXv674KevYsePYsWOvvfbadevW7dX9rf3w++uB
huQSdgexXr16Vf428Xt6y5YtiW/ffffdKIoqv6M2iqImTZp06dJl9erVX3zxxS7X2bZt24ED
Bx5//PFRFG3dunXNmjVr1qxJfERC4jdxFEWDBg2KoujZZ5+tuFWVFxlrv+mTTjppr7ZeXl6+
dOnSlJSU7t27V77hOeecU/nbut333dnbIaP9uov2XZV91bhx4yiKjjnmmCpLKobfL7PF4/EF
CxZUX0/jxo07duxYUlKyZMmSioVV9nDd/PjHP47H43369Jk6dWrFefSJVwYT6nxY7nHNtVTl
BzZx9lvFbq+ivLz8448/jqKoW7dulZdXPpG0buq8H2p/w726p7v09ttvR1F03HHHVV54/fXX
33///e3bt6/9eirUZvj99UBDcjnH7iCWOF2mQkpKShRF8Xg8iqLt27dv27YtiqLdnbT01Vdf
ff/739/lRbNmzbr//vsXLFhQXFy8yyucd955OTk5s2bN+v3vf5+amlpcXPzCCy+0aNEi8Z/7
vdp0lbuwx61v27atpKQkNzc3PT298vLECVsJ+3Lfd2lvh4z26y7ad82aNav8beLJmMoLE0v2
/cipbNu2bcXFxRkZGbm5uVUuSuzPDRs2VFmyjx588MGysrKpU6cOGzYsiqKjjz763HPPvfba
a9u1axft22FZ85prL/EqaoXKu726xKHeoEGDxGkGFf7t3/5trzZaRZ33w17dcK/uaXWFhYWF
hYXV73ud1XL4/fVAQ3IJuzAl/iWNxWKJ03Sqq/Ivb4VHHnnkmmuuadSo0bXXXnvCCSfk5uam
pKTMmjXrD3/4Q8V1srOzBwwYMH369Pnz5/ft2/ell17aunXr0KFDE5+nsFebrtJne9x64ndD
YhPV7+8+3vfd2dsho/26i75j+2u2Gn6Xl5eXR//zIauyh+smPT3997///e233z5nzpyXX375
tddeu++++x588MGnnnrqwgsv3JfDsuY17/vku5TYddV3YFlZ2b6sts774bs8aBP/Ry0tLY3H
49V/2OuglsMn5YGG/U7YhalBgwa5ublbtmy57rrr9urpkP/8z/+Momju3LmnnXZaxcLqp5gM
GjRo+vTpzz33XN++fROnLVe8yFjnTddm6zk5OampqVu3bi0rK6s4+SaKolWrVlV8vS8D7Jch
E+ppF9W3/TVbTk5OdnZ2UVHR5s2bq3yIyfr166O9fJZul5m4evXq6tdMvOfxmmuuKS4unjZt
2siRI6+55poBAwbs+/3a3Zorn0G4HyUO9R07dmzfvr3yE1f7+Gltdd4P3+VBm5WV1ahRo61b
t37zzTdVnm+um70a/jt+oGG/c45dsBLn4lT+5KeEjRs37u4mO3bs+Oqrr3JycionSzwenzdv
XpVr/uhHP2rWrNkLL7ywffv2F154oVOnTolzzuq86VpuPTU1tV27dmVlZUuXLq182yoT1m2A
2kjuLvpu7K/ZEvc3cbJU5ZV88sknWVlZnTt3rv2qEh9kk3iDZ4X333+/8rcrV66snHoNGjS4
9tprTz755M2bN69YsSLah/u1xzXXh9TU1COPPDKq9LahhLfeemsf11zn/fBdHrSJg+fVV1+t
vPDee+/94Q9/+H/+z/+pwwprM3xSHmjY74RdsBKnidxxxx2JJ0gS3nzzzcMOOyzxJrXqMjMz
mzZtum3btoonwOLx+H/+538mzizevHlzxTXT0tJ+9rOfrVq1asKECYWFhZXfAVe3Tdd+62ed
dVYURQ899FDFDf/+97//6U9/2vcBEvXwzTff7O4KtR8yqp9dVIeB62C/zFaxnnvuuaekpKRi
4T333LNz587Bgwfv1fMfifPlE58mk1jy8ccfJ97nmPDhhx+2bdt2yJAhlbe1devWFStWpKam
tmjRos73qzZrrif9+/ePouiBBx6oWPL5558/9thj+7jaOj++++vAqM1xe/nll0dRdP/991d8
gPB///d/jx8//p133ikoKKjDOvc4fBIfaNi/vBQbrAsvvHDWrFl//vOfe/TocdFFFzVq1Gjx
4sVz5szJysqq/FkhVVxxxRUPPPDAGWeckfiHde7cuZs2bXriiSfOOuusGTNmtGnTZvDgwa1b
t46iaNCgQZMnTx43blwsFhs8ePC+b7qWW//lL3/5xz/+8Q9/+MPKlStPOOGElStXPv/887fe
emviY6v2ZYCCgoJYLPbiiy8OGzYsIyNj8uTJB+AuqsPAe2u/zBZF0aWXXvr888/Pnj37uOOO
69evX3p6+nvvvffXv/71qKOOGjdu3F6NdMEFF9x8883z58//wQ9+0KtXr9WrV8+dO/f2228f
PXp04oy9bt26DRo06E9/+lNBQUG/fv3+7d/+bcOGDS+++OKXX345atSoxBsO6na/arPmenLj
jTc++eSTM2fOXLFixUknnbR+/fqXX3755z//+f33378vq63z47u/DozaHLeXXnrps88+O3fu
3M6dO/fr16+wsHDWrFlbt26dMmVK4j22e7vOPQ6fxAca9rPv9FPz2Bt7/IDi8ePHV1746aef
RlHUrVu3iiVlZWVTpkxJ/AmdtLS01q1bX3bZZR9//HENG92+ffuYMWM6dOiQmZnZpk2b4cOH
b9iwIR6PX3HFFQ0bNmzZsuVHH32UuGZ5eXnbtm2jKDr11FOrr2ePm97lXajl1hcuXHjmmWc2
atSocePGvXv3fu211xYtWhRF0emnn74v9z0ej48bN65Zs2aZmZnHHnvsPg6577tojx9QXH3g
XX4ubpX5e/fuHUVR5Q0lPoei8mfY1mHvVf8g3Hg8Xlpa+uCDDx577LHZ2dmZmZmdOnW65ZZb
Nm3aVHGFXU64S4sWLerbt292dnZOTs6JJ544a9asxFMvFQ96WVnZpEmTTj755GbNmqWmpubm
5p566qlTp04tLy+v/f3a5Ty1WXMVtXkgqv/AVvfxxx8PGDCgSZMmDRo06Nq165QpUxJPSp14
4om73FBtPqC4zvuhzjesfk+rHLe7VFpa+pvf/OaYY47Jyspq2LDhaaed9tprr1VcWuWOV19n
9Svscfg6PNBwAIrFa/0WdDhgvffee7169TrnnHPmzp2b7FkAIGmcY8dBZu3atS+99FKVM8oX
LlwYRZGPmwLgECfsOMi88sor55xzzi9+8YvS0tLEki1btvzmN7+J/u+fxgKAQ5aXYjnIlJSU
nHHGGW+99Vbnzp379+9fVFQ0e/bsL7/8cuDAgc8//3yypwOAZBJ2HHy2bt06YcKEmTNnrly5
sqysrGPHjoMHD77++usTf9cBAA5Zwg4AIBDOsQMACISwAwAIhLADAAiEsAMACISwAwAIhLAD
AAiEsAMACISwAwAIhE/qP4Bs2bKlntackpKSlZVVWlpaUlJST5sIUoMGDXbs2OFDvGvPkVY3
WVlZxcXFjrTaS01NbdCggSNtbznS9tYBe6Tl5ubu7iJhdwCp+Kv2+11aWlpaWtrOnTvrbxNB
ys7O3rlzZ3l5ebIHOWikp6enpaWVlpY60vZKw4YNHWl7y5FWBw0bNiwtLRV2tReLxdLS0kpK
Sg6iI81LsQAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAA
gRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYA
AIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2
AACBSEv2AHwXSkpKbr755g0bNpSWliZ7loNJRkZGaWlpPB5P9iAHjZSUlIyMjJ07d+7cuTPZ
sxxMHGl7y5FWNxkZGSUlJcme4mBS5yOtoKDgqquuqqepahbzT8mBY8OGDfW05iVLlpx++un1
tHIAoLL09PSvv/66/tbfrFmz3V3kGbtDQnl5eRRFUXRpFN2R3EkAIHQDy8uXJGvbwu6QkhtF
7ZM9AwCELTOJ2/bmCQCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsA
gEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7
AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAI
OwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBA
CDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCA
QAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsA
gEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7
AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAI
OwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBA
CDsAgEAcQmH3k5/85N13362ysKys7Lzzzvvwww+TMhIAwH50IIbdDTfc8Nvf/rbykquvvvq2
226rvORXv/rVb37zm33fVkpKytixYzt06FCH23700UfLly/f9xkAAPaLAzHsevbs+c9//jMe
jye+XbNmzebNmz/++OMdO3YklhQVFS1btqxnz577vq1YLNa1a9ecnJw63HbWrFmffvrpvs8A
ALBfpCV7gF3o2bPnn//8588//7x9+/ZRFC1YsODoo49eu3btokWLjj/++CiKFi5cGI/Hjz32
2JUrVz722GPLly8vLy/v2LHjtdde26pVqyiK/vrXvz733HPr1q3Lzs4+6aSThg0blpGREUXR
1q1bb7/99sWLFzds2HDo0KF9+vQpKysbOHDgXXfddcwxxwwYMOCXv/zlX//61w0bNhQXFw8e
PLhv375RFH3++ecTJkz4+uuv27Rpc+WVV44ZM2bixIlTpkxZvHjxhx9++F//9V8TJkzYvHlz
YklhYWH79u2HDh1aUFAQj8d3t04AgP3uQHzGrkOHDk2bNl2wYEHi2wULFnTp0qVLly4VSxYu
XFhQUJCTkzNu3LimTZtOnTp16tSpWVlZEyZMiKJozZo1EydOvOaaa2bOnHnfffd98sknc+bM
SdzwhRdeuPjii//4xz+eeeaZDz/8cHFxccVGY7FYSkrKrFmzbrjhhkmTJl188cWTJ08uLi6O
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
SURBVD3LwSQnJ6eoqKi8vDzZgxw00tLScnJyduzYsX379mTPcjBp1KhRYWGhI632HGl106hR
o23btsXj8WQPctBIT09v2LBhcXFxcXHxXt2wVatW9TTSHgm7Q0X79u3z8/O3bduW7EEOJrm5
uVu3bvXrtvbS09Nzc3O3b99eWFiY7FkOJk2aNPn2228dabXnSKubJk2abNmyRdjVXkZGRuPG
jYuKig6ip0W8eQIAIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQ
wg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBBpyR6A
78jixYu/+OKL7du3J3uQg0nDhg23b99eXl6e7EEOGmlpaQ0bNtyxY0dxcXGyZzmY5OTkFBUV
OdJq78A/0mKx2NFHH92sWbNkD8IhR9gdElasWNGzZ0+/NgC+M126dHn99deTPQWHHGF3SNiy
ZUt5eXkUHRtFZyZ7FoBDwaTNmzcnewYORcLukHJyFI1L9gwAh4Knkj0AhyhvngAACISwAwAI
hLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMA
CISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLAD
AAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISw
AwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiE
sAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAI
hLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMA
CISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLAD
AAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIRK3CrrS0tL7nAABg
H9Uq7PLz80eNGvXPf/6zvqcBAKDOahV2Xbp0+d3vfnfcccd17dp1/Pjxq1evru+xAADYW7UK
u9dff/2rr7566KGH8vLyfvWrX7Vp06Zfv34zZszYvn17fc8HAEAt1fbNEy1bthwxYsQbb7zx
5Zdf/uY3v/nmm28uueSSli1b/vznP//73/9eryMCAFAbe/2u2MT5do8//vigQYO+/fbbRx99
9MQTT/zBD37wj3/8oz7mAwCglvYu7NauXfvAAw9069atS5cuTz/99DnnnPPcc8/NmTOnpKSk
V69ef/nLX+ppSgAA9iitNlcqKSl54YUXnnjiiZdffnnnzp0dO3a89957L7/88latWiWucPbZ
Z5933nnXXXfd8uXL63NaAAB2q1Zh16pVq40bN+bk5Fx66aVXXnnlKaecUuUK6enp11577cCB
A+thQgAAaqVWYXf00UcPHTr0oosuatiw4e6uc+yxxz766KP7bzAAAPZOrc6x2759+0knnVS9
6p577rmjjz468XWbNm2uvPLK/TwdAAC1VquwW7BgQWFhYZWFO3fuXLJkyWeffVYPUyVBWVnZ
eeedty9/XSOxhg8//HA/TgUAUHt7CLtYLBaLxaIo6tmzZ+x/Sk9Pv/3227t06bLHbdxwww0/
/elPv/7668oLR4wY8fLLL+/L6JW9+eab559//sqVKysvfO211y644IJVq1btr61EUbRhw4bJ
kydfddVV559//mWXXXb33XcvWbIkcVFKSsrYsWM7dOgQRdFHH33kfSQAwHdsD+fYffDBB/Pn
zx81atSAAQOaNWtW+aJYLJafn//zn/+8NpvJzMycNGnS2LFj6z5pjU499dS33nrroYceGj9+
fKJEt2zZ8thjjw0aNKhNmzb7aytffvnlzTff3KRJk2HDhrVu3Xrz5s2vvPLKmDFjbrrpppNP
PjkWi3Xt2jVxzVmzZvXs2fOII47YX5sGANijPYRdt27dunXr9tJLL40fP/7II4+s82YGDBgw
e/bsV1999Yc//GH1Szdt2vToo48uXry4qKjoiCOOuOqqqzp06DBs2LDBgwf37ds3iqKnnnrq
mWeeefTRR1u0aBFF0S233NKjR48LL7yw8kp+8YtfXHfddXPmzBkwYEAURVOmTGnVqlXijbqb
N2+eMmXK4sWLCwsL27dvP3To0IKCgvLy8p/85CcjRoyYOXNm165dR4wYUbGqsrKyO+64Iy0t
7dZbb01NTa1YPnny5Nzc3AceeCAjIyOKojZt2nTt2rVZs2YrV648+eSTy8rKBg4ceNddd82c
OXPx4sUffvjhf/3Xf6Wnp7dr1+4Xv/hFYg2ffPLJTTfdNGXKlMQdAQDYj2r1rth58+bt42Ya
Nmw4dOjQqVOn9uzZMzc3t8qlY8eOPeyww373u99lZmbOnDnzjjvueOyxx7p3775kyZJE2H30
0Udt2rRZsmRJixYtSkpKli1bNmzYsCoradKkyc9//vNJkyb16tXrq6++eueddx588MGUlJQo
iu6+++6cnJyJEyc2aNBg+vTpd9555yOPPNK4ceOUlJR58+bdcsst+fn5lVf10EMP7dixo0rV
bdmyZdGiRaNGjUpUXYXLLrus+t256qqrLrjggn79+r366quPPfbYsGHDErd68803u3TpUlF1
X3/99ZYtWxJfp6am1l/tVb4jAHw30tJq9Uv2OxOLxdLS0uLxeLIHOWgkKiIlJeWAeihrfgRr
GrRTp06XX375Lbfc0qlTpxqutnTp0trM8cMf/vBvf/vbI488Mnr06MrLP/vss2XLlo0ZM6ZR
o0ZRFA0ePPjFF1987733unfvPn369CiKiouLV65cOWTIkMWLF/fp02fp0qVZWVmJU9mqOP30
0996662JEyeuXbu24kXYFStWLFu2bNKkSYmgHDJkyLx58xYsWNCnT58oinr16pVYVVlZWWIl
06dP//TTT8eNG5eZmVl55WvXro2i6PDDD6/Nna1wyimnTJky5d133z3ttNPi8fjbb79dOQQf
fvjhimjOy8t75ZVX9mrltZednV1PawZgl1JSUpo0aZLsKaqq/twKe9SgQYMGDRoke4r/p6JY
dqmmsGvSpElWVlbii/0yynXXXTdy5Mh//OMfxx9/fMXCxJsqLr/88srXXLt27VlnnXX//fdv
2rTps88+a9++fbdu3V588cUoihYtWtS9e/fEiXTVDR8+fPjw4fn5+RWflrx69epYLNa6devE
txkZGc2bN1+3bl3i24o/npHwyiuvvP322/fcc0+iMqureW9W16BBg9NOO+3VV1897bTT/vWv
fxUVFZ188skVl5522mmHHXZY4uusrKzt27fv1cprr6SkpJ7WDMAuxePx+vtXvW4yMzN37NiR
7CkOJqmpqRkZGTt37iwtLU32LP9PeXl5DZ8rXFPYvfvuu1W+2EetWrW6+OKLJ0+ePGnSpIoy
S7xG+eyzz1Z5iTOKog4dOvzrX//65JNPunbt+v3vf3/btm0bN25ctGjRj370o91tomnTpvn5
+QUFBYmnT3cpHo/v3Lkz8XV6enrliz799NMePXpMnTp1/PjxVV6+zM/Pj8ViK1as6NixY+Xl
5eXlFe8d3qUzzzxz9OjRGzdufPPNN0899dTKTwT+6Ec/qnxfNmzYsLuV7CM/yQDfsXg8Xv2T
wpIrPT29qKjIS7G1l5GRkZGRUVJSUlRUlOxZ/ocawm7Pn2O3Zs2a9evXV1n47rvvbty4sQ6j
DBw4MDs7+6mnnqrIpsT5bZ9//nnlLSa+6N69++LFixcvXtylS5dYLFZQUPDPf/5z2bJlPXr0
qP0W8/Pz4/F4xYeeFBcXr1u3rsoTdRWuvfba0aNHb968+cknn6xyUU5OTo8ePZ599tkqj+70
6dNvu+22GgY46qijDj/88L/97W9vv/32GWecUfvJAQD2yh7Cbu7cuZ06dUqc61bZFVdc0alT
pw8++GBvt5eamjpy5MiXXnrpm2++SSxp06bNMccc89hjj61fv76srOzll18eOXJkohp79Ojx
wQcffPHFFwUFBVEUde7cefbs2a1bt87Ly6v9Ftu1a9epU6fHH39869atxcXF06ZNy8rK6tWr
1y6vnJKSkpOTc+ONN86ZM2fhwoVVLr366qtLSkpGjRr1xhtvrFq1avHixQ8++ODs2bMvuOCC
KtfMzMxcvXp1xf/VzjzzzJkzZzZs2DBxRwAA6kNNYffpp59efPHFOTk5xxxzTJWLpk6dmpqa
2r9//02bNu3tJo866qj+/ftXvBs0iqIbb7yxWbNmI0eOHDRo0Ouvv37HHXc0bdo0iqKCgoJv
vvnmiCOOSLxK27lz55UrV+7V03UJo0ePTktLGz58+FVXXbVu3bpx48bV/GaCzp07X3DBBRMm
TKg8ZBRF+fn5EyZM6N69+7Rp00aNGjV+/PgdO3bcd9991Uc6++yzX3rppZEjRya+7dOnT0lJ
yS4/6gUAYH+J1fBa+6hRoyZPnvzRRx/t8l2xH3zwwfHHH3/77bfX/EIkURStXLnyxhtvfPTR
R2t+G0r9nWO3aNGivn37RtGIKHqonjYBQCXfa906pforP8nVpEmTLVu2OMeu9jIyMho3blxU
VHSgnWNX5W9GVFbTM3Z/+ctfLrjggt191kn37t3PPffcP/3pT/s6XdDKy8vXrVs3ceLEfv36
HYDvewcAQlJT2H355ZcVfyNrl4499tjKb3qguqeffnrEiBFt2rS59NJLkz0LABC4PXyScg0f
GhJFUXl5efXPKKGySy655JJLLkn2FADAIaGmbmvXrt37779fwxXmz5/frl27/T0SAAB1UVPY
9e/ff/bs2QsWLNjlpXPnzv3b3/523nnn1c9gAADsnZrC7oYbbsjNzT377LNnzJhR+U9pbd++
/cEHH7zwwgubN2/+H//xH/U/JAAAe1bTOXaHHXbY7NmzBw4ceMkll4wYMaJbt26NGjXauHHj
woULt23b1rJlyzlz5iQ+cA4AgKTbw5snTjnllMWLF//2t7+dPXv2/Pnzy8rK0tLSjj766PPP
P3/kyJGqDgDgwLGHsIui6LDDDrvnnnvuueeeeDxeVFSUnZ1dwx+8BwAgWfYcdhVisVjDhg3r
bxQAAPZFTW+eAADgICLsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh
7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAAC
IewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAA
AiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewA
AAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHs
AAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh
7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAAC
IewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAA
AiHsAAACIewAAAKRluwB+C6ti6IFyZ4B4FBQGkWZyZ6BQ5GwOySkpqZGURRFM6NoZpJHATg0
pKR8P9kjcCgSdoeEgoKCW2+9dfXq1aWlpcme5WCSkZFRWloaj8eTPchBIyUlJSMjY+fOnTt3
7kz2LAcTR9reOvCPtNTU1FNPPTXZU3AoEnaHhPT09Lvuuqu4uHjbtm3JnuVgkpubu3Xr1vLy
8mQPctBIT0/Pzc3dvn17YWFhsmc5mDRp0uTbb791pNWeIw12x5snAAACIewAAAIh7AAAAiHs
AAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh
7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAKRluwB+C5s2bLlrLPOWr9+fXl5ebJnOZik
pKTE4/F4PJ7sQQ4asVgssdMcaXvFkba3Qj3SWrRo8eyzz2ZnZyd7EA5iwu6QsGLFir///e9R
lBlF/r0AODAVrVy5ctWqVR07dkz2JBzEhN0h5edR9FCyZwBgl4ZF0dRkz8BBzzl2AACBEHYA
AIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2
AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQ
dgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACB
EHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAA
gRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYA
AIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2
AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQ
dgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACB
EHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBOHTD7ic/+cm7
775bZWFZWdl555334YcfJmUkAIB9kZbsAerRhg0bnnnmmQULFmzcuDEnJ+eoo44aOHBg586d
a7hJSkrK2LFj27Vr950NCQCwvwQbdl9++eXNN9/cpEmTYcOGtW7devPmza+88sqYMWNuuumm
k08+eXe3isViXbt2/S7nBADYX4INu8mTJ+fm5j7wwAMZGRlRFLVp06Zr167NmjVbuXJlRdht
3br19ttvX7x4ccOGDYcOHdqnT5+ysrKBAwfedddd3bp127BhwyOPPPLBBx80aNDgpJNOuvLK
KzMzM1euXPnYY48tX768vLy8Y8eO1157batWraIo+vzzzydMmPD111+3adPmyiuvHDNmzMSJ
E9u2bbt58+YpU6YsXry4sLCwffv2Q4cOLSgoSOZ+AQDCFeY5dlu2bFm0aNH555+fqLoKl112
2SWXXFLx7QsvvHDxxRf/8Y9/PPPMMx9++OHi4uLKV7733ntTU1P/8Ic/jBs3bsmSJdOmTYui
aNy4cU2bNp06derUqVOzsrImTJgQRVE8Hr/rrrvatm375JNPjho16vHHH4+iKBaLRVF09913
FxYWTpw4cfr06Z06dbrzzju//fbb+t8BAMChKMxn7NauXRtF0eGHH17z1Xr37p14/uzMM898
5pln1q5d27p168RFK1as+PTTT0ePHp2Xl5eXl3fDDTds3LgxiqLx48enp6dnZmYmbn7ffffF
4/FPPvlkw4YNgwcPzs7Obtu2bf/+/SdOnJhYybJlyyZNmpSbmxtF0ZAhQ+bNm7dgwYI+ffok
tvLAAw/Mnz8/8XVubm6iCOtDw4YN62nNAOxHjRs3zsvLq6eVp6SkNGnSpJ5WHqTEczRZWVmJ
3/sHiPLy8houDTPsEsrKymq+Qn5+fuKLxANWWlpacdHq1atjsdhhhx2W+LZ9+/bt27ePomjF
ihVPP/30qlWrEtcvKysrLy9fv359SkpKixYtElfu0KFD5ZVUxGJGRkbz5s3XrVtXsZXt27dv
3bo18XVqampKSn09gZo4NAE4wKWkpNTr74L6W3nYDqj9Fo/Ha7g0zLDLz8+PxWIrVqzo2LFj
5eXl5eWxWKyicmrIncRF8Xi88nVWr1595513XnLJJbfffntGRsZ77703duzYxNVSU1MrrlnD
wx+Px3fu3Fnx7ZgxY8aMGVPx7YYNG/bqbtbetm3b6mnNAOxHmzdv/uabb+pp5U2aNNmyZUvN
WUBlGRkZjRs33r59e1FRUbJn+R+aNWu2u4sOoALdj3Jycnr06PHss89WeSSmT59+22231WYN
rVq1isfjiWfmoihatmzZiy++uHz58sS7KxKn7n3yySeJS/Py8kpLSxOv1UZR9NlnnyW+yM/P
r7yS4uLidevWJd5sAQCw34UZdlEUXX311SUlJaNGjXrjjTdWrVq1ePHiBx98cPbs2RdccEFt
bt6uXbujjjpq6tSpa9eu/eqrrx5++OEvvviiRYsW5eXlS5cuLS0tfeONNz7++OMoijZu3FhQ
UNC4ceOZM2eWlJSsWrVq3rx5FSvp1KnT448/vnXr1uLi4mnTpmVlZfXq1ase7zYAcAgLNuzy
8/MnTJjQvXv3adOmjRo1avz48Tt27Ljvvvt69OhRyzXcdtttGRkZI0aMuPnmm4888sihQ4d2
7Njx/PPPHzt27BVXXPHhhx+OGTPmiCOO+Pd///eNGzfefPPNS5YsGTJkyKRJkwYPHhz93xdk
R48enZaWNnz48KuuumrdunXjxo3Lzs6ux7sNABzCYl5r3y/Kysri8XhaWloURUuXLr3ppptm
zJixtw1Xf+fYLVq0qG/fvlE0IooeqqdNALBvhkXR1LfeeqvK2eH7kXPs9lbiHLuioiLn2B1a
4vH48OHDJ02aVFhYuGnTphkzZnTu3NkzcwDAd0zY7QexWOyWW25Zv3790KFDR44cmZmZeeON
NyZ7KADgkBPmx51899q2bXv33XcnewoA4JDmGTsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7
AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAI
OwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBA
CDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCA
QAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsA
gEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7
AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAI
OwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBA
CDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCA
QAg7AIBACDsAgEAIOwCAQKQlewC+SzOj6J1kzwDALq1M9gCEQNgdElq3bt22bdvNmzdH0WfJ
nuVgEovF4vF4sqc4yNhpdWCn1UGQOy0vr13Lli2TPQUHN2F3SGjevPnnn39eXFy8bdu2ZM9y
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"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="n">my.summary</span> <span class="o">&lt;-</span> <span class="nf">with</span><span class="p">(</span><span class="n">city</span><span class="p">,</span> <span class="nf">aggregate</span><span class="p">(</span><span class="nf">list</span><span class="p">(</span><span class="n">Trip.Duration</span><span class="p">),</span> <span class="n">by</span> <span class="o">=</span> <span class="nf">list</span><span class="p">(</span><span class="n">City</span><span class="p">),</span> 
                   <span class="n">FUN</span> <span class="o">=</span> <span class="nf">function</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="p">{</span> <span class="n">mon.mean</span> <span class="o">=</span> <span class="nf">mean</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">na.rm</span> <span class="o">=</span> <span class="kc">TRUE</span><span class="p">)</span> <span class="p">}</span> <span class="p">))</span>

<span class="nf">colnames</span><span class="p">(</span><span class="n">my.summary</span><span class="p">)</span> <span class="o">&lt;-</span> <span class="nf">c</span><span class="p">(</span><span class="s">&#39;City&#39;</span><span class="p">,</span> <span class="s">&#39;Average.Trip.Duration&#39;</span><span class="p">)</span>
<span class="n">my.summary</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<table>
<thead><tr><th scope=col>City</th><th scope=col>Average.Trip.Duration</th></tr></thead>
<tbody>
	<tr><td>Chicago      </td><td> 937.1728    </td></tr>
	<tr><td>New York City</td><td> 903.6147    </td></tr>
	<tr><td>Washington   </td><td>1233.9533    </td></tr>
</tbody>
</table>

</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>**
Washington(1233.9533) recorded highest in average trip duration, this can be attributed to being the city with highest number of users.</p>
<p>The percentage total of number of user from each city is; Washingto (58.41%), New york city (35.93%) and Chicago (5.66%).</p>
<p>Although the number of users in Chicago is comparatively less among all, however, it recorded higher average trip duration than New york city**</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Question-2">Question 2<a class="anchor-link" href="#Question-2">&#182;</a></h3><p><strong>What is the most common month? (Most frequent time of travel)</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># formatting of date columns</span>
<span class="nf">library</span><span class="p">(</span><span class="n">lubridate</span><span class="p">)</span>
<span class="n">city</span><span class="o">$</span><span class="n">Start.Time</span> <span class="o">&lt;-</span> <span class="nf">ymd_hms</span><span class="p">(</span><span class="n">city</span><span class="o">$</span><span class="n">Start.Time</span><span class="p">)</span>
<span class="n">city</span><span class="o">$</span><span class="n">End.Time</span> <span class="o">&lt;-</span> <span class="nf">ymd_hms</span><span class="p">(</span><span class="n">city</span><span class="o">$</span><span class="n">End.Time</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>
Attaching package: ‘lubridate’

The following object is masked from ‘package:base’:

    date

Warning message:
“ 1 failed to parse.”</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Creating new column &#39;Month&#39; extracting from Start.Time</span>
<span class="n">city</span><span class="o">$</span><span class="n">Month</span> <span class="o">&lt;-</span> <span class="nf">month</span><span class="p">(</span><span class="n">city</span><span class="o">$</span><span class="n">Start.Time</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Visualizing data with ggplot</span>
<span class="nf">ggplot</span><span class="p">(</span><span class="nf">aes</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="n">Month</span><span class="p">,</span> <span class="n">fill</span> <span class="o">=</span> <span class="n">City</span><span class="p">),</span> <span class="n">data</span> <span class="o">=</span> <span class="n">city</span><span class="p">)</span> <span class="o">+</span>
    <span class="nf">geom_bar</span><span class="p">(</span><span class="n">position</span> <span class="o">=</span> <span class="s">&#39;dodge&#39;</span><span class="p">,</span> <span class="n">colour</span><span class="o">=</span><span class="s">&quot;black&quot;</span><span class="p">)</span> <span class="o">+</span>
    <span class="nf">scale_x_continuous</span><span class="p">(</span><span class="n">breaks</span> <span class="o">=</span> <span class="nf">c</span><span class="p">(</span><span class="m">1</span><span class="p">,</span><span class="m">2</span><span class="p">,</span><span class="m">3</span><span class="p">,</span><span class="m">4</span><span class="p">,</span><span class="m">5</span><span class="p">,</span><span class="m">6</span><span class="p">),</span> <span class="n">labels</span> <span class="o">=</span> <span class="nf">c</span><span class="p">(</span><span class="s">&#39;Jan&#39;</span><span class="p">,</span> <span class="s">&#39;Feb&#39;</span><span class="p">,</span> <span class="s">&#39;Mar&#39;</span><span class="p">,</span> <span class="s">&#39;Apr&#39;</span><span class="p">,</span> <span class="s">&#39;May&#39;</span><span class="p">,</span> <span class="s">&#39;Jun&#39;</span><span class="p">))</span> <span class="o">+</span>
    <span class="nf">ggtitle</span><span class="p">(</span><span class="s">&#39;Number of Rides in different Months&#39;</span><span class="p">)</span> <span class="o">+</span>
    <span class="nf">labs</span><span class="p">(</span><span class="n">y</span> <span class="o">=</span> <span class="s">&#39;Number of Rides&#39;</span><span class="p">,</span> <span class="n">x</span> <span class="o">=</span> <span class="s">&#39;Month&#39;</span><span class="p">)</span> <span class="o">+</span>
    <span class="nf">scale_fill_manual</span><span class="p">(</span><span class="s">&quot;legend&quot;</span><span class="p">,</span> <span class="n">values</span> <span class="o">=</span> <span class="nf">c</span><span class="p">(</span><span class="s">&quot;Chicago&quot;</span> <span class="o">=</span> <span class="s">&quot;black&quot;</span><span class="p">,</span> <span class="s">&quot;New York City&quot;</span> <span class="o">=</span> <span class="s">&quot;orange&quot;</span><span class="p">,</span> <span class="s">&quot;Washington&quot;</span> <span class="o">=</span> <span class="s">&quot;blue&quot;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>Warning message:
“Removed 1 rows containing non-finite values (stat_count).”</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA0gAAANICAIAAAByhViMAAAACXBIWXMAABJ0AAASdAHeZh94
AAAgAElEQVR4nOzdd3gU5f738Xv7ZtMIJEAiLRQp0iJKL6Eq5QiIIKjUIE1UVKqA9HIQIaAU
CQdE0IAgAupBqQJKEThUETChhSAlEFJI2/b8Mc/Z354Ekk12N7sM79fl5bVz78w935mdzH6Y
2ZlRWK1WAQAAgMef0tMFAAAAwDUIdgAAADJBsAMAAJAJgh0AAIBMEOwAAABkgmAHAAAgEwQ7
AAAAmSDYedKkSZMUCsVnn33m6UL+x8mTJxs2bKjVav38/K5evep8h+PHj1coFMuXL89/pgqF
IjIy0vnZOVlJ0eSqP++M8q5Vl6/nJ9DcuXMVCsX8+fM9XQgAeIsnMdhJ38EKhWLq1KkPHSEy
MlKhUNy8ebN46/IWffv2PXr0aPPmzYcMGWIwGPKOYFuBuRgMhho1arz11ltxcXH24wcFBVWs
WNHf37+4luCRiq2SvDPKu1YLXM/Fb+3atdu2bctnBNtH361bt0eN88MPP0jjTJo0qfgrBIAn
nNrTBXjSnDlzevXqVatWLU8X4kWys7PPnj0bEBCwY8cOtTq/zcPPz69z5862QavVeuvWrdOn
Ty9dunT16tXbtm1r166d9Na4cePGjRvn3rodU2yV5JpR3rXq+HouTmPHju3cufNLL72U/2gK
heLHH3+8fft26dKl8767Zs0ahULhpkfaOFghADyxnsQjdpK6devm5OS8+eabPFTNXmZmphAi
KCiowLRRpkyZ9XY2bNjwyy+/XL9+ffjw4ZmZmVFRURaLpVhKfgzkXauOr+dic+nSJQePUter
V89kMq1bty7vW8nJyd9///0zzzzj6uqEKEyFAPDEenKDXfPmzXv16nXw4MECf3E1cuRIhULx
xRdf2DcePnxYoVB06dJFGpw8ebJCodi2bduhQ4ciIyP9/f1DQkIGDBiQlpZmtVqjo6Nr1Khh
MBhq1ao1Z86cXFFSqVTu3bu3VatWAQEBfn5+zZs337Vrl/0IVqt15cqVTZo08ff39/HxqVmz
5uTJkx88eGAbYeLEidLcly5d+tRTT5UoUeJRy2I0GhctWvT888/7+/vr9fqqVauOHDnyxo0b
0rvdunULCgoSQly9elU6m5brpGqBDAbDZ599FhAQcO3atTNnzkiNeX9wdvXq1d69ewcHBxsM
hvr1669atSpvVwUutRBi06ZNbdq0KVmypFarDQsL69ix4/bt2/MpL1cltk/tjz/+6N69e+nS
pfV6ff369WNjY/NfzALrt59R3rVau3bth67nIn/QBU5Y4JK+8sorVapUEUL861//UigUzZs3
z2fxGzRoEBISsnr16rxvrV+/Pjs7u3379rna89/wnKxQpVKdO3euS5cuQUFBPj4+9evX37Bh
g/3cC7udAMDjy1uOFhS/rKysxYsX79y5c/z48S+99NJTTz3lTG9arVYIcfjw4WXLlr3wwgv9
+/ffunXrmjVrLBZLWFjY119/3blz54yMjPXr13/44YflypXr27evbdqTJ0++//77rVu3fvPN
N+Pj47dt29axY8ddu3a1atVKGqFfv37r1q0LDQ0dOnSoTqfbs2fPzJkzf/jhh/3790u/4pLm
vm/fvuXLl3ft2tXPz++hRVoslq5du27fvr1GjRpRUVEBAQHHjh1bsmTJ5s2bDx06VLFixaio
qEaNGn344YdBQUEfffSRECIkJKSwq0KpVJYuXTo1NTU7O/uhIyQnJ7do0SIhIaFly5YtW7a8
c+fOxIkTO3bsmGu0Apc6JiZmyJAhISEhvXr1Kl26dGJi4pYtWzp37rxmzRr71ZsPab2dOHGi
X79+jRo1euONNy5evPjjjz++9tprZcqUadOmjTP12+Rdq8HBwQkJCXnXc5E/aAcnzGdJBw4c
6O/v/8UXXzRu3PjVV1/N/8/BarX26NFj+fLlx44de+655+zf+uKLL8qUKdOkSZOFCxfaGgvc
8JysMDExsVmzZg0bNoyKivrrr7+2bdvWp0+f4ODgtm3bCldsJwDwOLE+eU6cOCGEGDBggNVq
XbFihRCiW7du9iNIiervv/+WBt966y0hxOrVq+3HOXTokBCic+fO0uCcOXOEEDqdbu/evVLL
1atXVSqVRqOpUaPG3bt3pcaVK1cKIbp06SINTpw4UQihVCq3bt1q6/njjz8WQjRr1kwalI49
NGjQIDU1VWqxWCwjR44UQowfP15qmT17thAiMDDw559/zmfBpYVt0qRJVlaWrVH6hXuvXr2k
weTkZCFExYoVC1yBVapUeei7Fy5cUCqVGo3m/v37Uov0a7Nly5ZJg1KUefXVV22T/P3332XL
lhVCtGrVyvGlrlOnjhAiLi7O1k9CQoK/v3/jxo0fVXmuSqRPTavVrl271jbO6NGjhRD9+/d/
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
wgsvVKtW7YUXXrB/QogQIjs7e9asWbVq1XJneQAAAHBUfsHu8OHD7dq127lzZ05Ozt69ezt3
7rxx40bprR07dtSpU2fSpElcJAsAAOAl8gt2c+fONRgMJ06cuHr16vXr1xs0aDBlypTr16/3
7NnzhRdeuHPnzsKFC3mUBwAAgJfI7+KJU6dODRgwoF69ekKI0qVLz5gxo2PHjtWqVTMajcOH
D58+fXpwcHBx1QkAAIAC5Bfsrl+//vTTT9sGa9asKYRo1KjRZ599Vrt2bbeXBgAAvMC2bdsO
Hjzo2j7r16/fu3dv1/YJkX+wM5lMWq3WNqjT6YQQ48ePJ9UBAPDk2LVr16effuraPl9//XWC
nTvwsFcAAACZINgBAADIRH6nYoUQly5dsj124t69e0KI8+fP53rCWOPGjd1UHAAAABxXQLCb
M2fOnDlz7Fvee++9XONYrVYXFwUAAIDCyy/YTZkypdjqAAAAgJPyC3ZTp04trjIAAADgLC6e
AAAAkAmCHQAAePyo1eotW7bkajSZTAqFYteuXR4pyRsQ7AAAgDe6fv36iBEjKlWqpNPpypYt
+9JLLx04cCD/SVQq1d69exs0aFA8FXohgh0AAPA658+fj4iI2L9//4IFC06cOBEbGxsYGNi6
detvv/02n6kUCkVkZGRQUFCx1eltCnhWbMmSJQ0Gw5UrV8LCwuwfLwYAHpeenv7hhx8+ePCg
wDHVarVKpcrJySnw9kwWi0WIuy4qEEDRjRgxIiQk5NixY3q9XghRq1at1q1bly9f/syZMz16
9JDGuXv37gsvvLBv374SJUp8/PHHffv2NZlMGo1m586d7dq1u379+ttvv71z504/P7+XX355
/vz5BoPh7Nmz77///rFjxywWS6NGjZYsWVK1alUhxKlTp/r163fx4sVatWrNnz+/TZs2p06d
qlu37q1bt0aNGrVv37779+9HRETMmzevWbNmnlwvBckv2FWrVm3jxo1dunQJDw8/evToc889
V2xlAUCBTp06FRsb64aOb7mhTwCFcOfOnb17965evVpKdTazZ8+2H1y8ePHSpUvr1q07d+7c
YcOGde/e3X78l19+uVKlSn/99Vd6enr37t3Hjh372WefvfLKK40aNUpISDCbzYMGDerfv/9v
v/1msVj+8Y9/tGzZ8sCBA1euXBk0aJAQQqlUCiG6du1aokSJkydP+vn5TZ48uVOnTvHx8cHB
wcWyGooiv2CnUCi++eabwMBAIcSpU6eysrIeOlrz5s3dUhoA5Es6/DbqRfHRyy7rM2SYMFtc
1huAorl06ZIQonbt2vmP9tprr0nHz6KiombPnn3lypUaNWpIb508efLo0aOxsbGhoaFCiLVr
1964cUMIcejQIZ1OZzAYpMl79+5ttVoPHz6ckJAwY8aMgICAunXrjhgxIioqSghx4sSJI0eO
nDt3rnTp0kKImTNnfv7559u3b+/bt68bF945+QW77t27r127du3atUKIwYMHP2o0njwBwIN8
tCLI19NFAHADk8mU/wjVqlWTXkhBzf4IVFxcnEKhCA8PlwYjIiIiIiKEECdOnJg5c+a5c+eE
ENnZ2Uaj0Ww2X7t2TaVSVapUSRrZdu1FfHy8Uqm0hUUfH5+KFSteuXLFNYvnHvkFuzVr1rz2
2mtJSUkDBgyYMmWKbYEBAADc5+mnn1YoFCdOnMj1PHqz2axUKhUKhTQonS19KGmcXMee4uLi
OnXqNGXKlH//+996vX7r1q3dunWTRlOr1bZuVSrVo7q1WCw5OTlFXazikF+wU6vVnTt3FkKs
Xbv2tddee/rpp4urKgAA8OQKCgrq0KHD3LlzX3/99YCAAFv7Rx99dPjw4d27dxfYQ9WqVa1W
659//imdz/39999///334OBgk8k0evRojUYjhDh8+LA0cmhoaHZ29o0bN8LCwoQQx48fl9qr
VatmsVjOnTv3zDPPCCEePHhw9epV22FC7+TQ7U527dr19NNP371798cff4yJifnXv/71888/
p6Wlubs4AADwZPr0008zMzPr168fGxt77ty5ffv29e/ff8GCBePGjXNk8nr16jVq1OiDDz64
fPnyxYsXhw4deu7cuUqVKpnN5sOHD2dnZ8fGxh48eFAIcePGjaZNmwYHB8+aNSszM/PcuXOf
f/65rZOmTZuOGTPm7t276enpY8eO9ff3lw7yeS2Hgp3FYhk9enRoaGiXLl2GDBkyePDgF198
MTQ09OOPP3Z3fQAA4AlUrVq148ePt2vXbty4cREREX369MnIyDh06FCHDh0c7OH777/38fGp
Xbt28+bNGzZs+PHHHzdu3HjMmDFdu3YNCwvbvXv3li1bGjRoUK9evRs3bmzatGn//v0hISFD
hw6dMWOG+O953tjYWK1WW6tWrfDw8CtXrhw4cMD+CKIXyu9UrM0nn3zyySefdO/evUuXLqGh
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
FEK0atWqQ4cOEyf+z82Rly1bVqtWrUWLFr333ntCiHfffbdKlSqjR48WQty6dWvUqFH79u27
f/9+RETEvHnzmjVrZjab1Wp1TEzMrFmzIiMjY2JibF0ZjcZOnTppNJpt27bZR6MRI0aEhIQc
O3ZMuiymVq1arVu3Ll++/JkzZ3r06GE7FTt79uxffvll165dMTExOp2uXr16y5Ytk3o4fPhw
06ZNL126VKlSpQJXmkNH7GJiYkaPHt26dWv745/Vq1dft27dwoULHekBAACgUEqUKDF//vzR
o0ffvn0777vdunUTQkiPKmjRokXHjh0zMzPbt2+/f/9+aYQ9e/bUqlVLGszKyjpy5MgLL7yQ
q5MyZcosWrRo0qRJly9f/umnnzZv3rx69WrpWv6uXbsmJyefPHkyKSmpcePGnTp1SkpKUqlU
KpXq888///bbbxcvXmzf1eDBgx88eLBp0yb7VHfnzp29e/eOHTs218XOs2fPnjp1qn3Lnj17
KlSoEB0dffz48cGDB69fv952YeKGDRsiIyMdSXXCwWD32WefDRs2bOvWrf3797c19uvXb8yY
MY86GgcAAOAMq9U6cODAiIiId999N9db//nPf44cObJw4cJSpUr5+PhMnz49Jydn27ZttmCX
np5+5syZN998c9++fUKIgwcP+vv7P/vss3nn8sYbb7Rt2zYqKmrYsGG2k7AnTpyQ+i9durTB
YJg5c6bZbN6+fbs0Sbdu3Z599ll/f39bJ5MnTz527NgPP/xgMBjsO7906ZIQonbt2oVa8Fdf
fdVsNn/33XfSSti4cePAgQMdnNahYHfx4sUePXrkbY+MjLx8+bLjhQIAABTK559/vmXLllxP
wLp48aIQIiwsTKFQKBQKlUp1//79S5cutWvXLj4+/ubNm/v374+IiGjXrp0U7Pbu3du+fftH
3cp0+fLl//nPf0JCQqSTsEKI+Ph4pVJZo0YNadDHx6dixYq2+7tJN+KwWbVq1cyZM5cuXfqo
G80U9pZPvr6+vXv3Xr16tRDiwIEDqampD41hD+VQsAsICHjojcpSUlIeozu/AwCAx07VqlU/
+uij4cOHp6en2y6OlOJHZmam1c6ECRNKlSoVERFx4MCBPXv2REZGPvPM1qBglgAAIABJREFU
M8nJyTdu3Pjll1/ynoe1CQsLq1q1arNmzfK5obrFYsnJyZFe57rN+NGjRzt06DB69Oi8tw59
+umnFQrFiRMncrUXeJefwYMH7969+8aNGxs2bHj11VdzHQjMh0PBrm7duvPnz891p8d79+5N
nz69cePGDs4JAACgCMaMGRMYGDhp0iTbIxKqVasmhDh58qRtHOmkpxCiQ4cO+/fv/+WXXyIj
IxUKRbNmzX766afff/+9Q4cOjs+xWrVqFovFdtOTBw8eXL16VZppXp999tn69etv3br14Ycf
5norKCioQ4cOc+fOTU1NtW//6KOP8r9xXcOGDWvXrv3VV19t3LhxwIABjlfuULCbOHHir7/+
Wrdu3fHjxwshYmJiBgwYEB4efuHChY8++sjxmQEAABSWWq1euXLl0qVLr1+/LrXUqlWrTZs2
H3zwwbVr14xG47Jly+rUqXPjxg0hRPv27Xfu3Hnu3LmmTZsKIVq0aLFw4cIaNWqEhoY6Psd6
9eo1bdp0zJgxd+/eTU9PHzt2rL+/v3S5Rl4qlSooKGjdunXR0dHSDd3sffrpp5mZmfXr14+N
jT137ty+ffv69++/YMGCcePG5RrTYDDExcXdv39fGoyKipo1a1aJEiWaNWvmeOUOBbvIyMif
f/7Z399/0aJFQohVq1atWbOmRo0aO3fuLNTMAAAAiqBhw4bDhw+/c+eOreWrr74qV65c3bp1
S5UqtW7duu3bt4eFhQkhmjVrdv369QYNGkina1u0aHH27NlCHa6TxMbGarXaWrVqhYeHX7ly
5cCBAwEBAfmM37Jly3HjxvXr1y/XNbzVqlU7fvx4u3btxo0bFxER0adPn4yMjEOHDuUtaejQ
oUuXLq1Tp4402Ldv38zMTMcvm5A4eh+7tm3b/uc//7l9+7YUhytWrGj/PFYAAAAXynur3kWL
FkkHmCRly5bdsGFD3gm1Wm16erptsFGjRo48XC7v7CpUqLBly5a8Y9pfCaFWq+07nzlz5syZ
M/NOUr58+RUrVjx0vvY9vPvuu/bX/yYmJiqVyofewy8fjgY7IcS1a9eOHz9+584dpVKZkJDw
/PPPly1btlAzAwAAQP7MZnNCQsKgQYOGDx9epkyZQk3rULBLTk7u27fvjz/+aN+oVCp79+69
YsUKX1/fQs0SAAAAjzJjxoz58+e/8sors2bNKuy0DgW7d95558cff+zRo0eXLl2ko3Q3b978
+eefY2Nj/fz8Pv/880KXDAAAgIeZOnVqrudSOM6hYPfDDz+8++670dHR9o0DBgyoWrXqsmXL
CHYAAADewKGrYrOzs1u3bp23vVWrVrlubgcAAABPcSjYNWjQQHp2Ry5xcXEPfewaAAAAip9D
p2IXLVrUs2fPKlWq/OMf/5Bu+myxWHbv3r1w4cKvv/7azRUCAADP+z1epGS4oJ8byS7oBI+S
X7CzPftWoVDk5OT06NFDp9OFhYUplcqbN28+ePCgXLlyb7/99sGDB4ulVAAA4AEGgyEoKGjy
Vpd1GBQkuKWGm+QX7IKDg22vS5UqVbFiRdugdG2sxWLJzs52X3EAAMDj5s6dO3fuXE9XAYfk
F+x+/fXXYqsDAAB4p3HjxsXExLi2z549e3JXDXcoxJMnhBBpaWlmszlXY4kSJVxXDwAA8C6Z
mZnJyclCPCWEzhX9GYVIePDggSu6Qm4OBbtLly698847v/zyy0M/BkcewQYAAB5z3wnxvCv6
iReiqiv6wUM4FOyioqJOnDjRrVu30NBQlUrl7poAAABQBA4Fu6NHj+7YsaNp06burgYAAABF
5tANin19fStVquTmSgAAAOAUh4Jd3759V61a5e5SAAAA4AyHTsXOnj27c+fOP/30U5MmTUqV
KpXr3fHjx7uhMAAAABSOQ8FuwYIFu3btEkL89ttved8l2AEAAO+nVqs3bdrUrVs3+0aTyaTR
aHbu3NmuXTtPFeZCDgW7xYsX9+jR47333itbtixXxQIAALd6/vnna9euvXr1altL1apVw8PD
d+7caWtp3rx5xYoVv/rqKyfnpVKp9u7dW69evSJMu2fPnoCAgOeee87JGlzIoWB37969xYsX
h4WFubsaAACALl26LF++3Gq1KhQKIUR8fPzNmzcTExMzMjIMBoMQIiUl5ciRI2+99Zbz81Io
FJGRkUWbdsGCBV26dHn8gl2tWrXu3LlDsHscJSYmbt261WQyubBPX1/fPn36SH9aAAC4XJcu
XaZOnXry5MmIiAghxPbt25s3b3758uW9e/d27txZCLFz506r1friiy+ePfv/2rv3+Cjqe//j
370lm809QiQxIuFihGAoWEXuCMQL4gFarQIVvBUiR5EHKAXUA4goigr1iBZUUMqp4qViDyVR
AyKIQMMdxaoEiBzuAZKQbPY68/tj2v1tuQRIZjK737ye/7D73clnPvkyO/vOzOzutxMmTNi8
ebOiKF27dp0/f37btm2FEO+8884LL7ywf//+5OTkX/3qV6+88orT6RRCnDhx4pZbbvnqq69S
UlLmzJlz7733hk7F9uvXz2az/fnPf37nnXcOHDhQU1PzzDPPjBo1SgixY8eOkSNH/vjjjx06
dHjppZf69eu3Y8eO8ePHr1mzpri4+M0339yyZcvRo0fHjx//1VdfVVRUdO7c+cUXX+zRo4ei
KOeraZCLCnbz5s2bMGHC3Llz8/LyjGsFRnjppZeWLl2qe1mn0zlixAjdywIAIITo0qVLZmZm
YWGhFuyKior69OnTsmXLoqIiLdh99tlnPXr0SE1N7datW9euXQ8cOBAMBh944IFRo0atX79+
7969DzzwwBdffNG3b9+ysrJf//rXc+fOnTJlihDi1Vdfff311/Py8mbPnl1QUDB06FAt8Akh
rFarzWZ7+eWXV65cmZ6e/vbbb48dO/bOO++Mi4u74447evfuvW7duv379z/wwAPawqtXr27V
qtXkyZMLCgqEEIMHD05JSdm+fXtCQsLTTz89cODA0tLSZs2anbNmfHy8QVN3UcFu6tSpZWVl
nTp1SkhIOPtdsfv379e/L+jE7/cLIYT4gxAZOpVcK8RrXq9Xp2oAAJzJYrEMHDiwsLBw6tSp
Pp9vzZo1M2bM2Lt379SpU7UFPvvss0cffVQIsWHDhtjYWO0k0vDhw++55x5VVSsqKlRVTUtL
s9lsrVu33rx5c+gdAsOHD+/Ro4cQ4sEHH3zuuef2799/zTXXhK/63nvvTU9PF0L079/f7Xbv
37+/srLywIEDM2fOTEpKysvLGzt27IMPPnhGw9u2bdu0adPu3bu1n3322WcXLFhQWFh47733
nrNmbm6uQVN3UcHOarXm5OTk5OQY1ASMd6sQV+tUqlanOgAAnNegQYMWL15cUVGxefNml8vV
pUuX1q1bDxs2rLS01OPxHDhwYNCgQUKIbdu2Pfvss7t37xZCeL1ev98fDAY7d+48ZsyYG264
4YYbbsjPzx8xYkS7du20sqEbWhb0eDxnrLdly5baDe1IXm1t7c8//2yz2ULf1HDddded3W1p
aanVag1lxLi4uKuuuip05Ovsmg2fn/O5qGC3du1a4zoAAAA4Q35+vsPhKC4u3rhxY35+vsVi
SU1Nvf766z///PPa2trWrVu3b99+z549AwcOnDZt2sqVK51O56effqp9lInFYvnjH/84efLk
lStXrlixYtasWUuXLr377ruFEFbrBb6aQXu7RjhVVe12e2j8Ij8eRFEUn893vprGuahvngAA
AGhMLperb9++q1atWrNmza233qoN3nzzzatXry4uLtYO123evDkQCDz++OPakbCNGzdqiwUC
gePHj7dq1Wrs2LErV64cM2bM66+/Xu9OMjIyvF7voUOHtLtbtmw5e5l27dopiqIdOBRC1NTU
lJWVhY4ONqaLCnbNzi8pKcnoFgEAQBM0aNCgL774YufOnTfffLM2csstt6xbt279+vVasGvV
qlUwGNy4caPX633vvfe++eYbIcShQ4eWLFnSpUuXLVu2KIpy5MiR7777riEZq3v37s2aNZs1
a1Ztbe3u3bsXLFgQesjlcu3Zs6eioqJTp07du3d/4oknTpw4UV1dPWnSpMTExDM+CblxXFSw
63mWNm3auN3ujIyMkSNHGt0iAABogu64447S0tLc3NzLL79cG+natavX61UUpU+fPkKIG2+8
8Yknnhg8eHBmZuaqVauWL19+3XXXderUqW/fvg899NDQoUPj4uK6dOmSnZ390ksv1buNmJiY
jz76aO3atc2bNx8zZszMmTPFv07pascCr732WiHEe++9FxMT06FDh+zs7P37969bt86Ug18X
dY3d8uXLzx48cuTI3Xfffdttt+ndEgAAgGjZsqWqquEjNpvt1KlT4SMvvvjiiy++GLq7efNm
7ca0adOmTZt2RsHwT3Vt0aJFqHjoxvkW6NGjx5YtW2JiYoQQGzZsEEJkZWUJIR577LHHHnss
1O0589L5ahqk/tfYtWjR4uWXXz571gAAAKShqmr79u3HjBlTUVFx+PDhGTNm9O7dO2IvRWvQ
myeysrJC1wkCAADIx2KxfPzxxz///POVV16Zl5cXHx9vxCf/6+WiTsWek6qqixYtOvvzigEA
AGSSl5e3atUqs7u4KBcV7H7xi1+cMRIMBo8cOVJeXv74448b0BUAAAAuWT2P2Dkcjry8vMGD
B2vfjwYAAADTXVSw2759u9F9AAAAoIHqf40dAABoSpYIsVqPOif0KIJzqyvYDRgw4GJKFBcX
69QMAACIWK+Z3QAurK5gV1FRcc5xi8XicDgsFsuGDRuM/pw9AABgrvvvv79Xr1761mzZsqW+
BaGpK9iFPr75bH/961/HjRsnhLj//vv1bwoAAESMzp07d+7c2ewucFEu+QOKy8rKBg8ePHjw
4OTk5HXr1i1atMiItgAAAHCpLiHY+f3+F154oUOHDl9++eXLL7+8ZcuWHj16GNcZAAAALsnF
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
9NLhw4eFEKNGjQofP3r0qHYj9JHFDocjLS2tvLy8UTptPP3793///fdPnTqVmpq6atWqoUOH
hj9ax9ZyzpPa0e7o0aNbt26dPXu2djc/P3/ZsmXDhw8PvVGgRYsW2g2r1Rq+PUg5G6Jem4fT
6ezdu3dxcXHv3r13797tdru7d+9uUvvmk36nCikR7KKGxWI5fPjwjBkzhg0bNm3atJiYmE2b
NmlnIUMLmNheI+jVq9ddd90VPpKRkXHixAkhxEcffRQTExP+kHaRePig1WoNv1pRDmlpab/4
xS++/PLLG2644fDhw127di0tLdUeqntrkW8qhBBFRUWqqs6YMUO7qyiKx+PZuHFjjx49tJHw
tw4Eg8HQU0bK2RD13Tzy8/OfeOKJkydPrlu3rlevXrGxseb9BsY6e5+pKErdCwCRj2AXoT75
5JPKysr77rtPCFFVVSWESElJ2bNnTzAYHDp0qHYE4ocffjC3yUaWmJh41VVXnTGYmZkphNi3
b19OTo42cuTIkdCBmYMHD15//fVCiEAgcOLEifDzUNLIz89///333W533759Q5fJCyGa2tYS
CASKi4uHDRsW/gk4ixcvLioqCgW7Q4cOaTd8Pt+JEyeaN29uQqONqx6bx9VXX33VVVetWbNm
/fr1U6dONaFpY5xzp+pwOCwWi9/v15YJHewHohfX2EWo1NTUTz/9dPXq1WVlZUuXLs3KysrM
zExPT1cU5R//+Iff71+7du33338vhDh58qTZzZrpyiuvzMvLe/vtt48fPx4MBgsLCx999NHQ
nHzxxRdlZWWBQGD58uWKokj2rljN9ddff+rUqTVr1pxxLVRT21rWr19fU1Nz++23p4cZNGjQ
zp07Q3nuyy+/LCsr8/l8H3/8saIoWuiXW/02j/z8/A8++CA+Pr59+/YmNG2Mc+5UbTZbixYt
duzYIYTwer1/+9vfzG4TaCiO2EWovn37lpeXL126tLq6+pprrnnyySetVmtOTs6vfvWrWbNm
WSyWG2+88cknn/yv//qvcePG/eEPfzC7XzNNnDjxzTfffPTRR1VVveqqq6ZPn56WlqZdDfPr
X/96/vz5e/fuvfzyy6dMmZKYmGh2s/qz2Ww33XTTjh07srOzw8eb2tZSWFjYrVu3pKSk8MHc
3NwrrriiqKhIuwrz9ttvf/3110tLS1NSUqZOnXrGwlKqx+aRnp5+0003LV68WLK3TZxzpyqE
ePjhh//4xz9u2LAhNTX1N7/5TUlJCZ/2h6hmCb1LDgBkpZ12nD59epcuXczuJQqUlZVNnDjx
rbfeauKfAQ5EI47YAQD+SVGU8vLyV1999bbbbiPVAdGIa+wAAP+0bNmyRx555Morr7z33nvN
7gVAfXAqFgAAQBIcsQMAAJAEwQ4AAEASBDsAAABJEOwAAAAkQbADAACQBMEOAABAEgQ7AOc2
ffp0i8WSnp4e+or0cA899JDFYunZs6fu6x0wYECrVq10LwsATQHBDsB5Wa3WkydPnv3N6LW1
tR9++KHD4dBlLdu3b7dYLLqUAoAmjmAH4LysVmvXrl0XL158xvgnn3xSW1vbqVMnXdaybt06
XeoAAAh2AM4rEAgMGjRo5cqVR48eDR9/9913b7rpptjY2PDBwsLC3r17JyYmxsXFdezY8ZVX
Xgl9sU3v3r179eq1bdu2/v37JyUlpaenDxs27NixY0KIW2+9ddy4cUIIi8Xyy1/+Ulvebrfv
27fvtttuS0xMTExMvPvuu0+ePNkYvzAARDmCHYC63HXXXYqiLF26NDRy8ODB4uLie+65JxgM
hgaXL19+++23x8fHL126dMWKFbfccsvEiRN///vfa4/GxMSUlZWNGTNmypQpe/bseeONNz78
8MNJkyYJIf77v/978ODBQoiSkpI//elP2vLBYHDo0KG9e/deunRpQUHBhx9+OHHixMb7nQEg
eqkAcC7Tpk0TQtTW1g4YMCA3Nzc0Pnv27Li4uKqqqq5du/bo0UMbvOaaa1q2bOn1ekOLDRky
xOFwlJeXq6rav39/IcTXX38derR///6ZmZna7QcffDB8X6Qt/Je//CU00r179/T0dGN+SwCQ
CkfsAFzAfffd991335WUlGh333333SFDhiQmJoYWOHTo0D/+8Y+BAwfGxMSEBu+44w6/379x
40btrsvl6tGjR+jRrKysI0eOnG+NTqdzyJAhobtt27YtLy/X69cBAIkR7ABcwNChQxMTE7W3
UJSUlHz//fcjR44MX+DgwYNCiCuuuCJ8MCMjQwhx6NAh7W7z5s3DH7Xb7YqinG+Nl19+efj7
ZB0ORx0LAwBCCHYALsDlct11113vvfeex+N59913MzIy8vPzwxfQQtgZ2UtVVSGE1cpOBgAa
D/tcABc2atSoioqKzz//fNmyZcOHD7fZbOGPZmVliX8dtwvR7moPAQAaB8EOwIX16tWrdevW
M2fOLC8vP+M8rBCiRYsWHTt2XLFihcfjCQ3+5S9/cblc3bp1u2Bx7YBfIBDQt2cAaIIIdgAu
zGKxjBw5cvPmzZ06dcrLyzt7gRdeeOHIkSODBw/+61//WlRUNHbs2KKioqeffjopKemCxTMz
M4UQzz333Mcff6x/6wDQlBDsAFyUkSNHavHunI8OHDiwqKjI7XYPHz58yJAhGzduXLRo0eTJ
ky+m8u9+97vOnTs/++yzTz75pK4tA0CTY1H/9dHwAAAAiGocsQMAAJAEwQ4AAEASBDsAAABJ
EOwAAAAkQbADAACQBMEOAABAEgQ7AAAASRDsAAAAJEGwAwAAkATBDgAAQBIEOwAAAEkQ7AAA
ACRBsAMAAJDE/wMtwQAB+LB2OQAAAABJRU5ErkJggg=="
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Load function crosstab developed by Dr Paul Williamson</span>
<span class="nf">source</span><span class="p">(</span><span class="s">&quot;http://pcwww.liv.ac.uk/~william/R/crosstab.r&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Count and percentage of users per month</span>
<span class="nf">crosstab</span><span class="p">(</span><span class="n">city</span><span class="p">,</span> <span class="n">row.vars</span> <span class="o">=</span> <span class="s">&quot;Month&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_text output_subarea ">
<pre>     
Month     Count   Total %
  1    15341.00     10.06
  2    18857.00     12.37
  3    19235.00     12.62
  4    30709.00     20.14
  5    31157.00     20.44
  6    37151.00     24.37
  Sum 152450.00    100.00</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Count of users per month by grouped by cities</span>
<span class="nf">crosstab</span><span class="p">(</span><span class="n">city</span><span class="p">,</span> <span class="n">row.vars</span> <span class="o">=</span> <span class="s">&quot;Month&quot;</span><span class="p">,</span> <span class="n">col.vars</span> <span class="o">=</span> <span class="s">&quot;City&quot;</span><span class="p">)</span>

<span class="c1"># Percentage of users per month by grouped by cities</span>
<span class="nf">crosstab</span><span class="p">(</span><span class="n">city</span><span class="p">,</span> <span class="n">row.vars</span> <span class="o">=</span> <span class="s">&quot;Month&quot;</span><span class="p">,</span> <span class="n">col.vars</span> <span class="o">=</span> <span class="s">&quot;City&quot;</span><span class="p">,</span> <span class="n">type</span> <span class="o">=</span> <span class="s">&quot;r&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_text output_subarea ">
<pre>      City Chicago New York City Washington    Sum
Month                                             
1              650          5745       8946  15341
2              930          6364      11563  18857
3              803          5820      12612  19235
4             1526         10661      18522  30709
5             1905         12180      17072  31157
6             2816         14000      20335  37151
Sum           8630         54770      89050 152450</pre>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_text output_subarea ">
<pre>      City Chicago New York City Washington    Sum
Month                                             
1             4.24         37.45      58.31 100.00
2             4.93         33.75      61.32 100.00
3             4.17         30.26      65.57 100.00
4             4.97         34.72      60.31 100.00
5             6.11         39.09      54.79 100.00
6             7.58         37.68      54.74 100.00</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>**
Least common month is month 1(JANUARY) with 10.06%.</p>
<p>The most popular month of the three cities(Chicago, New York City and Washington) is month 6(JUNE) with 24.37% followed by 5 (May) with 20.44%.
.
**</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Question-3">Question 3<a class="anchor-link" href="#Question-3">&#182;</a></h3><p><strong>What gender travels frequetly? (Considering NYC and Chicago)?</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Creating new city2 by joining &#39;New York City&#39; and &#39;Chicago&#39; data</span>

<span class="n">city2</span> <span class="o">&lt;-</span> <span class="nf">concatenation</span><span class="p">(</span><span class="n">chi</span><span class="p">,</span><span class="n">ny</span><span class="p">)</span>      <span class="c1">#city2 &lt;- rbind(chi, ny)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Count of Gender (Male and Female)</span>
<span class="n">total</span> <span class="o">=</span> <span class="nf">sort</span><span class="p">(</span><span class="nf">table</span><span class="p">(</span><span class="n">city2</span><span class="o">$</span><span class="n">Gender</span><span class="p">))</span>
<span class="nf">print</span><span class="p">(</span><span class="n">total</span><span class="p">)</span>

<span class="c1"># percentage of Gender (Male and Female)</span>
<span class="nf">round</span><span class="p">((</span><span class="n">total</span> <span class="o">/</span> <span class="nf">length</span><span class="p">(</span><span class="n">city2</span><span class="o">$</span><span class="n">Gender</span><span class="p">)</span> <span class="o">*</span> <span class="m">100</span><span class="p">),</span> <span class="n">digits</span> <span class="o">=</span> <span class="m">2</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>
       Female   Male 
  7158  13882  42360 
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_text output_subarea ">
<pre>
       Female   Male 
 11.29  21.90  66.81 </pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Visualizing data with ggplot</span>
<span class="nf">ggplot</span><span class="p">(</span><span class="nf">aes</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="n">Gender</span><span class="p">,</span> <span class="n">fill</span> <span class="o">=</span> <span class="n">City</span><span class="p">),</span> <span class="n">data</span> <span class="o">=</span> <span class="n">city2</span><span class="p">)</span> <span class="o">+</span>
    <span class="nf">geom_bar</span><span class="p">(</span><span class="n">position</span> <span class="o">=</span> <span class="s">&#39;dodge&#39;</span><span class="p">,</span> <span class="n">colour</span><span class="o">=</span><span class="s">&quot;black&quot;</span><span class="p">)</span> <span class="o">+</span>
    <span class="nf">ggtitle</span><span class="p">(</span><span class="s">&#39;Counts of each gender&#39;</span><span class="p">)</span> <span class="o">+</span>
    <span class="nf">scale_x_discrete</span><span class="p">(</span><span class="n">labels</span> <span class="o">=</span> <span class="nf">c</span><span class="p">(</span><span class="s">&#39;Not mentioned&#39;</span><span class="p">,</span> <span class="s">&#39;Female&#39;</span><span class="p">,</span> <span class="s">&#39;Male&#39;</span><span class="p">))</span> <span class="o">+</span>
    <span class="nf">labs</span><span class="p">(</span><span class="n">y</span> <span class="o">=</span> <span class="s">&#39;Number of Riders&#39;</span><span class="p">,</span> <span class="n">x</span> <span class="o">=</span> <span class="s">&#39;Gender&#39;</span><span class="p">)</span> <span class="o">+</span>
    <span class="nf">scale_fill_manual</span><span class="p">(</span><span class="s">&quot;legend&quot;</span><span class="p">,</span> <span class="n">values</span> <span class="o">=</span> <span class="nf">c</span><span class="p">(</span><span class="s">&quot;Chicago&quot;</span> <span class="o">=</span> <span class="s">&quot;black&quot;</span><span class="p">,</span> <span class="s">&quot;New York City&quot;</span> <span class="o">=</span> <span class="s">&quot;orange&quot;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
VsXHefPNN5csWVK/fn1LpcQ7U716dSHE7du379hbUVHRmTNnnJycmjdvXrxu2YuqfRXuuPTi
f5eioqLTp08LIdR4Z1H8SL4yLat9+/Z3XCkAAB5QZTwjUj1bQt1kdU9ZWVl5eXmurq5eXl4l
JqnXuktPTy/T0tX9dxaKogghzGbz3eaPjY01mUzr1q0bPXq0ECIkJKRPnz5RUVFBQUF2bTg3
NzcrK0sIoR4PV1pKSkqdOnWEEJs3b16yZMmRI0fy8vJKz5adnZ2dne3u7q7uJLWixLUDnZyc
xN3fmaysrIKCAi8vLxcXl+L1unXr3scqCKt/F3VZpVehRo0a97csB14lEQAgt8oY7Bo2bPjb
b78dPnxYPaXAOivBq6ioyDKD/bi4uKxevTo6Ovrbb7/dunXrzp07Fy1aFBsbu379+oEDB9qv
YXU2RVHUw8tKU5PQmjVrIiMjPT09o6Ki2rZt6+Xl5eTktHnz5o8++kidTc1nRqPRbDbb8L1S
V7D0gMUrGldB47JKv6Umk+n+llUijAIAYCuVMdiFh4dv2LDhk08+mTZt2h2v4mY2m+fNmzdg
wIBGjRp5eHgYDIacnJxbt26VuDjFtWvXxP+2vtwxTqWmptqqZ39//8jIyMjIyLy8vI8//vj1
11+PjIzs27evm5tbiTk1NnxP7u7uXl5et2/ffvXVV628RD2ldMuWLZ07d7YU1cPjVHq93tPT
MzMz8/r16z4+PloWrYWHh4ezs3NmZqbJZHJ2drbUk5OTy7oKGpeVn5+fm5tbfKNd8SsO2mpZ
AAA8iMp4jN3gwYP9/PzOnTunnlZZ2oIFC2bNmqXu+hRCqAeQqQeKWdy4ceOPP/7Q6/VNmjQR
Qri7u4tSu3cPHTr04N0mJSUVD4ju7u5RUVEdOnS4devW+fPn7/gSLQ1roR5DVvqCczdu3FAf
5Ofnp6SkeHh4FE91ZrN527Ztpfv54Ycfihfffffd8PDwX3/9VWMzJTg7OwcFBZlMpjNnzhSv
l1j0PVdB47KCg4OFEMePHy9e37t3r82XBQDAg6iMwU6v16tXAF60aNFLL71UfLtLWlraq6++
OmPGjKpVq8bFxalFNeEtWLCgoKDAMueCBQsKCwuHDh2qbjNTTwJQL/ChznD69Om1a9eWtTc1
IF6/fl19euzYsXr16r344ovFF52ZmXn+/HlnZ2c/P787DqKlYS3UcWbPnq1u6lPt2bOnZs2a
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
SURBVDbfbVqjRo1GjBgxbdo068dLPlwnxqanpzu6BRm4u7t7eHhkZWXl5eU5uhdUXIqi1KhR
o6CgICMjw9G9oEIbOHDgrl27suOFwfXeM8ukzUxx9KIuNTXVtsP6+PjYdkAhRMeOHdPT09Vf
/JYtW2ZmZh47dsxgMKhT+/btu2vXrqtXr7q5ufn7+/v6+h4/flxRFCHEgQMH2rVrV6VKlays
LOuvdXd3Dw8P//HHH/fu3RsWFqZODQ8PP336dEpKitlsDgwMrF69+okTJ9RJqampdevWdXV1
VUeGytqu2GrVqun1evWBFeXVKgAAcLCrV68mJCT07t3byckp73969eqVmZl54sSJtLS0K1eu
9OjRQ011QognnniiadOmWl6rzmMwGCypTggRGBiYlpYmhEhOTr58+fKTTz5pmeTv79+6dety
Wu2Hh7Vdsfv37y/xAAAAVGaXL18WQqxYsWLFihUlJl26dMnFxUUIUfqOBhcuXLjna9u0aSOE
UC++YaHT6YqKioQQarwrMTUgIOD48eM2WCuJlOEYuztKTEysV6+eLToBAAAPh5deeunll18u
UXz00UfPnTsnhHBy+n/2B1q23ll/rfUl3vHIMZPJpLHhyuMewW737t3z588/f/58/fr133zz
zZ49e1om5efnL1myZP78+Tk5OdYHuXHjxrp1644dO1ZQUFC/fv1Ro0Y99thjQoisrKw1a9Yc
P37caDQ2bNgwKirKz8/PhnUAAGBb6jmUJpOpXbt2pafevHlTCHHlypXixT/++EPLa62zXEa3
eDExMbGs40jP2jF2+/fvDw8P37FjR0FBwa5du3r37v3VV1+pk7Zv3/7444/PmDFDy0my8+bN
S09PnzNnTmxsrI+PT0xMjHrEfWxs7NWrV6OjoxcvXmwwGGJiYtTNrbaqAwAA26pevXrbtm03
b95869YtS/HTTz+dMWNGYWFhUFCQl5fX1q1bLZMOHTpkOX7O+mutL7devXo+Pj7btm2z/MT/
+eefx44ds9mKycJasFu4cKHBYEhISEhKSrp06VKrVq2io6MvXbo0YMCAp5566tq1a8uXL7f8
te4mMzPT19f31VdfrV+/vr+///DhwzMyMpKTk9PT0w8dOvTKK68EBQUFBARERUWlpKScOHHC
VnWbvksAAOD/LFq0KCcnp0uXLp9++un27dtnzpw5ZsyYlJQUnU6n0+lGjx598uTJUaNGbd++
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
mwAAACk1a9bsxx9/dHQXNqBpi90HH3wQFxe3efNmo9Fo74YAAABwfzRtsVuyZIlOp+vfv7+r
q6uPj4+Li0vxqRX8EswAAACVhKZgV1RU5Ovr2717d3t3AwAAgPumKdjt3bvX3n0AAADgAZXh
OnZ5eXknTpy4dOlSp06dfHx8CgsLdTougwcAgOTCw8MNBoNtx2zRooVtB4RKazJbunTpnDlz
MjMzhRD79u3z8fGJjo6+fPny2rVriXcAAEisdu3arVq1su2YderUse2AUGnKZGvXrp00adIz
zzzTq1evqKgotdiwYcNFixaFhIRMnjzZnh0CAABHio+PX7VqlW3HHDp06BNPPGHbMSE0Brv3
338/Kirq73//e15eniXYDR8+/MyZM3FxcQQ7AACk91qECKxug3GuZ4nFW2wwDu5IU7D7888/
ly5dWrretWvXJUuW2LolAABQ4QzvJNrUt8E4564Q7OxI0wWKq1atmpeXV7p++/ZtvV5v65YA
AABwPzQFu2bNmi1ZsiQ3N7d48caNGzExMe3atbNPYwAAACgbTbtip0+fHh4e3qxZs969ewsh
1q5du3r16m+++SY3N3f16tV27hAAAACaaNpi17Vr1++//97T03PFihVCiHXr1n3yySeNGjXa
sWNHWFiYnTsEAACAJlovQde9e/fffvvt6tWrly9fFkLUrVvX29vbno0BAACgbDRtsVNdvHjx
l19+OXjw4OHDh/fu3ZuWlma/tgAAACq4wsJCRVG2bdv2gCP88MMPtmpJU7C7efNmnz596tat
++yzz0ZGRr788svPPPPMI488MnTo0OzsbFu1AgAAoGrdurVer//rr7+KF5s2bWrDg/s///xz
Nze3kydPFi9++umn7u7up06dstVShBCXLl0aN25cvXr13NzcatWq9cwzz+zZs0ed5OzsvGvX
LvXGHjt37jx8+PADLktTsBs/fvx///vf5557Lj4+fuvWrVu3bo2Pjx84cOCGDRsmTJjwgB0A
AACUVqVKlcjISPuNP2jQoN69e48ZM6aoqEitXLt2bcKECXPmzAkJCbHVUs6cOdOiRYvdu3cv
W7YsISFhw4YNXl5e3bp1+/rrr4UQiqJ07dpVPbxt2bJl5RTstmzZ8sYbb2zcuHHkyJFPP/30
008/PXLkyA0bNkyfPl1tCwAAwLbeeuutY8eOrVu37o5T09LSBg0aFBAQUKVKlS5duvz2229C
iLp163766afqDNOnT1cUJSkpSX3apUuX+fPnlxjk73//+19//aWeGyqEeOONNxo0aDBp0iQh
xJUrVwYPHhwQEGAwGMLCwn755RchhMlkUhQlLi4uKCho1KhRxYcyGo09evTo1atXYWFh8fq4
ceN8fX0PHz787LPPhoSEdOvWbf369VOmTDlx4oQotiv2ySef/O677958881WrVp16NBh7Nix
lhH279/v5OSUmJio5U3TFOzy8/O7detWut6lS5cSF7cDAACwiWrVqi1ZsmTSpElXr14tPbVf
v35CiBMnTqSnp3fq1Klnz565ubk9evTYvXu3OsPOnTtDQkLUp3l5eQcOHHjqqadKDFKzZs0V
K1bMmDHjwoUL27Zt27RpU3x8vLOzsxCib9++N2/ePHr0aHp6ert27Xr16pWenu7s7Ozs7PzR
Rx99/fXXK1euLD7UmDFjsrOzN27cqNP9/2emXrt2bdeuXVOmTHF3dy8+84IFC2bPnl28snPn
zjp16sTGxh45cmTMmDGff/655d4QX3zxRdeuXevVq6flTdMU7Fq1avXnn3+Wrp89e7Zly5Za
RgAAACgTs9k8atSoFi1avPHGGyUm/fbbbwcOHFi+fHmNGjX0en1MTExBQcG3335rCXZZWVkn
Tpx4+eWXf/75ZyHEr7/+6unpecfQ8uKLL3bv3n306NFRUVGWnbAJCQnq+H5+fgaDYd68eSaT
aevWrepL+vXr17JlS09PT8sgM2fOPHz48JYtWwwGQ/HBz58/L4Ro2rRpmVb8hRdeMJlM33zz
jfomfPXVVyW2DlqhKditWLFi9erVmzZtMhqNaqWoqGjHjh3Lly+PjY0tU68AAADaffTRR5s3
b/7uu++KF9XtTQEBAYqiKIri7Ox869at8+fPh4eHnzt3Li0tbffu3S1atAgPD1eD3a5du3r0
6OHkdOfYs3r16t9++83X11fdCSuEOHfunJOTU6NGjdSner2+bt26lp2hjz76aPGXr1u3bt68
eR9++GH16tXvOH6JnbP3VKVKlUGDBsXHxwsh9uzZk5GR8dxzz2l8rbXr2FnWR1GUgoKC5557
zs3NLSAgwMnJKS0tLTs7OzAw8PXXX//111/L1C4AAIBGjz766KxZs8aOHfv7778riqIW1VvV
5+bmltjFKYRo0aLFnj17Dhw40LVr1yZNmty8efPy5cs//fTTmDFj7raIgICARx99NCwsTN0J
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
9rPnnntupqcAgN0JO/ZFU1NTCOHKs8PY/8r0KJ1r4Yrwq6dDF3ydEoCsIOzYd0M+Gyq+kOkh
OtfqDZmeAAD2zIcnAAAi4RU7gIPFvHnzbr/99paWlkwP0tnq6+tDCMlkpueA7CfsAA4WL7zw
Qm1tbaanyJgdjaFHItNDQJZzKhYAIBJd7hW7Hj16ZHqEGHTr1i3TI2RSIpGwkPZG6tPTXVZe
Xl5710kX/8nqsjr290lzc3MH7o2s0+XCros/03SUZNd+L0xzc7OFtDe6+BNMMpls7zrp4j9Z
XVbH/j7pgu/RpLUuF3Y7d+7M9Agx6OK/OJqamiykvdHFH6Xm5ub2PgJd/Cery+riPyl0LO+x
AwCIhLADAIiEsAMAiISwAwCIhLADAIiEsAMAiISwAwCIhLADAIiEsAMAiISwAwCIhLADAIiE
sAMAiISwAwCIhLADAIiEsAMAiISwAwCIhLADAIiEsAMAiISwAwCIhLADAIiEsAMAiISwAwCI
hLADAIiEsAMAiISwAwCIhLADAIiEsAMAiISwAwCIhLADAIiEsAMAiISwAwCIhLADAIiEsAMA
iISwAwCIhLADAIiEsAMAiISwAwCIhLADAIiEsAMAiISwAwCIhLADAIiEsAMAiISwAwCIhLAD
AIiEsAMAiISwAwCIhLADAIiEsAMAiISwAwCIhLADAIiEsAMAiISwAwCIhLADAIiEsAMAiISw
AwCIhLADAIhEXqYHyG61tbWzZs3atm1bpgfpbBs2bAghbO5y3/e+q6mpqa6uzvQUnS31o9Hc
kuk5ALoMYbdf/vKXvzzyyCOZniJjVm/I9ARZIplMnnzyybW1tZkeJDP+YZ0AdBanYvdLMpnM
9AiZ1LW/+3ZIJpNdtupCCLuaMj0BQJch7AAAIiHsAAAiIewAACIh7AAAIiHsAAAiIewAACIh
7AAAIiHsAAAiIewAACIh7AAAIiHsAAAiIewAACIh7AAAIiHsAAAiIewAACIh7AAAIiHsAAAi
IewAACIh7AAAIiHsAAAiIewAACIh7AAAIiHsAAAiIewAACIh7AAAIpGX6QE6QH19/bx58155
5ZXGxsZBgwZNmTKlb9++mR4KAKCzxfCK3Z133llTUzNz5sw5c+YUFRXdcMMNLS0tmR4KAKCz
ZX3Ybdq0acWKFd/5znfKy8v79+8/ZcqUqqqqV199NdNzAQB0tqwPu7Vr1+bn55eXl6e+7Nmz
54ABA954443MTgUA0Pmy/j12dXV1xcXFOTk56S0lJSUffPBB+sv7779/xYoVqcs9e/acPXt2
Bx69qKioA/eWdSr/Ecb8LNNDdK5/vx9CCEVFRSUlJXt/ry7+3oAPtne5ddLQGEII+fn57Von
IYS8vKz/nbw//vuOUNDFHoA11SGE0N510rampqYO3BtZJ4afodZV91Hr1q3729/+lrrcu3fv
/Pz8Djz0oEGDCgsLGxoaOnCfWeS9LeG9LZkeotMlEolBgwa1dyENGTLk9ddfP0AjHeQam8PT
qzM9RCYMGzasvetk2LBhTzzxxAGa5+D33D8zPUEmjBgxtGOfmOjicpLJZKZn2C/Lly+fM2fO
o48+ms67adOmjR49+mtf+9rH3n7Tpk2dOF20CgsLe/bsWV9f32Wjlr2Rk5NzyCGH7Nq1q66u
LtOzcFArKSnJz89///33s/0p6SBRVlaW6RHImKx/j92RRx7Z2Ni4bt261Jd1dXXvvPPOkCFD
MjsVAEDny/qwKy0tPeGEE+bOnfv2229XVVXdcccdRxxxxNFHH53puQAAOlvWn4oNIWzfvn3e
vHkrV65sbm4eOnTolClTevfuvacbOxXbIZyKZW84Fcteciq2YzkV25XF8OGJoqKiK6+8MtNT
AABkWNafigUAIEXYAQBEQtgBAERC2AEARELYAQBEQtgBAERC2AEARELYAQBEQtgBAERC2AEA
RELYAQBEQtgBAERC2AEARELYAQBEQtgBAERC2AEARELYAQBEQtgBAERC2AEARELYAQBEQtgB
AERC2AEARELYAQBEQtgBAERC2AEARELYAQBEQtgBAERC2AEARCInmUxmegayz+LFi+fMmTN9
+vRzzz0307Nw8Kqvrz///PNHjRp1yy23ZHoWDmrTp0//+9//vnjx4kQikelZILt5xY590djY
WFdXt2vXrkwPwkEtmUzW1dXt2LEj04NwsNuxY0ddXZ0XGmD/CTsAgEgIOwCASORlegCyUv/+
/SsqKgYMGJDpQTio5eXlVVRUHHXUUZkehIPdyJEjS0pKcnO91gD7y4cnAAAi4Z9HAACREHYc
WM3Nzeeff/6qVasO0P5ramrOP//89evXH6D902lSS+Xll1/O9CAcFKwH2DfeY5d9pk+f/u9/
//vuu+/u379/euPll18+duzYr3zlK23c8ZVXXikqKho4cOCBn/H/jpWbmzt79uzy8vJOOCgd
bvr06W+++eZuG6+44oozzjgjI/OQdVJL6M477zz88MPTG1taWiZOnLhly5bf/e533bp1y+B4
EB9hl5USicTcuXNnz57drns9/vjjo0aN6pywSx8rJydn2LBhnXBEDpBTTz314osvbr3lU5/6
VKaGIRuVlJRUVla2DruXX365ubk5gyNBxIRdVho3btzvf//7p59+uqKi4qPXbtmy5d577129
evW2bdsOP/zwSZMmDRkyZMaMGatXr161atWSJUvuuOOO9I2TyeS4ceOuvPLKysrKjRs3JhKJ
q666atmyZatWrdqyZcu4ceMuuOCCEMLmzZt//etfr169evv27QMHDpw8efIRRxyRuu+PfvSj
ysrKTZs2NTQ0XHLJJaeffnrrY912223jx4//6U9/OmLEiI8dbE872dNBQwhvvfXWL3/5y/Xr
13/mM5+58MILO+tR76J69OjRr1+/j25vY0l84nJav379fffd9+abb7a0tAwaNGjKlCm7HWJP
/+nJRl/84hefffbZSZMm5eV9+IxTWVk5fPjwF154IfWl9QAdyHvsslKPHj0mTZo0f/78Dz74
4KPX3njjjdu2bbv77rsfeuihwYMHX3/99XV1dbNnz+7Tp8/kyZNbV10IIScnJzc3d8mSJdde
e+28efN69eo1Y8aMIUOG3HXXXVdcccUDDzyQOkTq1cFf/OIXDz300NChQ2fNmrVr167UfR9/
/PHp06fPnTt3woQJv/rVrxoaGvZ0rI8dbE872dNBk8nkTTfdNGDAgAcffPC666576qmnDtzj
TBvaWBKfuJxuvvnm0tLS+fPnz58/v3v37rutkz3tvPO/RzrEkUceWVRUtGLFitSX9fX1L774
4kknnZS+gfUAHUjYZauKiorDDz983rx5u21/66231qxZc9lll5WUlCQSiW9+85stLS0vvfRS
23sbPXp0YWFhbm7u4MGDu3fvfsIJJ4QQjj766JaWlvfee2/dunVr1qyZPHlycXFxQUHBJZdc
0tTUtHz58tR9TzvttJKSkhDCiBEjdu7cWVNT87GHaHuwj+5kTwd94403ampqJkyYUFhY2KdP
n/POO28/HkX2UdtLou3lFEKYM2fO1KlTCwsLi4qKRo8evXbt2tZ/d6ntnZONxowZ8/TTT6cu
P//880OHDi0rK0tfaz1AB3IqNot9//vfnzZt2osvvnjsscemN1ZXV+fk5KT/dHBBQUGfPn32
FFtphxxySPr2paWlqcv5+fkhhF27dqXufumll7a+y8aNG1MX0r+g07f/2EO0PdhHd1JdXb2n
g+bk5PTt2ze1pfUnSDgQnnzyycWLF7fectttt7XxXyd80nIKIbz11lu//e1v33nnnRBCY2Nj
c3NzS0tLej/vvvtuGzsnG51xxhm/+c1vNm/e3Lt378rKyvHjx7e+1nqADiTssli/fv1SJy7n
zp2bk5Ozp5slk8mmpqa2d9XG3UMIBQUFIYTHHnssdaFd921D68E+upM9HfSZZ55pfXtvwT7Q
Tj755N3eyNivX7/3338/7OuSqK6uvv766y+++OKZM2cWFBQsX758t48Btb3eyEalpaXHHHPM
0qVLjzvuuOrq6i996Uvr1q1LXWU9QMdyKja7jR8/vqio6MEHH0z/yYD+/fsnk8nUv31DCA0N
DTU1NR/75ve9l3pV7O23305vSZ1Qa+9O2jXYng5aVlaWTCbTL/Vt2LChvZPQLsXFxYf9fwUF
BfuzJN58883m5ubx48ennqffeOON3W7QIeuNg82YMWOee+65ZcuWnXrqqelPUQTrATqasMtu
3bp1mzZt2pNPPpl6BSWEUF5ePnjw4Pvvv3/r1q0NDQ0LFizo3r378ccfH0JIJBLV1dXbtm1r
71EOPfTQ4cOH33ffff/5z3+am5sXL148bdq02traNu7y0WO1MVi7Djp48ODi4uJHHnmkvr6+
qqrqj3/8Y3u/HfbfPiyJtL59+7a0tPzzn/9sbGx87rnnXn/99RBC6/vuz845aI0aNWrz5s3L
li3b7bP81gN0LGGX9Y466qhzzjmn9cdjr7766ry8vO9973uTJ0+uqam5+eabi4qKQghnn332
k08+OW3atH04ylVXXVVWVjZt2rRvfOMbS5cunTVrVvq9Ux/rY4+1p8HaddCCgoKZM2euX79+
4sSJN99880UXXRRC8L887nztXRJpgwYNuuCCC2bPnj1x4sRVq1bNmDFj4MCBP/jBD1q/E3Sf
d85Bq1u3bqeddlpxcfFuf67ceoCOleMZEQAgDl6xAwCIhLADAIiEsAMAiISwAwCIhLADAIiE
sAMAiISwAwCIhLADAIiEsAMAiISwA/6fjRs3XnPNNcccc0yvXr3y8/P79+9/0UUXPfvsswfu
iBMmTOjZs+eB2z9A15GX6QGAg8iyZcvGjx+/devW884776KLLsrLy1u7du1jjz326KOP3njj
jTNmzMj0gAC0xf8rFvhQVVXVsGHDCgoKnnrqqREjRqS319bWjh079q9//evSpUtPPfXUDj/u
hAkTFi1aVF9f3+F7BuhqnIoFPnT77bdv3rz5nnvuaV11IYTS0tKHH374lltuKS8vT2989tln
x4wZ06tXr6KiopEjR86fPz991SmnnHLyySevXLnyjDPO6NWrV9++fS+++OKamprUtclk8oYb
bjj00EMLCwuHDRv22GOP7TZGG3s+6aSTTjnllEWLFh166KFf/vKXO/4hAMhyTsUCH/rDH/7w
6U9/ety4cR+9qry8/Mc//nH6y8rKyrPOOuvEE098+OGHE4nEwoULL7vsss2bN1911VUhhIKC
gjVr1nz3u9+96aabhg8f/vzzz3/9619PJBILFiwIIcyZM2fmzJmXXHLJxIkTa2trr7/++sbG
xr3ccyKR2LRp09VXX33NNdccdthhB/oBAcg6TsUCIYTQ1NSUn59/5plnPvXUU59445EjR27d
unXVqlVFRUWpLePGjVu6dGlNTU1hYWFFRUVlZeWf//znE088MXVtRUXF66+/XlVVlUwmBwwY
UFpa+uqrr6auqq6uPuywwwoKClKnYvdmzwsXLhw/fnzHPwQA2c+pWCCEELZt2xZCKC4ubr2x
rq7uX61s2LAhhFBTU7Ny5cqxY8fm5uY2/K9zzjln69at6VwrKipKV10IYcCAAe+9914I4Z13
3nn33XdPP/309FX9+vU79thjU5f3Zs8FBQXnnnvuAXwgALKZsANCCKG4uDg3N7e2trb1xnnz
5pW3cvzxx4cQ3n333RDCXXfd1b2VKVOmhBBS5RdC6NOnT+v95OXltbS0hBBSebfbtf37909d
2Js9l5WV5efnd/i3DxAH77EDQgghNzd36NChL7300s6dOxOJRGrjV7/61YEDB6Yu/+xnP6uq
qkrf/lvf+ta3v/3t3XaSvvGefOx7P5qbm1t/2faeVR1AG4Qd8KELL7zwuuuumz9//tSpU1Nb
Bg4cmC6qBQsWpMLuc5/7XAihubk59QJeu6Req0u9bpf2r3/9K3Vhf/YMQHAqFki7/PLLBwwY
cPXVVy9ZsmS3q1577bXVq1fn5uaGEEpLS4877rjHH398y5Yt6Rs88MADP/nJT5qamto+xOc/
//mysrI//elPqTOzIYQ1a9asWrUqdXl/9gxAEHZAWu/evRctWlRSUnLWWWedffbZN910089/
/vNrr732tNNO+8IXvrBz584HH3wwdctbb711+/bto0ePfuCBB5YsWXLttddOnjy5qqoqL+8T
TgLk5uZOnTp13bp1F1544cKFC++5554zzzxz5MiR6Rvs854BCE7FAq2NGDHitddeu/vuu594
4olbb711x44dZWVlw4YNmzt37qRJkwoLC1M3Gz169DPPPHPDDTdcfvnlDQ0N5eXls2fP/uEP
f7g3h5g5c2ZjY+OCBQsWLVo0aNCgO++8s7KyMv2h1/3ZMwD+jh0AQCScigUAiISwAwCIhLAD
AIiEsAMAiISwAwCIhLADAIiEsAMAiISwAwCIhLADAIiEsAMAiISwAwCIhLADAIiEsAMAiMT/
AEDdNy2uZIGiAAAAAElFTkSuQmCC"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Count of Gender(Male and Female) in Chicago</span>
<span class="n">total_chi</span> <span class="o">=</span> <span class="nf">sort</span><span class="p">(</span><span class="nf">table</span><span class="p">(</span><span class="n">city2</span><span class="o">$</span><span class="n">Gender[city2</span><span class="o">$</span><span class="n">City</span> <span class="o">==</span> <span class="s">&#39;Chicago&#39;</span><span class="n">]</span><span class="p">))</span>
<span class="nf">print</span><span class="p">(</span><span class="n">total_chi</span><span class="p">)</span>

<span class="c1"># percentage of Gender(Male and Female) in Chicago</span>
<span class="nf">round</span><span class="p">((</span><span class="n">total_chi</span> <span class="o">/</span> <span class="nf">length</span><span class="p">(</span><span class="n">city2</span><span class="o">$</span><span class="n">Gender[city2</span><span class="o">$</span><span class="n">City</span> <span class="o">==</span> <span class="s">&#39;Chicago&#39;</span><span class="n">]</span><span class="p">)</span> <span class="o">*</span> <span class="m">100</span><span class="p">),</span> <span class="n">digits</span> <span class="o">=</span> <span class="m">2</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>
Female          Male 
  1723   1748   5159 
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_text output_subarea ">
<pre>
Female          Male 
 19.97  20.25  59.78 </pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="c1"># Count of Gender(Male and Female) in New York City</span>
<span class="n">total_ny</span> <span class="o">=</span> <span class="nf">sort</span><span class="p">(</span><span class="nf">table</span><span class="p">(</span><span class="n">city2</span><span class="o">$</span><span class="n">Gender[city2</span><span class="o">$</span><span class="n">City</span> <span class="o">==</span> <span class="s">&#39;New York City&#39;</span><span class="n">]</span><span class="p">))</span>
<span class="nf">print</span><span class="p">(</span><span class="n">total_ny</span><span class="p">)</span>

<span class="c1"># percentage of Gender(Male and Female) in Chicago</span>
<span class="nf">round</span><span class="p">((</span><span class="n">total_ny</span> <span class="o">/</span> <span class="nf">length</span><span class="p">(</span><span class="n">city2</span><span class="o">$</span><span class="n">Gender[city2</span><span class="o">$</span><span class="n">City</span> <span class="o">==</span> <span class="s">&#39;New York City&#39;</span><span class="n">]</span><span class="p">)</span> <span class="o">*</span> <span class="m">100</span><span class="p">),</span> <span class="n">digits</span> <span class="o">=</span> <span class="m">2</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>
       Female   Male 
  5410  12159  37201 
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_text output_subarea ">
<pre>
       Female   Male 
  9.88  22.20  67.92 </pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>
In Chicago and New York City, number of users:
Male : 42360 (66.81%)
Female : 13882 (21.90%)
Not Mentioned: 7158 (11.29%)
In New York City,users gender summary are; 67.92% of Male , 22.20% of Female and 9.88% of Not Mentioned'.
While chicago recorded 59.78% of Male , 19.97% of Female and 20.25% of Not Mentioned.</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Finishing-Up">Finishing Up<a class="anchor-link" href="#Finishing-Up">&#182;</a></h2><blockquote><p>Congratulations!  You have reached the end of the Explore Bikeshare Data Project. You should be very proud of all you have accomplished!</p>
<p><strong>Tip</strong>: Once you are satisfied with your work here, check over your report to make sure that it is satisfies all the areas of the <a href="https://review.udacity.com/#!/rubrics/2508/view">rubric</a>.</p>
</blockquote>
<h2 id="Directions-to-Submit">Directions to Submit<a class="anchor-link" href="#Directions-to-Submit">&#182;</a></h2><blockquote><p>Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).</p>
<p>Alternatively, you can download this report as .html via the <strong>File</strong> &gt; <strong>Download as</strong> submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.</p>
<p>Once you've done this, you can submit your project by clicking on the "Submit Project" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!</p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-r"><pre><span></span><span class="nf">system</span><span class="p">(</span><span class="s">&#39;python -m nbconvert Explore_bikeshare_data.ipynb&#39;</span><span class="p">)</span>
</pre></div>
<div> Your project has been completed</div>
<div> You can close your browser</div>

</div>
</div>
</div>

</div>
    </div>
  </div>
</body>

 


</html>
