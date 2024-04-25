

$(document).ready(function(){

    $("#itmlist").on('click', '.itmAdd', function() {
    	// alert('hello');
  // get the current row
  var currentRow = $(this).closest("tr");

  var col1 = currentRow.find(".itmname").html();
  var col2 = currentRow.find(".itmprice").html(); 
  var colid = currentRow.find(".itmid").html(); 
  var iqty = currentRow.find("input").val(); 

  var data = col1 + "" + col2;

  alert(iqty);
});
});