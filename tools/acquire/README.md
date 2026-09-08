# Acquisition helpers

These utilities make explicit network requests to public services such as OpenAlex, Kaggle, or Google Drive. Inspect their command help and the relevant service terms before use. They are optional and are not invoked by CI or `make reproduce`.

`kaggle_image_audit.py` additionally requires Pillow. Keep downloaded files and intermediate inventories under the ignored `workspace/` tree unless an output is deliberately curated for publication.

