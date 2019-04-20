$(document).ready(function(){

	//<----------- markdown

	var markdown_contents = $('.markdown-content');
	markdown_contents.each((i, e) => {
		var text = e.innerText;
		var markedContent = marked(text);
		console.log(markedContent);
		$(e).html(markedContent);
	});

	// end markdown 

	// <--------- for fold the spec table
	var see_more_btn = $('#see-more-btn');
	var last_row_container = $('#last-row-container');

	see_more_btn.attr('display','false');

	see_more_btn.click(function(){
		if(screen.width < 1025){
			$('#second-display').css('display','unset');
			see_more_btn.removeAttr('id');
			see_more_btn.attr('display','true');
		}
	})

	last_row_container.click(function(){
		if(screen.width < 1025){
			$("#second-display").css('display','none');
			see_more_btn.attr('id','see-more-btn');
			see_more_btn.attr('display','false');
		} 
	})
	window.addEventListener('resize',function(){
		if(screen.width > 1024){
			$('#second-display').css('display','unset');
			see_more_btn.removeAttr('id');
			see_more_btn.attr('display','true');
		}
	})

	// end fold spec table ------------------>


	// ---------- Product picture slide --------------
	/// initial data set

	var all_img = $("#pho_change ul li img");
	var main_pic = $("#sli_pic");
	main_pic.css("background-image",`url('${all_img[0].currentSrc}')`);

	var cur_img_index = 0;
	var img_len = all_img.length;
	var sli_button = $("#sli_pic div");

	all_img.each((i,ele) => {
		ele.setAttribute('data-pos',i+'');	
	});

	function setImg(ele){
		// set the background image for main_pic and border for image that is seleted

		main_pic.css("background-image",`url('${ele.currentSrc}')`);
		$(ele).parent().parent().children().attr("style","");
		$(ele).parent().css("border-color","#348899");
	}

	all_img.click(function(){
		cur_img_index = this.dataset.pos;
		setImg(this);
	})

	// listen for click on slide button 
	sli_button.click(function(){
		// keep looping the index <==
		if(this.dataset.to == "right"){
			cur_img_index++; 		
			cur_img_index %= img_len;
		}
		else if(this.dataset.to == "left"){
			console.log(cur_img_index);
			cur_img_index--;
			cur_img_index = cur_img_index == -1 ? img_len-1 : cur_img_index;
		} 
		// <==

		var next_img;
		$.each(all_img,function(){
			if(this.dataset.pos == cur_img_index){
				next_img = this;
			}
		})
		setImg(next_img);
	})
    
})