$(function(){
    $('#progressBar').hide()
    $('#btnSubmit').click(function () {
        progressBar(0, $('#progressBar'))
        $('#progressBar').show();
        for (var x = 0; x <= 100; x += 2){
            progressBar(x, $('#progressBar'));
        }
    })
});
function progressBar(percent, $element) {
        var progressBarWidth = percent * $element.width() / 100;
        $element.find('div').animate({ width: progressBarWidth }, 500).html(percent + "%&nbsp;");
}
/**
 * Created by Henrique on 04/04/2015.
 */

