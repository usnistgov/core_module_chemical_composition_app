/** Chemical composition script */
saveChemicalElementCompositionData = function() {
    let jqModuleOpenModal = $($("#modal-" + moduleElement[0].id)[0]);
    let hiddenSavedElements = jqModuleOpenModal.find('.saved:hidden');
    $.each(hiddenSavedElements, function(index, hiddenElement) {
        $(hiddenElement).remove();
    });

    let elementList = jqModuleOpenModal.find('.element-list tbody');
    let data = [];
    $.each(elementList.find('tr'), function(index, element) {
        let $element = $(element);
        let elementData = {};

        if(!$element.hasClass('empty')) {
            // name
            elementData.name = $element.find('.name').text();
            // qty
            elementData.qty = $element.find('.qty input').val();
            $element.find('.qty :input').attr('value', elementData.qty);
            // pur
            elementData.pur = $element.find('.pur input').val();
            $element.find('.pur :input').attr('value', elementData.pur);
            // err
            elementData.err = $element.find('.err input').val();
            $element.find('.err :input').attr('value', elementData.err);

            data.push(elementData);
        }
    });

    return {'elementList': JSON.stringify(data)};
}

let chemicalElementCompositionPopupOptions = {
    title: "Chemical Composition",
    getData: saveChemicalElementCompositionData
}

configurePopUp('module-chemical-composition',
                chemicalElementCompositionPopupOptions);

