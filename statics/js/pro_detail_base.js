$(document).ready(function(){
	// ---------- Product picture slide --------------
	var all_img = $("#pho_change ul li img");
	var main_pic = $("#sli_pic");
	console.log(all_img[0].currentSrc);
	main_pic.css("background-image",`url('${all_img[0].currentSrc}')`);

	var cur_img = 1;
	var img_len = all_img.length;
	var sli_button = $("#sli_pic div");

	// set the background image for main_pic and border for 
	// image that is seleted
	function setImg(ele){
		main_pic.css("background-image",`url('${ele.currentSrc}')`);
		$(ele).parent().parent().children().attr("style","");
		$(ele).parent().css("border-color","black");
	}

	all_img.click(function(){
		cur_img = this.dataset.pos;
		setImg(this);
	})

	// listen for click on slide button 
	sli_button.click(function(){
		if(this.dataset.to =="right")
			cur_img++;
		else if(this.dataset.to == "left")
			cur_img--;

		switch(cur_img){
			case img_len+1: // if current image is bigger than the all images length
				cur_img = 1;
				break;
			case img_len-img_len: // if current image is 0 
				cur_img = img_len;
				break;
			default:
				var s = "nth";
		}
		var next_img;
		$.each(all_img,function(){
			if(this.dataset.pos == cur_img){
				next_img = this;
			}
		})
		setImg(next_img);
	})
	// ----------- End product picture slide ------------
	


	// ----------- Supported product -----------
	function putNewPro(section, newProArr){
		$(section).empty();
		$(section).append(newProArr);	
	}

	// --- CPU ---
	var cpu_section = $(".all_pro_cont ul"); 
	var curr_cpu = $(".all_pro_cont ul li:not('.test')");
	var cpu_arr = $(".all_pro_cont ul li");
	var cpu_sli_btn = $(".sli_cpu");
	var cpu_pos = {
		"start":0,
		"end":2
	}

	// this 2 lines below dosen't use when there is server
	cpu_section.empty();
	cpu_section.append($(curr_cpu));
	
	// listen for click;
	cpu_sli_btn.click(function(){
		console.log("Click");
		if(this.dataset.to == "left"){
			console.log("left")
			if(cpu_pos.start < 2){
				return;// it will request from server,
			}else{
				cpu_pos.start -= 2;
				cpu_pos.end -= 2;
			}
			
		}else{
			if(cpu_pos.end == cpu_arr.length){
				return; // it will request from server,
			}else{
				cpu_pos.start += 2;
				cpu_pos.end += 2;
			}
		}
		// put the new product in
		curr_cpu = cpu_arr.slice(cpu_pos.start,cpu_pos.end);
		putNewPro(cpu_section,curr_cpu);
	})
    
})