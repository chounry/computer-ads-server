

$(document).ready(function(){

    // <------------- handle filter on the top
    var del_btns = $('.del-tag-icon');
    var all_checkBoxes = $('.each_filter_cont input');

    del_btns.click(function(){
        // get the query parameter in the url
        var queryParams = queryConvert();
        var selectedName = this.nextElementSibling.innerText;

        unCheckBox(selectedName);
        this.parentElement.remove();

    });

    function joinQuery(arr){
        var query = "?";
        arr.forEach(ele => {
            if(ele != null){
                ele.forEach(e =>{
                    query +=  e;
                })
            }
        });

        
    }

    function unCheckBox(name){
        for(i = 0;i<all_checkBoxes.length;i++){
            if(all_checkBoxes[i].value == name){
                all_checkBoxes[i].toggleAttribute('checked');
            }
        }
    }


    var queryConvert = function(){
        var queryStr = window.location.search,
        queryArr = queryStr.replace('?','').split('&'),
        queryParams = [];
        
    
        for (var q = 0, qArrLength = queryArr.length; q < qArrLength; q++) {
            var qArr = queryArr[q].split('=');
            if(queryParams[qArr[0]] == null)
                queryParams[qArr[0]] = Array();

            queryParams[qArr[0]].push(qArr[1]);
            
        }
        console.log(queryParams['form_factor']);
        return queryParams;
    }

    $('#clear_btn').click(function(){

    })

    // END handle filter on the top --------------------->

})