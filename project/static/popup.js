 $(window).load(function() {    

            var theWindow        = $(window);
                                
            function posPopup(){

                if( $(window).width() > 750 ){
                  $('.popup').css('height', '400px');
                }
                else{
                  $('.popup-bar').css('left', 0);
                  $('.popup-bar').css('top', '50px');
                }

                boxWidth = $('.popup').width();
                boxHeight = $('.popup').height();

                winWidth = $(window).width();
                winHeight = $(window).height();

                width = (winWidth - boxWidth) / 2;
                height = (winHeight - boxHeight) / 2;

                $('.popup').css({ 'left': width+'px', 'top': height+'px' });
            }

            theWindow.resize(posPopup).trigger("resize");

        });
