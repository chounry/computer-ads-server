var market_form_box = $('.market-each-box').hide();

$(document).ready(function(){
    init_page()

    var market_form_html = market_form_box[0].outerHTML;

    function init_page(){            
        var input_files = $('input[type="file"]');
        input_files.hide(); 
        $('.market-each-box .control-label').remove();
        market_form_box.find('input').attr('required','');
        market_form_box.remove();    
    }

    $('#add_market_btn').click(function(e){
        if(!isMaketFormEmp()){
            var tmp = $(market_form_html).show();
            console.log(tmp.find('select'));
            tmp.insertBefore($('#market_form_btn'));
        }
    })

    $('#remove_market_btn').click(function(){
        var all_market_boxes = $('.market-each-box');
        $(all_market_boxes[all_market_boxes.length-1]).remove();
    })

    $('div.form_img_box').click(function(e){
        var input_file = $(this).find("input[type=file]");
        var a_tag = $(this).find('a');
        if (!$(e.target).is('input[type=file]')) {
            input_file.trigger('click');
        }
        input_file.change(function(){
            var reader = new FileReader()
            reader.readAsDataURL(input_file[0].files[0])
            reader.onload = function(){
                a_tag.css("background-image","url('"+ reader.result +"')");
                a_tag.css('background-color','white');
            }
        })
    })

    function isMaketFormEmp(){
    // check whether the market form input is empty to prevent many empty box
        var all_selects = $.makeArray($('.market-each-box select'));
        var all_inputs = $.makeArray($('.market-each-box input'));

        for(var i=0;i<all_selects.length;i++){
            if(!all_selects[i].value)return true;
        }

        for(var i=0;i<all_inputs.length;i++){
            if(!all_inputs[i].value)return true;
        }
        return false;
    }

})