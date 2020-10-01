/** Event management script for the Chemical composition module */
$(document).on('click', '.periodic-table-multiple td.p-elem', function(event) {
    let jqModuleOpenModal = $($("#modal-" + moduleElement[0].id)[0]);
    let chosenTable = jqModuleOpenModal.find('.element-list');
    // if an element is already on the list (selected)
    // so we don't add it again
    if(!$(this).hasClass('selected')) {
        let elementName = $(this).text();
        $(this).addClass('selected');
        let newRow = chosenTable.find('tr.sample-row').clone();
        newRow.show();
        newRow.removeClass('sample-row');
        newRow.find('td:first').text(elementName);
        chosenTable.find('.empty').hide();
        chosenTable.find('tbody').append(newRow);
    }
});

$(document).on('click', '.element-list .remove-element', function(event) {
    let jqModuleOpenModal = $($("#modal-" + moduleElement[0].id)[0]);
    let chosenTable = jqModuleOpenModal.find('.element-list');
    let currentRow = $(this).parent().parent();

    // unselect the periodic table element
    let elementText = $(currentRow).find("td:first").text();
    $.each($('.periodic-table-multiple td.p-elem'), function(index, element){
        if($(element).text() === elementText){
            $(element).removeClass('selected');
        }
    })

    // remove the row from the table
    currentRow.remove();
});
