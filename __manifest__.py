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
            '/odoo_theme_backend/static/src/scss/theme_style.scss',
        },
    },
    'installable': True,
    'author': 'Youcef Messelem',
    'maintainer': 'Youcef Messelem',
    'support': 'messelemy@gmail.com',
}