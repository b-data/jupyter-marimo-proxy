#!/usr/bin/env python3

import os
import json

def setup_marimoserver():
	with open(os.path.join(os.environ['HOME'], 'env.json'), 'w+', encoding='utf-8') as f:
		json.dump(dict(os.environ), f, ensure_ascii=False, indent=4)
	return {
		'command': ['marimo', 'edit', '--port', '{port}', '--base-url', '/user/' + os.environ['JUPYTERHUB_USER'] + '/marimo', '--no-token', '--headless'],
		'timeout': 60,
		'absolute_url': True,
		'launcher_entry': {
			'title': 'Marimo',
			'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
		},
	}
