""" Chemical composition module view
"""
import json

from django.template import loader
from xml_utils.xsd_tree.xsd_tree import XSDTree
from core_parser_app.tools.modules.views.builtin.popup_module import AbstractPopupModule
from core_parser_app.tools.modules.views.module import AbstractModule


class ChemicalCompositionModule(AbstractPopupModule):
    def __init__(self):

        template = AbstractModule.render_template('core_module_periodic_table_app/periodic.html')
        popup_content = AbstractModule.render_template('core_module_chemical_composition_app/'
                                                       'chemical_composition.html',
                                                       {'periodic_table': template})

        AbstractPopupModule.__init__(self, popup_content=popup_content, button_label='Select Element',
                                     styles=['core_module_periodic_table_app/css/periodic.css',
                                             'core_module_chemical_composition_app/css/'
                                             'chemical_element_composition.css'],
                                     scripts=['core_module_chemical_composition_app/js/events.js',
                                              'core_module_chemical_composition_app/js/'
                                              'chemical_element_composition.js'])

    def _retrieve_data(self, request):
        """ Retrieve module's data

        Args:
            request:

        Returns:

        """
        data = ''
        if request.method == 'GET':
            if 'data' in request.GET:
                data = request.GET['data']
        elif request.method == 'POST':
            if 'elementList' in request.POST:
                element_list = json.loads(request.POST['elementList'])
                if len(element_list) > 0:
                    element_list_xml = ""
                    for element in element_list:
                        element_list_xml += '<constituent>'
                        element_list_xml += "<element>" + element['name'] + "</element>"
                        element_list_xml += "<quantity>" + element['qty'] + "</quantity>"
                        element_list_xml += "<purity>" + element['pur'] + "</purity>"
                        element_list_xml += "<error>" + element['err'] + "</error>"
                        element_list_xml += '</constituent>'

                    # set the data
                    data = element_list_xml
        return data

    def _render_data(self, request):
        """ Return module's data rendering

        Args:
            request:

        Returns:

        """
        return render_chemical_composition(self.data, True, True)


def render_chemical_composition(data_constituents, display_purity, display_error):
    if len(data_constituents) > 0:
        constituents = XSDTree.fromstring("<constituents>" + data_constituents + "</constituents>")

        # build data to display
        if len(constituents) > 0:
            data = []
            for constituent in constituents:
                constituent_elements = list(constituent)
                name = ''
                quantity = ''
                purity = ''
                error = ''
                for constituent_element in constituent_elements:
                    if constituent_element.tag == 'element':
                        if constituent_element.text is not None:
                            name = constituent_element.text
                    elif constituent_element.tag == 'quantity':
                        if constituent_element.text is not None:
                            quantity = constituent_element.text
                    elif constituent_element.tag == 'purity':
                        if constituent_element.text is not None:
                            purity = constituent_element.text
                    elif constituent_element.tag == 'error':
                        if constituent_element.text is not None:
                            error = constituent_element.text

                item = {
                    'name': name,
                    'quantity': quantity,
                    'purity': purity,
                    'error': error
                }

                data.append(item)

            # template loading with context
            template = loader.get_template('core_module_chemical_composition_app/render_data.html')
            context = {
                'purity': display_purity,
                'error': display_error,
                'data': data
            }

            return template.render(context)
        return 'No selected element.'
    return 'No selected element.'
