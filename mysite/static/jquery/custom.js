




$(document).ready(function(){

    $("#itmlist").on('click', '.itmAdd', function() {
    	// alert('hello');
  // get the current row
  var currentRow = $(this).closest("tr");

  var col1 = currentRow.find(".itmname").html();
  var col2 = currentRow.find(".itmprice").html(); 
  var colid = currentRow.find(".itmid").html(); 
  var iqty = currentRow.find("input").val(); 

  var pri = parseInt(col2);
  var qt = parseInt(iqty);
  var amt = pri * qt;

  mydata = {itmname:col1, price:pri, qty:qy, amont:amt};
  $.ajax({
    url: "{% url 'save_invitm' %}",
    method: "POST",
    data:mydata,
    success: function(data){
    },
                    // console.log(data.status)
  });



//  alert(m);
});
});