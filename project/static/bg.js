    $(window).load(function() {    


            var theWindow        = $(window),
                $bg              = $("#bg"),
                aspectRatio      = $bg.width() / $bg.height();

            width = theWindow.width();


            if(width > 2200){ img_id = 3680 }

            if(width >= 1500 && width <= 2200){ img_id = 1920 }
            if(width >= 1000 && width < 1500){ img_id = 1366 }    
            if(width >= 600 && width < 1000){ img_id = 900 }

            if(width < 600){ img_id = 480 }    

            bg_img = 'static/img/bg' + img_id + '.jpg';

            $bg.attr('src', bg_img);
                                    
            function resizeBg() {

                max = $(window).width();
            
                if ( (theWindow.width() / theWindow.height()) < aspectRatio ) {

                    $bg
                        .removeClass()
                        .addClass('bgheight');

                    $bg.css('max-width', max);

                } else {
 

                    $bg
                        .removeClass()
                        .addClass('bgwidth');

                    $bg.css('max-width', max);
                }
                        
            }
                                
            theWindow.resize(resizeBg).trigger("resize");

        });