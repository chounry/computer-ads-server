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

	// --------- for fold the spec table
	var continue_display_btn = $('#continue-display-btn');
	var last_row_container = $('#last-row-container');

	continue_display_btn.attr('display','false');
	continue_display_btn.click(function(){
		$('#second-display').css('display','unset');
		continue_display_btn.removeAttr('id');
		continue_display_btn.attr('display','true');
	})

	last_row_container.click(function(){
		$("#second-display").css('display','none');
		continue_display_btn.attr('id','continue-display-btn');
		continue_display_btn.attr('display','false');
	})


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
	// ----------- End product picture slide ------------
	

	// ----------- Supported product -----------
	// function putNewPro(section, newProArr){
	// 	$(section).empty();
	// 	$(section).append(newProArr);	
	// }

	// // --- CPU ---
	// var cpu_section = $(".all_pro_cont ul"); 
	// var curr_cpu = $(".all_pro_cont ul li:not('.test')");
	// var cpu_arr = $(".all_pro_cont ul li");
	// var cpu_sli_btn = $(".sli_cpu");
	// var cpu_pos = {
	// 	"start":0,
	// 	"end":2
	// }

	// // this 2 lines below dosen't use when there is server
	// cpu_section.empty();
	// cpu_section.append($(curr_cpu));
	
	// // listen for click;
	// cpu_sli_btn.click(function(){
	// 	console.log("Click");
	// 	if(this.dataset.to == "left"){
	// 		console.log("left")
	// 		if(cpu_pos.start < 2){
	// 			return;// it will request from server,
	// 		}else{
	// 			cpu_pos.start -= 2;
	// 			cpu_pos.end -= 2;
	// 		}
			
	// 	}else{
	// 		if(cpu_pos.end == cpu_arr.length){
	// 			return; // it will request from server,
	// 		}else{
	// 			cpu_pos.start += 2;
	// 			cpu_pos.end += 2;
	// 		}
	// 	}
	// 	// put the new product in
	// 	curr_cpu = cpu_arr.slice(cpu_pos.start,cpu_pos.end);
	// 	putNewPro(cpu_section,curr_cpu);
	// })
    
})