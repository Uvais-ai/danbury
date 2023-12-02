// $(document).ready(function () {
//     // Form Validation start
//     if ($('#contact-form').length) {
//         $("#contact-form").validate({
//             submitHandler: function (form, event) { // Include 'event' as a parameter
//                 event.preventDefault(); // Prevent the form from submitting normally
                
//                 var form_btn = $(form).find('button[type="submit"]');
//                 var form_result_div = '#form-result';
//                 $(form_result_div).remove();
//                 form_btn.before('<div id="form-result" class="alert alert-success" role="alert" style="display: none;"></div>');
//                 var form_btn_old_msg = form_btn.html();
//                 form_btn.html(form_btn.prop('disabled', true).data("loading-text"));
//                 // ajax start
//                 $(form).ajaxSubmit({
//                     dataType: 'json',
//                     success: function (data) {
//                         if (data.status == 'true') {
//                             $(form).find('.form-control').val('');
//                             $('.form-success-result').addClass('form-active'); // Activate the success div
//                         }
//                         form_btn.prop('disabled', false).html(form_btn_old_msg);
//                         $(form_result_div).html(data.message).fadeIn('slow');
//                     }
//                 }); 
//             }
//         });
//     }
// });






