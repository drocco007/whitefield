<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
  <head>
    <title>${c.title}</title>
        ${h.stylesheet_link("/css/style.css", "/css/schedule.css",
            "css/ui-lightness/jquery-ui-1.8.custom.css")}
        ${h.javascript_link("/js/jquery-1.4.2.min.js", "/js/jquery-ui-1.8.custom.min.js", "js/whitefield.js")}
        ${h.stylesheet_link("/print.css", media="print")}
  </head>

  <body>
    <div id="wrap">
      <div id="header">
        <h1 id="sitename"><span class="big">Whitefield</span>
          <span class="logosmall">Whitefield Academy Class Schedule</span></h1>
        <div id="navigation">

          <%
             def active(school):
                if c.schedule.school == school:
                    return "active"

                return ""
          %>
        
          <ul>
            <li class="${active('us')}"><a href="/us/${c.schedule.date}">Upper School</a></li>
            <li class="${active('ms')}"><a href="/ms/${c.schedule.date}">Middle School</a></li>

          </ul>
        </div>
        
        <div class="clear"></div>
      </div>

      <div class="contents">
        ${next.body()}\

        <div class="clear"></div>
      </div>

    </div>

    <div id="footer">
      Copyright &copy; 2010&ndash;2011 Daniel J. Rocco
      | <a href="http://www.whitefieldacademy.com/ClassSchedule.aspx">Source
        Data</a>
      
      <div id="templateinfo">
        Buttons by <a href="http://cooltext.com/">Cool Text</a> | 
        <a href="http://www.ramblingsoul.com">Original CSS Template</a> by Rambling Soul
      </div>
    </div>
  </body>
</html>

