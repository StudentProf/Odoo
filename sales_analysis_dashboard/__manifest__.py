{
    'name': 'Sales Analysis Dashboard',
    'summary': 'Preconfigured sales analysis dashboard with pivot, graph, and filters for Odoo 17',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'license': 'LGPL-3',
    'author': 'Your Company',
    'website': 'https://example.com',
    'depends': ['sale', 'web'],
    'data': [
        'views/sales_dashboard_menu.xml',
        'views/sale_report_views.xml',
        'data/ir_filters.xml',
    ],
    'installable': True,
    'application': False,
}