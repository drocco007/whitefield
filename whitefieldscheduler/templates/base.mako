<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
        "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
<head>
    <title>${c.title}</title>

    <!--#"/css/reset.css", "/css/style.css",-->

    ${h.stylesheet_link("/css/schedule.css", "/css/ui-lightness/jquery-ui-1.8.custom.css")}
    ${h.javascript_link("/js/jquery-1.4.2.min.js", "/js/jquery-ui-1.8.custom.min.js", "/js/whitefield.js")}
    ${h.stylesheet_link("/print.css", media="print")}

    <link href="/css/screen.css" media="screen, projection" rel="stylesheet" type="text/css"/>
    <link href="/css/print.css" media="print" rel="stylesheet" type="text/css"/>
    <!--[if lt IE 8]>
        <link href="/css/ie.css" media="screen, projection" rel="stylesheet" type="text/css"/>
    <![endif]-->
</head>

<body class="bp two-col">
    <div id="container">
        <div id="header">
            <!-- Header -->

            <h1 id="sitename"><span class="big .large">Whitefield</span>
                <span class="logosmall .small">Whitefield Academy Class Schedule</span></h1>

            <div>
                <%
                def active(school):
                    if c.schedule.school == school:
                        return "active"

                    return ""
                %>

                <div class="clear"></div>

                <nav id="docs-nav" role="navigation">
                    <a class="button ${active('us')}" href="/us/${c.schedule.date}">Upper School</a>
                    <a class="button ${active('ms')}" href="/ms/${c.schedule.date}">Middle School</a>
                </nav>

                <div id="search">
                    <form class="bp" id="searchForm" action="/${c.schedule.school}/">
                        <input type="text" id="date" name="date" title="Jump to date" accesskey="f" value=""
                                placeholder="Go to date: yesterday, May 4, 2011, Thursday, ..."/>
                    </form>
                </div>
            </div>
        </div>

        <div id="content">
            ${next.body()}\
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
    </div>
</body>
</html>

