# \<test-qz\>

pour installer les dependances

 bower  install

pour generer les fichiers json
 
sur zephir

pour creer jeu de fichier json

 #!/usr/bin/env python
 # -*- coding: UTF-8 -*- 

 import sys,xmlrpclib,json
 login='admin'
 passwd=file('/root/admin.pwd').readline().split('\n')[0]
 adresse_zephir='localhost'
 id=1088 

 proxy = xmlrpclib.ServerProxy('http://%s:%s@%s:7081' % (login,passwd,adresse_zephir))
 
 rc,grp_serveurs=proxy.serveurs.get_config(id)
 json.dump(grp_serveurs, open("config.json",'w')) 
 
 rc,grp_etabs=proxy.etabs.get_etab()
 json.dump(grp_etabs, open("etabs.json",'w'))
 
 rc,grp_serveurs=proxy.serveurs.groupe_serveur(criteres_selection)
 json.dump(grp_serveurs, open("serveurs.json",'w'))


recuperer les fichiers et les mettre dans src/test-qz-app/


## Install the Polymer-CLI

First, make sure you have the [Polymer CLI](https://www.npmjs.com/package/polymer-cli) installed. Then run `polymer serve` to serve your application locally.

## Viewing Your Application

```
$ polymer serve
```

## Building Your Application

```
$ polymer build
```

This will create a `build/` folder with `bundled/` and `unbundled/` sub-folders
containing a bundled (Vulcanized) and unbundled builds, both run through HTML,
CSS, and JS optimizers.

You can serve the built versions by giving `polymer serve` a folder to serve
from:

```
$ polymer serve build/bundled
```

## Running Tests

```
$ polymer test
```

Your application is already set up to be tested via [web-component-tester](https://github.com/Polymer/web-component-tester). Run `polymer test` to run your application's test suite locally.
