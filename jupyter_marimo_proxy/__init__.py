#!/usr/bin/env python3

import os
import shutil

def setup_marimoserver():
	exe = shutil.which('marimo', path=os.path.expanduser(os.path.join('~', '.local', 'bin')) + os.pathsep + os.environ.get('PATH', os.defpath)) or 'marimo'
	return {
		'command': [exe, 'edit', '--port', '{port}', '--base-url', '/user/' + os.environ['JUPYTERHUB_USER'] + '/marimo', '--no-token', '--headless'],
		'timeout': 60,
		'absolute_url': True,
		'launcher_entry': {
			'title': 'Marimo',
			'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
		},
	}
