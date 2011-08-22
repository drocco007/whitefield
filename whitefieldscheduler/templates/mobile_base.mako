<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="initial-scale=1.0,maximum-scale=1.0,height=device-height,width=device-width,user-scalable = no">
      <title>${c.title}</title>

      <link rel="stylesheet" href="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.css" />
      ${h.stylesheet_link("css/jquery.ui.datepicker.mobile.css")}

      <script type="text/javascript" src="http://code.jquery.com/jquery-1.5.2.min.js"></script>
      <script>
                //reset type=date inputs to text
                $( document ).bind( "mobileinit", function(){
                        $.mobile.page.prototype.options.degradeInputs.date = true;
                });
        </script>
        <script type="text/javascript" src="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.js"></script>


        <!--${h.stylesheet_link("css/ui-lightness/jquery-ui-1.8.custom.css", "css/jquery.ui.datepicker.mobile.css")}-->
        <!--${h.stylesheet_link("/quick.css", "css/ui-lightness/jquery-ui-1.8.custom.css")}-->
        ${h.stylesheet_link("quick.css")}
        ${h.javascript_link("js/jquery-ui-1.8.custom.min.js", "js/jquery-mobile-swipe-up-down.js", "js/date.js")}
        <script src="js/jquery.ui.datepicker.mobile.js"></script>
        ${h.stylesheet_link("/print.css", media="print")}
  </head>

  <body>
    <div class="content">
      ${next.body()}\
    </div>
  </body>
</html>
