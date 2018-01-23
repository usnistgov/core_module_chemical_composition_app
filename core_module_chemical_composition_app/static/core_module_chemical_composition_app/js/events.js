$(document).on('click', '.periodic-table-multiple td.p-elem', function(event) {
    var chosenTable = openPopUp.find('.element-list');
    var elementName = $(this).text();

    var newRow = chosenTable.find('tr.sample-row').clone();
    newRow.show();
    newRow.removeClass('sample-row');
    newRow.find('td:first').text(elementName);

    chosenTable.find('.empty').hide();
    chosenTable.find('tbody').append(newRow);
});

$(document).on('click', '.element-list .remove-element', function(event) {
    var chosenTable = openPopUp.find('.element-list');
    var currentRow = $(this).parent().parent();

    if(currentRow.hasClass('saved')) {
        currentRow.hide();
        currentRow.addClass('hidden');
    } else {
        currentRow.remove();
    }

    console.log(chosenTable.find('tbody').children(':visible'));
    if(chosenTable.find('tbody').children(':visible').length === 0) {
        chosenTable.find('.empty').show();
    }
});
