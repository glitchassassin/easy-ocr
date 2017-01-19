# easy-ocr
An all-in-one pip module for Tesseract.

Most Python-Tesseract wrappers require you to already have Tesseract installed. This wrapper packages the latest build of Tesseract for an easy all-in-one install via `pip`.

## Build process

1. Update submodules (tesseract)
    * Pull Tesseract version
2. Compile Tesseract and Leptonica binaries
3. Build python-tesseract-sip wrapper