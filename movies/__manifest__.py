{
    'name': 'Movies',
    'version': '1.1',
    'category': 'Tools',
    'summary': 'Movies_management',
    'depends': ['web'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'depends': [],

    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/movie_view.xml',
        'views/director_view.xml',
        # 'views/actress_view.xml',
        'views/person_view.xml',
        'views/studio_view.xml',
        'views/actor_view.xml',
        'views/genres_view.xml',
        # 'view/books_view.xml',
        # 'view/sale_view.xml',
    ]
    # 'demo': [
    #     'data/demo.xml',
    # ],
    # 'css': [],
    # 'installable': True,
    # 'auto_install': False,
    # 'application': True,

}

