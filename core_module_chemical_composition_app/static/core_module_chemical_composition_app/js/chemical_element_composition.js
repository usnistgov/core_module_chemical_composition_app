var chemicalElementCompositionPopupOptions = {
    width: 700,
    title: "Periodic Table",
    create: function(event, ui) {
        // Initialization
        $(this).find('.sample-row').hide();
        $(this).find('.saved-data').hide();

        var elements = $(this).find('.element-list tbody tr:not(.empty)');
        var savedElementCount = 0;
        $.each(elements, function(index, element) {
            var $element = $(element);

            if($element.hasClass('saved')) {
                savedElementCount += 1;

                if($element.is(':hidden')) {
                    $element.show();
                }

                var qty = $element.find('.qty .saved-data').text();
                $element.find('.qty input').val(qty);

                var pur = $element.find('.pur .saved-data').text();
                $element.find('.pur input').val(pur);

                var err = $element.find('.err .saved-data').text();
                $element.find('.err input').val(err);
            } else {
                $element.remove();
            }
        });

        console.log('saved:' + savedElementCount);
        if(savedElementCount === 0) {
            $(this).find('.element-list .empty').show();
        }
    },
}

saveChemicalElementCompositionData = function() {
    var hiddenSavedElements = openPopUp.find('.saved:hidden');
    $.each(hiddenSavedElements, function(index, hiddenElement) {
        $(hiddenElement).remove();
    });

    var elementList = openPopUp.find('.element-list tbody');
    var data = [];

    $.each(elementList.find('tr'), function(index, element) {
        var $element = $(element);
        var elementData = {};

        if(!$element.hasClass('empty')) {
            $element.addClass('saved');

            elementData.name = $element.find('.name').text();
            elementData.qty = $element.find('.qty input').val();
            $element.find('.qty .saved-data').text(elementData.qty);

            elementData.pur = $element.find('.pur input').val();
            $element.find('.pur .saved-data').text(elementData.pur);

            elementData.err = $element.find('.err input').val();
            $element.find('.err .saved-data').text(elementData.err);

            data.push(elementData);
        }
    });

    return {'elementList': JSON.stringify(data)};
}

configurePopUp('module-chemical-composition',
                chemicalElementCompositionPopupOptions,
                saveChemicalElementCompositionData);
