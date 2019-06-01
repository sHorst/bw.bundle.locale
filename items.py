actions = {
    'regenerate_locale': {
        'command': 'locale-gen',
        'triggered': True,
    }
}

files = {
    "/etc/default/locale": {
        'source': "locale",
        'owner': "root",
        'group': "root",
        'mode': "0644"
    },
    "/etc/timezone": {
        'content': "Europe/Berlin\n",
        'owner': "root",
        'group': "root",
        'mode': "0644"
    },
    "/etc/locale.gen": {
        'content': "en_US.UTF-8 UTF-8\nde_DE.UTF-8 UTF-8\n",
        'owner': "root",
        'group': "root",
        'mode': "0644",
        'triggers': {
            'action:regenerate_locale',
        }
    }
}
