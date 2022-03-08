{
    'name': 'Library_management',
    'version': '1.1',
    'category': 'Tools',
    'summary': 'Library_management',
    'depends': ['web'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'depends': [
        'sale',
        'mail',


     ],

    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_book_view.xml',
        # 'view/scientific.researches_view.xml',
        'view/publisher_view.xml',
        'view/publish_view.xml',
        'view/writer_view.xml',
        # 'view/novels_view.xml',
        'view/books_view.xml',
        'view/sale_view.xml',
    ]
    # 'demo': [
    #     'data/demo.xml',
    # ],
    # 'css': [],
    # 'installable': True,
    # 'auto_install': False,
    # 'application': True,

}

