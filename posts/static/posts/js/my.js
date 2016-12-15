$(document).ready(function () {

$('#loginpopup').click(function(e){
    e.preventDefault();
    swal("Good job!", "You clicked the button!", "success");
    }
);

$('#popup2').click(function(e){
    e.preventDefault();
    swal("Here's a message!", "It's pretty, isn't it?");
    }
);
$('#popup3').click(function(e){
    e.preventDefault();
    swal({
  title: "Are you sure?",
  text: "You will not be able to recover this imaginary file!",
  type: "warning",
  showCancelButton: true,
  confirmButtonColor: "#DD6B55",
  confirmButtonText: "Yes, delete it!",
  closeOnConfirm: false
},
function(){
  swal("Deleted!", "Your imaginary file has been deleted.", "success");
});
    }
);
$('#popup4').click(function(e){
    e.preventDefault();
    swal({
  title: "Are you sure?",
  text: "You will not be able to recover this imaginary file!",
  type: "warning",
  showCancelButton: true,
  confirmButtonColor: "#DD6B55",
  confirmButtonText: "Yes, delete it!",
  cancelButtonText: "No, cancel plx!",
  closeOnConfirm: false,
  closeOnCancel: false
},
function(isConfirm){
  if (isConfirm) {
    swal("Deleted!", "Your imaginary file has been deleted.", "success");
  } else {
    swal("Cancelled", "Your imaginary file is safe :)", "error");
  }
});
    }
);
$('#popup1').click(function(e){
    e.preventDefault();
    swal({
  title: "Sweet!",
  text: "Here's a custom image.",
  imageUrl: "images/thumbs-up.jpg"
});
    }
);












});