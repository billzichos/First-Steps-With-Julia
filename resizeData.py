

<!DOCTYPE html>

<!--[if lt IE 7 ]><html class="ie ie6 lte7 lte8 lte9"><![endif]-->
<!--[if IE 7 ]><html class="ie ie7 lte7 lte8 lte9"><![endif]-->
<!--[if IE 8 ]><html class="ie ie8 lte8 lte9"><![endif]-->
<!--[if IE 9 ]><html class="ie ie9 lte9"><![endif]-->
<!--[if (gt IE 9)|!(IE)]><!--><html ><!--<![endif]-->

<head>
    <link href='//fonts.googleapis.com/css?family=Merriweather:400,700|Open+Sans:300,400italic,700italic,400,700' rel='stylesheet' type='text/css'> 

    
    <link rel="stylesheet" href="/content/v/bbdad30669ee/shared/css/font-awesome.min.css">

    
    
    <title>Competition Rules - First Steps With Julia | Kaggle</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="robots" content="index, follow" />
    <link href="/content/v/4e3f994e938b/kaggle/favicon.ico" rel="shortcut icon" type="image/x-icon" />

    
        <meta name="keywords" content="Kaggle, data science, big analytics, data mining, forecasting, statistics, prediction, bioinformatics, competitions, contests, crowdsourced analytics" />
            <meta name="description" content="Kaggle is a platform for data prediction competitions. Companies, organizations and researchers post their data and have it scrutinized by the world&#39;s best statisticians." />

            <link rel="stylesheet" href="/content/v/a5d7b97da053/shared/css/base.less" type="text/css" />
        <link rel="stylesheet" href="/content/v/4b4de64aa988/kaggle/css/kaggle-site.less" type="text/css" />

        <script type="text/javascript" src="/content/v/47b68dce8cb6/shared/js/jquery-1.7.2.min.js"></script>
            <script type="text/javascript" src="/content/v/7846b5904b60/shared/js/jquery-ui-1.9.2.min.js"></script>

    
        <script type="text/javascript" src="/content/v/a60ecf3c5c7d/shared/js/kaggle.min.js"></script>
        <script type="text/javascript">
            
            Kaggle.Current.siteId = 1;
                Kaggle.Current.competitionId = 3947;
                            Kaggle.Current.userId = 137597;
        </script>

    
    <!--[if (gte IE 6)&(lte IE 8)]>
        <script type="text/javascript" src="/content/v/f1f17fea7cee/shared/js/ie/selectivizr.min.js"></script>
    <![endif]-->

    
                                            <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>
    
                                                                    
                    <link rel="apple-touch-icon" href="/content/v/1e4cdaa83f46/kaggle/img/apple-touch-icon.png" />


    
    <!--[if lt IE 9]>
        <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    
</head>
<body class="logged-in    kaggle">
    <div id="watermark1" class=""></div>
    <div id="watermark2" class=""></div>
    <div id="wrap"><!-- needed for sticky footer -->
<div id="menu-open-overlay"></div>

<div id="header2" class="">
    <div id="header2-inside">
        <a id="logo" href="/"><img alt="Kaggle" height="86" src="/content/v/d6801c936e94/kaggle/img/site-logo.png" width="240" /></a>

            <ul id="header-ul">
                <li>
  <a href="/solutions/competitions">Host</a>
</li>
<li>
  <a href="/competitions">Competitions</a>
</li>
<li>
  <a href="/scripts">Scripts</a>
</li>
<li>
  <a href="/jobs">Jobs</a>
</li>
<li>
<a href="">Community &#9662;</a>
<ul>
  <li><a href='/users'>User Rankings</a></li>
  <li><a href='/forums'>Forum</a></li>
  <li><a href="http://blog.kaggle.com" target="_blank">Blog</a></li>
  <li><a href='/Wiki'>Wiki</a></li>
</ul>
</li><!-- <script>
  $(function(){
    if (!$('body.logged-in').length) {
      $('a.logged-in-only').hide().parent().next().find('a').css('padding-top','10px');
    }
  });
</script> -->
            </ul>

        <script>
            jQuery(function () {
                jQuery('#header-ul li:has(ul) > a').click(function (e) {
                    e.preventDefault();

                    jQuery('#header-ul li').not(jQuery(this).parent()).find('ul').removeClass('open');
                    jQuery(this).parent().find('ul').toggleClass('open');
                    jQuery('#menu-open-overlay').show();
                });

                jQuery('#menu-open-overlay').click(function () {
                    jQuery('#header-ul ul').removeClass('open');
                    jQuery('#top-bar-signin').hide();
                    jQuery(this).hide();
                });

            });
        </script>

        <ul id="header-control">
                <li id="header-account"><a class="profilelink" href="/users/137597/bill-zichos" title="View my profile">Bill Zichos</a></li>
                <li id="header-logout"><a href="/account/logoff" class="logout-link">Logout</a></li>
        </ul>
    </div>
</div>







        <div class="message information"><div class="message-inside">We are making our URLs prettier -- <a href="/account/set-username">Claim your personal URL now</a>!</div></div><div class="message warning"><div class="message-inside">You must accept this competition's rules before you'll be able to download files.</div></div>    <script type="text/javascript">
        jQuery(function($) {
            $('body').on('click', '.message .remove-button', function () {
                $(this).parent().fadeOut(1000, function () {
                    $(this).remove();
                });
                    
                
                $.post('/notifications/messages/' + $(this).data('messageid') + '/dismiss', function (data) {
                    
                });
            });
        });
    </script>


        <!-- header-inside and header -->
            <div id="main">
                





<div id='competition' @Html.Attr('class', 'prospecting', competition.InProspectingPhase).Add(isPreview ? 'preview' : '')>                <header id="comp-header" >
                    <a href="/c/street-view-getting-started-with-julia"><img id="comp-image" src="https://kaggle2.blob.core.windows.net/competitions/kaggle/3947/logos/front_page.png" alt="" /></a>
                    <div id="comp-header-details">
                        <h2>

                    Knowledge 
                        &bull; <a href="/c/street-view-getting-started-with-julia/leaderboard">65 teams</a>
                </h2>
                <h1><a href="/c/street-view-getting-started-with-julia">First Steps With Julia</a>
                        </h1>

                        

                            <div id="comp-header-stats" >
                                    <div id="comp-header-stats-progress-section">
                                        <div id="comp-header-stats-progress">
                                            <div id="comp-header-stats-teams" style="width:66%">
                                            </div>
                                        </div>
                                        <div id="comp-progress-start"></div>
                                        <div id="comp-progress-end" ></div>





                                    </div>

                                <div id="comp-header-stats-start">
                                    Mon 4 Aug 2014
                                </div>
                                <div id="comp-header-stats-end">
                                    Thu 31 Dec 2015
                                        <span class="to-go-note">
                                            (5 months to go)
                                        </span>
                                </div>
                            </div>
                    </div>
                </header>
                <script type="text/javascript">
                    jQuery(function ($) {
                        $('#comp-header-details h1').textfill({ maxFontPixels: 26, innerTag: 'a' });
                    });
                </script>
            <div class="comp-sidebar">
                

<div class="_panel" id="competition-dashboard">
    <header>
        <h1>Dashboard</h1>
    </header>
    <ul id="competition-dashboard-dropdown">
        <li class="cd-home"><a href="/c/street-view-getting-started-with-julia">Home</a>
            <ul>
                <li class="cd-data"><a href="/c/street-view-getting-started-with-julia/data">Data</a></li>

                    <li class="cd-submit submission-link">
                        <a class="comp-link" href="/c/street-view-getting-started-with-julia/submit">Make a submission</a>
                    </li>
            </ul>
        </li>
        
        <li class="cd-info">
            <a id="open-info">Information</a>
            <ul id="pages-flyout">
                    <li>
<a href="/c/street-view-getting-started-with-julia">Description</a>                    </li>
                    <li>
<a href="/c/street-view-getting-started-with-julia/details/evaluation">Evaluation</a>                    </li>
                    <li>
<a href="/c/street-view-getting-started-with-julia/rules">Rules</a>                    </li>
                    <li>
<a href="/c/street-view-getting-started-with-julia/details/julia-tutorial">Julia Tutorial</a>                    </li>
                    <li>
<a href="/c/street-view-getting-started-with-julia/details/knn-tutorial">kNN Tutorial</a>                    </li>

            </ul>
        </li>

            <li class="cd-forum"><a href="/c/street-view-getting-started-with-julia/forums">Forum</a></li>


            <li class="cd-leaderboard">
                <a href="/c/street-view-getting-started-with-julia/leaderboard">Leaderboard</a>
            </li>

        
                <li class="cd-submissions"><a href="/c/street-view-getting-started-with-julia/submissions">My Submissions</a></li>
        
        
    </ul>
</div>

    <script type="text/javascript">
        $(function () {
            $(".cd-home").addClass("selected");
        });
    </script>

                


    <div class="widget _panel" id="compside-discussions">
        <header>
            <h1><a href="/c/street-view-getting-started-with-julia/forums">Forum (18 topics)</a></h1>
        </header>

        <ul>
                <li>
                    <div class="post-title"><a href="/c/street-view-getting-started-with-julia/forums/t/14877/pickling-a-model/82837#post82837">Pickling  A Model</a></div>
                    <div class="post-time">12 days ago</div>
                </li>
                <li>
                    <div class="post-title"><a href="/c/street-view-getting-started-with-julia/forums/t/14818/imread-not-defined/82589#post82589">imread not defined</a></div>
                    <div class="post-time">17 days ago</div>
                </li>
                <li>
                    <div class="post-title"><a href="/c/street-view-getting-started-with-julia/forums/t/10023/warnings-on-using-dataframes/81255#post81255">Warnings on &quot;using DataFrames&quot;</a></div>
                    <div class="post-time">31 days ago</div>
                </li>
                <li>
                    <div class="post-title"><a href="/c/street-view-getting-started-with-julia/forums/t/14118/installation-problems-not-a-git-repository/78114#post78114">Installation problems: &quot;Not a git repository&quot;</a></div>
                    <div class="post-time">58 days ago</div>
                </li>
                <li>
                    <div class="post-title"><a href="/c/street-view-getting-started-with-julia/forums/t/13487/matlab-treebagger/75200#post75200">Matlab TreeBagger</a></div>
                    <div class="post-time">2 months ago</div>
                </li>
                <li>
                    <div class="post-title"><a href="/c/street-view-getting-started-with-julia/forums/t/13121/scaleminmax-issue/68862#post68862">ScaleMinMax - issue </a></div>
                    <div class="post-time">3 months ago</div>
                </li>
        </ul>

    </div> 
                    <div id="partial-stats-ticker"></div>
                    <script type="text/javascript">
                        jQuery(function ($) {
                            $("#partial-stats-ticker").load("/c/3947/partial/stats");
                        });
                    </script>
            </div>
    <div class="rules comp-content with-sidebar _panel">
            <header class='info'>
                <div class="simple-steps">
                    <a class="info" href="/c/street-view-getting-started-with-julia">Competition Details</a>
                    &raquo;
                    <a class="data" href="/c/street-view-getting-started-with-julia/data">Get the Data</a>
                        &raquo;
                        <a class="submit" href="/c/street-view-getting-started-with-julia/submit">Make a submission</a>
                </div>
                    </header>
                <div class="comp-content-inside">
                    <div id="competition-intro">

                    </div>

                        <div id="comp-homepage-content" class="cms-page _buttons">
                            



<h1 class="page-name">Competition Rules</h1>

<ul id="standard-rules">
    <li>
        <h3>One account per participant</h3>
        <p>You cannot sign up to Kaggle from multiple accounts and therefore you cannot submit from multiple accounts.</p>
    </li>

        <li>
            <h3>No private sharing outside teams</h3>
            <p>
                Privately sharing code or data outside of teams is not permitted.
                It's okay to share code if made available to all participants on the forums.
            </p>
        </li>


    <li>
        <h3>Team Mergers</h3>
            <p>
                Team mergers are allowed and can be performed by the team leader. In order to merge, the combined team must have a total submission count less than or equal to the maximum allowed as of the merge date. The maximum allowed is the number of submissions per day multiplied by the number of days the competition has been running.<br/>
            </p>
    </li>

    <li>
        <h3>Team Limits</h3>
            <p>There is no maximum team size.</p>
    </li>

    
    <li>
        <h3>Submission Limits</h3>
        <p>You may submit a maximum of 5 entries per day.</p>

            <p>You may select up to 2 final submissions for judging.</p>
    </li>
    
    
</ul>
        <div class="rules-dates">
            <h3>Competition Timeline</h3>
            <div>Start Date: <strong>8/4/2014 3:52:06 PM UTC</strong></div>
            <div>Merger Deadline: <strong>None</strong></div>
            <div>First Submission Deadline: <strong>None</strong></div>
            <div>End Date: <strong>12/31/2015 11:59:00 PM UTC</strong></div>
        </div>
        <div class="_buttons" style="margin-top:3em;">
            <h2 style="margin-bottom:1em;">Rules Acceptance</h2>
    
<form action="/c/street-view-getting-started-with-julia/rules/accept" method="post"><input name="__RequestVerificationToken" type="hidden" value="G4XkC4cgeQMHvK5oKVlrbt3wPbxplWex2X582QS9aLu1iW8gJxfnRq1RdlwEd2vbDANse-IfUzZWvNDQ6qXbghdbS-41" />                    <input type="submit" name="doAccept" value="I understand and accept" />
                    <input type="submit" id="do-not-accept" name="doNotAccept" value="I do not accept" /> 
                    <p><small>By clicking on the "I understand and accept" button below, you are indicating that you agree to be bound to the above rules.</small></p>       
</form>        </div>

                        </div>
                </div>
            </div>  
        </div>
    


            </div>
    </div> <!-- wrap -->
    <div id="footer">
        <div id="footer-inside">
            <div id="footer-social">
                    <div id="social-links">
            <a class="twitter" href="http://www.twitter.com/kaggle" title="Follow Kaggle on Twitter"></a>     
                    <a class="facebook" href="http://www.facebook.com/kaggle" title="Follow Kaggle on Facebook"></a>           
                    <a class="linkedin" href="http://www.linkedin.com/companies/kaggle" title="Follow Kaggle on LinkedIn"></a>        
    </div><!-- social-links -->

            </div>
            <div id="footer-copyright">
                


&copy; 2015 Kaggle Inc            </div>
            <div id="footer-links">
                <a href="/about">About</a>
<a href="/team">Our Team</a>
<a href="/careers">Careers</a>
<a href="/terms">Terms</a>
<a href="/privacy">Privacy</a> 
<!--<a href="/Home/ContactPress">Press</a>-->
<a href="/Home/contact">Contact/Support</a>
            </div> <!-- footer-links -->
        </div> <!-- footer-inside -->
    </div> <!--footer-->

        <script type="text/x-mathjax-config">
            MathJax.Hub.Config({
                "HTML-CSS": {
                    preferredFont: "TeX",
                    availableFonts: ["STIX","TeX"],
                    linebreaks: {
                        automatic: true
                    },
                    EqnChunk: (MathJax.Hub.Browser.isMobile ? 10 : 50)
                },
                tex2jax: {
                    inlineMath: [ ["\\\\(","\\\\)"] ],
                    displayMath: [ ["$$","$$"], ["\\[", "\\]"] ],
                    processEscapes: true,
                    ignoreClass: "tex2jax_ignore|dno"
                },
                TeX: {
                    noUndefined: {
                        attributes: {
                            mathcolor: "red",
                            mathbackground: "#FFEEEE",
                            mathsize: "90%"
                        }
                    }
                },
                messageStyle: "none"
            });
        </script>
        
        <script type="text/javascript">
            var _gaq = _gaq || [];
            _gaq.push(['_setAccount', 'UA-12629138-1']);
            _gaq.push(['_trackPageview']);
            _gaq.push(['_trackPageLoadTime']);
            _gaq.push(['_setCustomVar', 1, 'usertype', 'registered', 2]);
                _gaq.push(['_setCustomVar', 2, 'userid', '137597', 2]);
            (function () {
                var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
            })();
        </script>
        <script type="text/javascript">
            /**
        * Function that tracks a click on an outbound link in Google Analytics.
        * This function takes a valid URL string as an argument, and uses that URL string
        * as the event label.
        * See: https://support.google.com/analytics/answer/1136920?hl=en
        */
            var trackOutboundLink = function(url) {
                ga('send', 'event', 'outbound', 'click', url, {'hitCallback':
                        function () {
                            document.location = url;
                        }
                });
            }
        </script>


    

    <!-- Cheers, RD00155D486538p. -->
</body>
</html>
