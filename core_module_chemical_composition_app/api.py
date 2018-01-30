""" Chemical composition API
"""
from django.template import loader
from core_parser_app.tools.modules.views.module import AbstractModule
from xml_utils.xsd_tree.xsd_tree import XSDTree


def get_chemical_composition_popup_content(data, edit_template):
    """ Chemical_composition module's rendering
    """
    # rendering data in the periodic table
    template = AbstractModule.render_template('core_module_periodic_table_app/periodic.html',
                                              {'selected_elements': get_periodic_table_selected_elements(data)})

    # rendering both form in the popup template
    return AbstractModule.render_template('core_module_chemical_composition_app/chemical_composition.html',
                                          {'periodic_table': template,
                                           'data_template': edit_template})


def get_periodic_table_selected_elements(data_constituents):
    """ get selected elements from xml constituents

    Args:
        data_constituents:

    Returns: selected_elements
    """
    selected_elements = []
    constituents = XSDTree.fromstring("<constituents>" + data_constituents + "</constituents>")
    for constituent in constituents:
        constituent_elements = list(constituent)
        for constituent_element in constituent_elements:
            if constituent_element.tag == 'element':
                if constituent_element.text is not None:
                    selected_elements.append(constituent_element.text)
    return selected_elements


def render_chemical_composition(data_constituents, display_purity, display_error, template):
    """ render elements from xml constituents using the given template

    Args:
        data_constituents:
        display_purity:
        display_error:
        template:

    Returns: selected_elements
    """
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
            template = loader.get_template(template)
            context = {
                'purity': display_purity,
                'error': display_error,
                'data': data
            }

            return template.render(context)
        return 'No selected element.'
    return 'No selected element.'
