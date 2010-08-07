<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
  <head>
    <title>${c.title}</title>
        ${h.stylesheet_link("/quick.css", "css/ui-lightness/jquery-ui-1.8.custom.css")}
        ${h.javascript_link("/js/jquery-1.4.2.min.js", "/js/jquery-ui-1.8.custom.min.js", "js/whitefield.js")}
        ${h.stylesheet_link("/print.css", media="print")}
  </head>

  <body>
    <div class="content">
      ${next.body()}\
    </div>
  </body>
</html>

