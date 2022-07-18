# German MeSH Database

Provides a database that contains the 2022 edition of the german MeSH. The definitions are taken from the official download page https://repository.publisso.de/resource/frl%3A6432097.

This repository contains a script that downloads the definitions from the offical source and initializes the linked database with its contents.


## How to Use

This script can be executed locally or dockerized. For the latter one the latest image from the container repository can be used or can be built locally. Both require some container virtualization as Docker.

### Build the Image

The image can be built using Docker compose

```bash
docker compose -f docker-compose.build.yml
```

This creates an image tagged `ghcr.io/bih-cei/mesh-terms-de/import`.

### Execute

To starte the database and the import simply run

```bash
docker compose up -d [--url=<url>] [--force]
```

Per default the definitions stated at the introduction are used. This can be modified using the `--url=<url>` flag. This `<url>` needs to point directly to the download of the CSV archive (e.g. for the current version this is https://repository.publisso.de/resource/frl:6433711/data).

If started multiple times, the script will used the already cached definitions. To pull the latest ones (or if the URL was changed) one can use `--force` to force the download.
