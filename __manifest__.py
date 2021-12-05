{
    'name': 'Odoo Backend Theme',
    'summary': 'Change Odoo theme color',
    'sequence': 15,
    'description': """Change the default color of odoo backend""",
    'depends': [
        'base',
        'web',
        'mail',
    ],
    'data': [
        'views/layout.xml',
    ],
    'assets': {
        'web.assets_backend': {
            '\gradient-theme-odoo15\static\src\scss\style.scss',
        },
    },
    'installable': True,
    'author': 'Youcef Messelem',
    'maintainer': 'Youcef Messelem',
    'support': 'messelemy@gmail.com',
}