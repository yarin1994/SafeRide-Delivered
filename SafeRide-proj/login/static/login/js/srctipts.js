
window.onload = function() {
  console.log("hello")
  if(window.location.href.includes("myScooters") ||window.location.href.includes("index") ){
 
    var cards = $(".bodycard")
    // console.log(testing)
    for(var i =0; i< cards.length; i++){
      for(var j = 0; j < testing.length; j++){
        var list_item = cards[i].children[1].children[1]
        if(list_item.innerHTML.includes(testing[j].brand)){
          img_path = img_folder_path + testing[j].url
          $( cards[i].children[0]).css('background-image', 'url(' + img_path + ')');        }
      }
    }

    $(".option").on("click", function(){
      var cards = $(".bodycard")
      console.log($(this).children()[0].value)
      var city = $(this).children()[0].value
      for(var i=0; i<cards.length; i++){
        if(cards[i].children[1].children[2].innerHTML.includes(city) || city === "None"){
        
                $(cards[i]).show()
        }
        else $(cards[i]).hide()
        
      }
      
         
      })
      

    
    
};
}





$(".dropbtn").on("click",function(){
  var x= $(".dropdown-content")
  for(var i=0; i<x.length; i++){
    x[i].classList.toggle("hide")
  }
  $(this).siblings()[0].classList.toggle("show");

  }); 




$("#all_button").on("click",function(){
  if (($("input[name*='status']:checked").length)<=0 || ($("input[name*='helmet']:checked").length)<=0) {
      alert("You must check at least 1 box");
  }
  return true;
});
