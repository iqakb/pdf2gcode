# pdf2gcode

*Practical Report Plotter*

## Prerequisites

1. Install Rust environment
2. Install Python environment
3. Install cpp-poppler
4. Install ghostscript

## Installation Steps

1. Clone this repository
2. Install cargo svg2gcode by running:

```bash
cargo install --path cli/
```

## Usage Steps

1. Process your PDF file using:

```bash
./convertor.sh <yourpdf>
```

Ensure your PDF does not exceed 10000x10000mm. 

2. Review the generated G-code using [this viewer](https://zupfe.velor.ca/). If there are any anomalies, check the `processor.py` code.
3. Send the document's G-code to the 3D printer.
4. Calibrate your pen so that it touches the 3D printer bed or paper when z=5mm. Use serial communication or the 3D printer menu.
5. Set z=10mm.
6. Print your document's G-code.

## Calibration

1. The default offset is x=40mm and y=17mm. To check if it's correct, print the G-code file:

```bash
cal_4333_40_17.gcode
```

2. If it's incorrect, run the `offset.py` script with the following syntax:

```bash
python3.8 ~/larprak/offset.py -f <inputfile.gcode> -o <outputfile.gcode> -x <x offset in millimeters> -y <y offset in millimeters>
```

Example:

```bash
python3.8 ~/larprak/offset.py -f test.gcode -o shifted_test.gcode -x 12 -y -2.3
```

3. Adjust the offset in `cal_4333_40_17.gcode` as needed.
4. Recheck the offset results.

## Additional Tools

- `convertor.sh` — converts multi-page PDFs to G-code with artificial shifting.
- `convertor_s.sh` — converts single-page PDFs to G-code with artificial shifting.
- `processor.py` — converts G-code for use on a 3D printer with artificial shifting.
- `convertor.sh` — converts G-code for use on a 3D printer without artificial shifting.
- `offset.py` — shifts the entire G-code file.

