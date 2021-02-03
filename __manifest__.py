# -*- coding: utf-8 -*-
{
    'name': "Website Sale Field Remover",
    'summary': """
        Module for remove some fields""",
    'description': """
        Module for remove: company_name, пдв, улица, улица2, zip-code, страна. Страна по дефолту - Украина
    """,
    'category': 'Hidden',
    'version': '1.0',
    'depends': ['website_sale'],
    'auto_install': False,
    'data': [
        'views/website_sale_address_remove.xml',
    ],
}
