




$(document).ready(function(){

    $("#itmlist").on('click', '.itmAdd', function() {
    	// alert('hello');
        // console.log(cu);
  // get the current row
  var currentRow = $(this).closest("tr");

  var col1 = currentRow.find(".itmname").html();
  var col2 = currentRow.find(".itmprice").html(); 
  var colid = currentRow.find(".itmid").html(); 
  var iqty = currentRow.find("input").val(); 

  var pri = parseInt(col2);
  var qt = parseInt(iqty);
  var amt = pri * qt;

  var cu = $("#cusName").val();
    // console.log(cu);
  // ata = {itmname:col1, price:pri, qty:qy, amont:amt};
  // alert('helo')
  $.ajax({
    url: "/save_invitm/",
    method: "GET",
    data:{itmname:col1, price:pri, qty:qt, amont:amt, cu:cu},
    success: function(data){
        // console.log(data.status);

        alert('Item Add Successfully');
        window.setTimeout(function(){ } ,2000);
                        location.reload();

        // window.location.href = '/admin/';
        // window.open('https://www.codexworld.com', '_blank');
    },
    error:function(){
        alert('having some error contact to developer');
    },
                    
  });
  //end ajax

});
});